from fastapi import FastAPI

from .api.chat import router as chat_router
from .api.routes.health import router as health_router
from .core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, version=settings.app_version)
    app.include_router(health_router, prefix="/api/v1")
    app.include_router(chat_router, prefix="/api/v1")
    return app


app = create_app()
