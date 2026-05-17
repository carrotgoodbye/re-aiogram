from aiogram import Bot as _Bot, Dispatcher as _Dispatcher
from aiogram.types import (
    Message,
    CallbackQuery,
    InlineQuery,
    Chat,
    ChatMember,
    ChatPermissions,
    ChatAdministratorRights,
    MenuButton,
    WebhookInfo,
    Update,
    InputFile,
    InputMedia,
    InputMediaPhoto,
    InputMediaVideo,
    InputMediaAudio,
    InputMediaDocument,
    InputMediaAnimation,
    ForceReply,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    LabeledPrice,
    ShippingOption,
    BotCommand,
    BotCommandScope,
    MessageEntity,
    InputPollOption,
    InlineQueryResult,
    SentWebAppMessage,
    UserProfilePhotos,
    File,
    User,
    ChatFullInfo,
    Sticker,
    InputSticker,
    MaskPosition,
    InlineQueryResultsButton,
    PreparedInlineMessage,
    BusinessConnection,
    StarTransactions,
    RefundedPayment,
    RevenueWithdrawalState,
    TransactionPartner,
    Gift,
    Gifts,
    OwnedGifts,
    AcceptedGiftTypes,
    InputPaidMedia,
    PaidMediaPurchased,
    LinkPreviewOptions,
    ChatInviteLink,
    ChatJoinRequest,
    ForumTopic,
    GameHighScore,
    PassportElementError,
    ShippingAddress,
    OrderInfo,
    SuccessfulPayment,
    StarTransaction,
    InputProfilePhoto,
    InputStoryContent,
    Story,
    ExternalReplyInfo,
    TextQuote,
    LinkPreviewOptions,
    BackgroundFill,
    BackgroundType,
    Birthdate,
    BusinessIntro,
    BusinessLocation,
    BusinessOpeningHours,
    ChatLocation,
    ChatPhoto,
    ReactionType,
    ReactionCount,
    MessageReactionUpdated,
    MessageReactionCountUpdated,
    BotName,
    BotDescription,
    BotShortDescription,
    SwitchInlineQueryChosenChat,
    CallbackGame,
    LoginUrl,
    CopyTextButton,
    WebAppInfo,
)
from aiogram.methods import (
    SendMessage,
    SendPhoto,
    SendVideo,
    SendAudio,
    SendDocument,
    SendAnimation,
    SendVoice,
    SendVideoNote,
    SendMediaGroup,
    SendLocation,
    SendVenue,
    SendContact,
    SendPoll,
    SendDice,
    SendChatAction,
    SendSticker,
    GetFile,
    GetMe,
    GetChat,
    GetChatMember,
    GetChatMemberCount,
    GetChatAdministrators,
    BanChatMember,
    UnbanChatMember,
    RestrictChatMember,
    PromoteChatMember,
    SetChatPermissions,
    SetChatTitle,
    SetChatDescription,
    SetChatPhoto,
    DeleteChatPhoto,
    PinChatMessage,
    UnpinChatMessage,
    UnpinAllChatMessages,
    LeaveChat,
    AnswerCallbackQuery,
    AnswerInlineQuery,
    EditMessageText,
    EditMessageCaption,
    EditMessageMedia,
    EditMessageReplyMarkup,
    DeleteMessage,
    DeleteMessages,
    ForwardMessage,
    CopyMessage,
    CopyMessages,
    CreateInvoiceLink,
    SendInvoice,
    AnswerShippingQuery,
    AnswerPreCheckoutQuery,
    SetMyCommands,
    DeleteMyCommands,
    GetMyCommands,
    SetMyDefaultAdministratorRights,
    GetMyDefaultAdministratorRights,
    SetChatMenuButton,
    GetChatMenuButton,
    SetWebhook,
    DeleteWebhook,
    GetWebhookInfo,
    GetUpdates,
)
from aiogram.client.session.base import BaseSession
from typing import Any, List, Union, Optional, Sequence


