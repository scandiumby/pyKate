from functools import cached_property

from .base import AuthBackendInterface, AuthFrontendInterface, AuthBackendInterfaceType


class TelegramPhoneAuthBackend(AuthBackendInterface):
    """
    The class provide authorization(getting a JWT token) by code verification in telegram bot.
    User should provide phone number in admin login page and in telegram bot.
    In result user will get a code by the bot that can be applied in admin login page for finish authorization process.
    """

    async def authenticate(self, *args, **kwargs):
        ...


class TelegramPhoneAuthFrontend(AuthFrontendInterface):
    @cached_property
    def backend(self) -> AuthBackendInterfaceType:
        return TelegramPhoneAuthBackend()

    @property
    def backend_slug(self) -> str:
        return "tg-phone"

    @property
    def title(self) -> str:
        return "Telegram authorization using a phone"

    @property
    def desc(self) -> str:
        return "Authorization by specifying the phone number linked to your Telegram account " \
               "and confirming it through a Telegram bot."


class TelegramNativeAuthBackend(AuthBackendInterface):
    """
    The class provide authorization(getting a JWT token) by Telegram native authorization widget.
    """

    async def authenticate(self, *args, **kwargs):
        ...


class TelegramNativeAuthFrontend(AuthFrontendInterface):
    @cached_property
    def backend(self) -> AuthBackendInterfaceType:
        return TelegramNativeAuthBackend()

    @property
    def backend_slug(self) -> str:
        return "tg-native"

    @property
    def title(self) -> str:
        return "Authorization built into Telegram"

    @property
    def desc(self) -> str:
        return "Authorization by Telegram native authorization widget."
