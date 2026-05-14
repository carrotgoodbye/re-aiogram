from aiogram import Bot as _Bot, Dispatcher as _Dispatcher
import asyncio
import logging
import signal
import sys
import importlib


class Bot:
    def __init__(self, token: str = None):
        if not token:
            raise ValueError("Token is required")

        self._bot = _Bot(token=token)
        self._dp = _Dispatcher()

        # middlewares
        from .mediagroup import AlbumMiddleware

        self._dp.message.middleware(AlbumMiddleware())

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
                raise ValueError(
                    f"There is no 'router' variable in the {path} module"
                )

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
        except KeyboardInterrupt:
            logging.info("Bot stopped by user")
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
                # Windows doesn't support add_signal_handler for all signals
                break

        try:
            await self._dp.start_polling(self._bot)
        finally:
            await self._shutdown()

    def _request_shutdown(self):
        """Signal handler: initiate graceful stop."""
        logging.info("Shutdown signal received, stopping polling...")
        asyncio.create_task(self._dp.stop_polling())

    async def _shutdown(self):
        """Close sessions and clean up resources."""
        logging.info("Closing bot session...")
        await self._bot.session.close()

        loop = asyncio.get_running_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            try:
                loop.remove_signal_handler(sig)
            except (NotImplementedError, ValueError):
                pass

        logging.info("Shutdown complete")