class Bot:
    message: Any

    def __init__(self, token: str = None, env_token: str | None = None) -> None: ...

    # === Proxied aiogram.Bot methods ===

    async def send_message(
        self,
        chat_id: Union[int, str],
        text: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_photo(
        self,
        chat_id: Union[int, str],
        photo: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_video(
        self,
        chat_id: Union[int, str],
        video: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        cover: Optional[Union[str, InputFile]] = None,
        start_timestamp: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        supports_streaming: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_audio(
        self,
        chat_id: Union[int, str],
        audio: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        performer: Optional[str] = None,
        title: Optional[str] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_document(
        self,
        chat_id: Union[int, str],
        document: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        disable_content_type_detection: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_animation(
        self,
        chat_id: Union[int, str],
        animation: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        has_spoiler: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_voice(
        self,
        chat_id: Union[int, str],
        voice: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        duration: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_video_note(
        self,
        chat_id: Union[int, str],
        video_note: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        duration: Optional[int] = None,
        length: Optional[int] = None,
        thumbnail: Optional[Union[str, InputFile]] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_media_group(
        self,
        chat_id: Union[int, str],
        media: List[Union[InputMediaPhoto, InputMediaVideo, InputMediaAudio, InputMediaDocument]],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
    ) -> List[Message]: ...

    async def send_location(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        horizontal_accuracy: Optional[float] = None,
        live_period: Optional[int] = None,
        heading: Optional[int] = None,
        proximity_alert_radius: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_venue(
        self,
        chat_id: Union[int, str],
        latitude: float,
        longitude: float,
        title: str,
        address: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        foursquare_id: Optional[str] = None,
        foursquare_type: Optional[str] = None,
        google_place_id: Optional[str] = None,
        google_place_type: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_contact(
        self,
        chat_id: Union[int, str],
        phone_number: str,
        first_name: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        last_name: Optional[str] = None,
        vcard: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_poll(
        self,
        chat_id: Union[int, str],
        question: str,
        options: List[InputPollOption],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        question_parse_mode: Optional[str] = None,
        question_entities: Optional[List[MessageEntity]] = None,
        is_anonymous: Optional[bool] = None,
        type: Optional[str] = None,
        allows_multiple_answers: Optional[bool] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_parse_mode: Optional[str] = None,
        explanation_entities: Optional[List[MessageEntity]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[int] = None,
        is_closed: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_dice(
        self,
        chat_id: Union[int, str],
        emoji: Optional[str] = None,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def send_chat_action(
        self,
        chat_id: Union[int, str],
        action: str,
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
    ) -> bool: ...

    async def send_sticker(
        self,
        chat_id: Union[int, str],
        sticker: Union[str, InputFile],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        emoji: Optional[str] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def get_file(self, file_id: str) -> File: ...

    async def get_file_url(self, file_id: str) -> str: ...

    async def download_file(
        self,
        file_path: str,
        destination: Optional[Any] = None,
        timeout: Optional[int] = None,
        chunk_size: Optional[int] = None,
    ) -> Any: ...

    async def get_me(self) -> User: ...

    async def get_chat(self, chat_id: Union[int, str]) -> ChatFullInfo: ...

    async def get_chat_member(self, chat_id: Union[int, str], user_id: int) -> ChatMember: ...

    async def get_chat_member_count(self, chat_id: Union[int, str]) -> int: ...

    async def get_chat_administrators(self, chat_id: Union[int, str]) -> List[ChatMember]: ...

    async def ban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        until_date: Optional[int] = None,
        revoke_messages: Optional[bool] = None,
    ) -> bool: ...

    async def unban_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        only_if_banned: Optional[bool] = None,
    ) -> bool: ...

    async def restrict_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
        until_date: Optional[int] = None,
    ) -> bool: ...

    async def promote_chat_member(
        self,
        chat_id: Union[int, str],
        user_id: int,
        is_anonymous: Optional[bool] = None,
        can_manage_chat: Optional[bool] = None,
        can_delete_messages: Optional[bool] = None,
        can_manage_video_chats: Optional[bool] = None,
        can_restrict_members: Optional[bool] = None,
        can_promote_members: Optional[bool] = None,
        can_change_info: Optional[bool] = None,
        can_invite_users: Optional[bool] = None,
        can_post_messages: Optional[bool] = None,
        can_edit_messages: Optional[bool] = None,
        can_pin_messages: Optional[bool] = None,
        can_post_stories: Optional[bool] = None,
        can_edit_stories: Optional[bool] = None,
        can_delete_stories: Optional[bool] = None,
        can_manage_topics: Optional[bool] = None,
    ) -> bool: ...

    async def set_chat_permissions(
        self,
        chat_id: Union[int, str],
        permissions: ChatPermissions,
        use_independent_chat_permissions: Optional[bool] = None,
    ) -> bool: ...

    async def set_chat_title(self, chat_id: Union[int, str], title: str) -> bool: ...

    async def set_chat_description(
        self, chat_id: Union[int, str], description: Optional[str] = None
    ) -> bool: ...

    async def set_chat_photo(
        self, chat_id: Union[int, str], photo: Union[str, InputFile]
    ) -> bool: ...

    async def delete_chat_photo(self, chat_id: Union[int, str]) -> bool: ...

    async def pin_chat_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
        business_connection_id: Optional[str] = None,
        disable_notification: Optional[bool] = None,
    ) -> bool: ...

    async def unpin_chat_message(
        self,
        chat_id: Union[int, str],
        business_connection_id: Optional[str] = None,
        message_id: Optional[int] = None,
    ) -> bool: ...

    async def unpin_all_chat_messages(
        self, chat_id: Union[int, str], business_connection_id: Optional[str] = None
    ) -> bool: ...

    async def leave_chat(self, chat_id: Union[int, str]) -> bool: ...

    async def answer_callback_query(
        self,
        callback_query_id: str,
        text: Optional[str] = None,
        show_alert: Optional[bool] = None,
        url: Optional[str] = None,
        cache_time: Optional[int] = None,
    ) -> bool: ...

    async def answer_inline_query(
        self,
        inline_query_id: str,
        results: List[InlineQueryResult],
        cache_time: Optional[int] = None,
        is_personal: Optional[bool] = None,
        next_offset: Optional[str] = None,
        button: Optional[InlineQueryResultsButton] = None,
    ) -> bool: ...

    async def edit_message_text(
        self,
        text: str,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        business_connection_id: Optional[str] = None,
        parse_mode: Optional[str] = None,
        entities: Optional[List[MessageEntity]] = None,
        link_preview_options: Optional[LinkPreviewOptions] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]: ...

    async def edit_message_caption(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]: ...

    async def edit_message_media(
        self,
        media: InputMedia,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        business_connection_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]: ...

    async def edit_message_reply_markup(
        self,
        chat_id: Optional[Union[int, str]] = None,
        message_id: Optional[int] = None,
        inline_message_id: Optional[str] = None,
        business_connection_id: Optional[str] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Union[Message, bool]: ...

    async def delete_message(
        self,
        chat_id: Union[int, str],
        message_id: int,
    ) -> bool: ...

    async def delete_messages(
        self,
        chat_id: Union[int, str],
        message_ids: List[int],
    ) -> bool: ...

    async def forward_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        video_start_timestamp: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
    ) -> Message: ...

    async def copy_message(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_id: int,
        message_thread_id: Optional[int] = None,
        video_start_timestamp: Optional[int] = None,
        caption: Optional[str] = None,
        parse_mode: Optional[str] = None,
        caption_entities: Optional[List[MessageEntity]] = None,
        show_caption_above_media: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[
            Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]
        ] = None,
    ) -> Message: ...

    async def copy_messages(
        self,
        chat_id: Union[int, str],
        from_chat_id: Union[int, str],
        message_ids: List[int],
        message_thread_id: Optional[int] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        remove_caption: Optional[bool] = None,
    ) -> List[Message]: ...

    async def create_invoice_link(
        self,
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        business_connection_id: Optional[str] = None,
        provider_token: Optional[str] = None,
        subscription_period: Optional[int] = None,
        max_star_count: Optional[int] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
    ) -> str: ...

    async def send_invoice(
        self,
        chat_id: Union[int, str],
        title: str,
        description: str,
        payload: str,
        currency: str,
        prices: List[LabeledPrice],
        business_connection_id: Optional[str] = None,
        message_thread_id: Optional[int] = None,
        provider_token: Optional[str] = None,
        max_star_count: Optional[int] = None,
        provider_data: Optional[str] = None,
        photo_url: Optional[str] = None,
        photo_size: Optional[int] = None,
        photo_width: Optional[int] = None,
        photo_height: Optional[int] = None,
        need_name: Optional[bool] = None,
        need_phone_number: Optional[bool] = None,
        need_email: Optional[bool] = None,
        need_shipping_address: Optional[bool] = None,
        send_phone_number_to_provider: Optional[bool] = None,
        send_email_to_provider: Optional[bool] = None,
        is_flexible: Optional[bool] = None,
        disable_notification: Optional[bool] = None,
        protect_content: Optional[bool] = None,
        allow_paid_broadcast: Optional[bool] = None,
        message_effect_id: Optional[str] = None,
        reply_parameters: Optional[Any] = None,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ) -> Message: ...

    async def answer_shipping_query(
        self,
        shipping_query_id: str,
        ok: bool,
        shipping_options: Optional[List[ShippingOption]] = None,
        error_message: Optional[str] = None,
    ) -> bool: ...

    async def answer_pre_checkout_query(
        self,
        pre_checkout_query_id: str,
        ok: bool,
        error_message: Optional[str] = None,
    ) -> bool: ...

    async def set_my_commands(
        self,
        commands: List[BotCommand],
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool: ...

    async def delete_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> bool: ...

    async def get_my_commands(
        self,
        scope: Optional[BotCommandScope] = None,
        language_code: Optional[str] = None,
    ) -> List[BotCommand]: ...

    async def set_my_default_administrator_rights(
        self,
        rights: Optional[ChatAdministratorRights] = None,
        for_channels: Optional[bool] = None,
    ) -> bool: ...

    async def get_my_default_administrator_rights(
        self, for_channels: Optional[bool] = None
    ) -> ChatAdministratorRights: ...

    async def set_chat_menu_button(
        self,
        chat_id: Optional[int] = None,
        menu_button: Optional[MenuButton] = None,
    ) -> bool: ...

    async def get_chat_menu_button(self, chat_id: Optional[int] = None) -> MenuButton: ...

    async def set_webhook(
        self,
        url: str,
        certificate: Optional[InputFile] = None,
        ip_address: Optional[str] = None,
        max_connections: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
        drop_pending_updates: Optional[bool] = None,
        secret_token: Optional[str] = None,
    ) -> bool: ...

    async def delete_webhook(self, drop_pending_updates: Optional[bool] = None) -> bool: ...

    async def get_webhook_info(self) -> WebhookInfo: ...

    async def get_updates(
        self,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        timeout: Optional[int] = None,
        allowed_updates: Optional[List[str]] = None,
    ) -> List[Update]: ...

    async def close(self) -> bool: ...

    # Properties
    @property
    def session(self) -> BaseSession: ...
    @property
    def token(self) -> str: ...

    # === Own methods ===
    def load(self, *paths: str) -> None: ...
    def run(self, logging_enabled: bool = True) -> None: ...
