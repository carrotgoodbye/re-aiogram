from aiogram import BaseMiddleware as _BaseMiddleware
from aiogram.types import (
    Message,
    InputMediaPhoto,
    InputMediaVideo,
    InputMediaDocument,
    InputMediaAudio,
    InputMedia,
)
from typing import Callable, Any, Awaitable, Union, List
import asyncio
import time
import logging

logger = logging.getLogger(__name__)


class MediaGroup(list):
    """
    Custom list-like class for media groups.
    Inherits from list for full aiogram compatibility (answer_media_group, etc.)
    while providing convenient properties for introspection.
    """

    def __init__(
        self,
        messages: List[Message],
        media: List[Union[InputMediaPhoto, InputMediaVideo, InputMediaDocument, InputMediaAudio, InputMedia]],
    ):
        super().__init__(media)
        self._messages = messages

    @property
    def messages(self) -> List[Message]:
        """Original aiogram Message objects."""
        return self._messages.copy()

    @property
    def photos(self) -> List[Message]:
        """Messages containing photos."""
        return [m for m in self._messages if m.photo]

    @property
    def videos(self) -> List[Message]:
        """Messages containing videos."""
        return [m for m in self._messages if m.video]

    @property
    def documents(self) -> List[Message]:
        """Messages containing documents."""
        return [m for m in self._messages if m.document]

    @property
    def audio(self) -> List[Message]:
        """Messages containing audio files."""
        return [m for m in self._messages if m.audio]

    @property
    def caption(self) -> Union[str, None]:
        """First caption found in the group (Telegram sends caption only on the first item)."""
        for msg in self._messages:
            if msg.caption:
                return msg.caption
        return None

    @property
    def captions(self) -> List[str]:
        """All captions from the group."""
        return [msg.caption for msg in self._messages if msg.caption]

    @property
    def is_mixed(self) -> bool:
        """True if album contains different media types."""
        types = {m.content_type for m in self._messages}
        return len(types) > 1

    @property
    def count(self) -> int:
        """Number of items in the group."""
        return len(self._messages)

    def __repr__(self) -> str:
        types = [m.content_type for m in self._messages]
        return f"<MediaGroup count={self.count} types={types}>"


class AlbumMiddleware(_BaseMiddleware):
    """
    Middleware for media groups with memory leak protection.
    Injects a MediaGroup instance into the handler data.
    """

    def __init__(
        self,
        latency: Union[int, float] = 0.01,
        max_age: Union[int, float] = 60.0,
    ):
        self.latency = latency
        self.max_age = max_age
        self.album_data: dict[str, list[Message]] = {}
        self._last_access: dict[str, float] = {}
        self._lock = asyncio.Lock()

    async def __call__(
        self,
        handler: Callable[[Message, dict[str, Any]], Awaitable[Any]],
        message: Message,
        data: dict[str, Any],
    ) -> Any:
        if not message.media_group_id:
            return await handler(message, data)

        await self._cleanup_old_albums()

        async with self._lock:
            if message.media_group_id in self.album_data:
                self.album_data[message.media_group_id].append(message)
                self._last_access[message.media_group_id] = time.time()
                return None

            self.album_data[message.media_group_id] = [message]
            self._last_access[message.media_group_id] = time.time()

        await asyncio.sleep(self.latency)

        async with self._lock:
            album = sorted(
                self.album_data.get(message.media_group_id, []),
                key=lambda m: m.message_id,
            )

            media_items: list = []
            for msg in album:
                if msg.photo:
                    file_id = msg.photo[-1].file_id
                    caption = msg.caption if msg.caption else None
                    media_items.append(InputMediaPhoto(media=file_id, caption=caption))
                elif msg.video:
                    file_id = msg.video.file_id
                    caption = msg.caption if msg.caption else None
                    media_items.append(InputMediaVideo(media=file_id, caption=caption))
                elif msg.document:
                    file_id = msg.document.file_id
                    caption = msg.caption if msg.caption else None
                    media_items.append(InputMediaDocument(media=file_id, caption=caption))
                elif msg.audio:
                    file_id = msg.audio.file_id
                    caption = msg.caption if msg.caption else None
                    media_items.append(InputMediaAudio(media=file_id, caption=caption))
                else:
                    try:
                        obj_dict = msg.model_dump()
                        file_id = obj_dict[msg.content_type]["file_id"]
                        media_items.append(InputMedia(media=file_id))
                    except (KeyError, TypeError):
                        logger.warning(
                            "Unsupported media type in album: %s", msg.content_type
                        )

            data["_is_last"] = True
            data["album"] = album
            data["media_group"] = MediaGroup(album, media_items)

        try:
            return await handler(message, data)
        finally:
            async with self._lock:
                self.album_data.pop(message.media_group_id, None)
                self._last_access.pop(message.media_group_id, None)

    async def _cleanup_old_albums(self):
        now = time.time()
        stale_ids = [
            mg_id
            for mg_id, last_time in list(self._last_access.items())
            if now - last_time > self.max_age
        ]
        if stale_ids:
            async with self._lock:
                for mg_id in stale_ids:
                    self.album_data.pop(mg_id, None)
                    self._last_access.pop(mg_id, None)
            logger.debug("Cleaned up %d stale album entries", len(stale_ids))