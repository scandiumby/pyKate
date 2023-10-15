from typing import List

from fastapi import APIRouter

from pykate.auth.backends.models import AuthFrontendContext
from pykate.configs import config
from pykate.core.class_loader import load_class

backend_router = APIRouter(
    tags=["auth_backends"],
)


@backend_router.get("/", response_model=List[AuthFrontendContext])
async def read_backends():
    return [load_class(backend)().fronted_context for backend in config.AUTH_BACKENDS]
