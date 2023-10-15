from abc import abstractmethod
from functools import cached_property
from typing import Type, TypeVar

from pykate.configs import config


class AuthBackendInterface:

    @abstractmethod
    async def authenticate(self, *args, **kwargs):
        ...

    # @property
    # @abstractmethod
    # def pipelines(self) -> List[Callable]:
    #     ...
    #
    # def run_pipelines(self, *args, **kwargs):
    #     ...


AuthBackendInterfaceType = TypeVar("AuthBackendInterfaceType", bound=AuthBackendInterface)


class AuthFrontendInterface:
    auth_root = config.AUTH_BACKENDS_ROOT

    @property
    @abstractmethod
    def backend(self) -> Type[AuthBackendInterface]:
        ...

    @property
    @abstractmethod
    def backend_slug(self) -> str:
        ...

    @property
    @abstractmethod
    def title(self) -> str:
        ...

    @property
    @abstractmethod
    def desc(self) -> str:
        ...

    @cached_property
    def fronted_context(self):
        return {
            "title": self.title,
            "desc": self.desc,
            "backend_root_url": self.backend_root_url,
        }

    @cached_property
    def backend_root_url(self) -> str:
        return f"{self.auth_root}/{self.backend_slug}"


AuthFrontendInterfaceType = TypeVar("AuthFrontendInterfaceType", bound=AuthBackendInterface)
