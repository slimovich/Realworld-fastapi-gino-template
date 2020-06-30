import logging

import uvicorn
from fastapi import FastAPI

from src.api.api import api_router
from src.core.config import (
    LOGGING_CONFIG,
    SERVER_ADRESS,
    SERVER_LOG_LEVEL,
    SERVER_PORT,
)
from src.core.db import db

LOGGER = logging.getLogger(__name__)


def create_app() -> FastAPI:
    try:
        LOGGER.info("Initiliase fast-API app")
        app = FastAPI()
        db.init_app(app=app)
        app.include_router(api_router, prefix="/api/v1")
    except Exception as e:
        LOGGER.error(f"Error in fast-API app initialisation => {e}")
    return app


app: FastAPI = create_app()


@app.on_event("startup")
async def _startup() -> None:
    try:
        LOGGER.info("Create tables")
        # await db.gino.drop_all()
        await db.gino.create_all()
    except Exception as e:
        LOGGER.error(f"Error in startup for tables creation => {e}")


def run() -> None:

    # os.system("uvicorn src.core.server:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 8080 --log-level debug")
    uvicorn.run(
        app,
        host=SERVER_ADRESS,
        port=SERVER_PORT,
        log_level=SERVER_LOG_LEVEL,
        log_config=LOGGING_CONFIG,
    )
