from aiogram import Bot as _Bot, Dispatcher as _Dispatcher
import asyncio
import logging
import signal
import sys
import importlib
import os
from dotenv import load_dotenv


class Bot:
    """
    Bot class.
    """

    # Methods from aiogram.Bot
    _BOT_METHODS = frozenset({
        "send_message",
        "send_photo",
        "send_video",
        "send_audio",
        "send_document",
        "send_animation",
        "send_voice",
        "send_video_note",
        "send_media_group",
        "send_location",
        "send_venue",
        "send_contact",
        "send_poll",
        "send_dice",
        "send_chat_action",
        "send_sticker",
        "get_file",
        "get_file_url",
        "download_file",
        "get_me",
        "get_chat",
        "get_chat_member",
        "get_chat_member_count",
        "get_chat_administrators",
        "ban_chat_member",
        "unban_chat_member",
        "restrict_chat_member",
        "promote_chat_member",
        "set_chat_permissions",
        "set_chat_title",
        "set_chat_description",
        "set_chat_photo",
        "delete_chat_photo",
        "pin_chat_message",
        "unpin_chat_message",
        "unpin_all_chat_messages",
        "leave_chat",
        "answer_callback_query",
        "answer_inline_query",
        "edit_message_text",
        "edit_message_caption",
        "edit_message_media",
        "edit_message_reply_markup",
        "delete_message",
        "delete_messages",
        "forward_message",
        "copy_message",
        "copy_messages",
        "create_invoice_link",
        "send_invoice",
        "answer_shipping_query",
        "answer_pre_checkout_query",
        "set_my_commands",
        "delete_my_commands",
        "get_my_commands",
        "set_my_default_administrator_rights",
        "get_my_default_administrator_rights",
        "set_chat_menu_button",
        "get_chat_menu_button",
        "set_webhook",
        "delete_webhook",
        "get_webhook_info",
        "get_updates",
        "close",
        "session",
        "token",
    })

    def __init__(self, token: str = None, env_token: str | None = None):
        # token
        if token:
            self._token = token
        elif env_token:
            load_dotenv()
            self._token = os.getenv(env_token)
            if not self._token:
                raise ValueError(f"Environment variable '{env_token}' not found or empty")
        else:
            raise ValueError("Token is required: pass 'token' or 'env_token'")

        self._bot = _Bot(token=self._token)
        self._dp = _Dispatcher()

        # middlewares
        from .mediagroup import AlbumMiddleware
        self._dp.message.middleware(AlbumMiddleware())

    def __getattr__(self, name: str):
        if name in self._BOT_METHODS:
            return getattr(self._bot, name)
        raise AttributeError(
            f"'{self.__class__.__name__}' object has no attribute '{name}'"
        )

    @property
    def message(self):
        return self._dp.message

    def load(self, *paths: str):
        """
        Load routers from the specified paths.

        :param paths:
        """
        routers = []
        for path in paths:
            module = importlib.import_module(path)
            if hasattr(module, "router"):
                routers.append(module.router)
            else:
                raise ValueError(f"There is no 'router' variable in the {path} module")
        for router in routers:
            if router.parent_router is None:
                self._dp.include_router(router)

    def run(self, logging_enabled: bool = True):
        """
        Start the Bot with graceful shutdown.
        """
        if logging_enabled:
            logging.basicConfig(level=logging.INFO)
        try:
            asyncio.run(self._start())
        except (KeyboardInterrupt, SystemExit):
            logging.info("Bot stopped.")
        except Exception as e:
            logging.error("Polling error: %s", e)
            sys.exit(1)

    async def _start(self):
        """Start polling and ensure cleanup on exit."""
        loop = asyncio.get_running_loop()

        # Register signal handlers for graceful shutdown where supported
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.add_signal_handler(sig, self._request_shutdown)
            except (NotImplementedError, ValueError):
                break
        try:
            await self._dp.start_polling(self._bot)
        finally:
            await self._shutdown() # sixsevenn

    def _request_shutdown(self):
        """Signal handler: initiate graceful stop."""
        logging.debug("Shutdown signal received, stopping polling...")
        asyncio.create_task(self._dp.stop_polling())

    async def _shutdown(self):
        """Close sessions and clean up resources."""
        logging.debug("Closing bot session...")
        await self._bot.session.close()
        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.remove_signal_handler(sig)
            except (NotImplementedError, ValueError):
                pass
