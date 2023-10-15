from pydantic.dataclasses import dataclass


@dataclass
class AuthFrontendContext:
    backend_root_url: str
    desc: str
    title: str
