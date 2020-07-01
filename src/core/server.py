import logging

import uvicorn
from fastapi import FastAPI

from src.api.api import api_router
from src.core.config import (
    DB_NAME,
    LOGGING_CONFIG,
    SERVER_ADRESS,
    SERVER_LOG_LEVEL,
    SERVER_PORT,
)
from src.core.db import db
from src.utils.sql import existing_database

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
    LOGGER.info("Check existing database")
    database: bool = await existing_database(db, DB_NAME)

    if not database:
        LOGGER.error(f"please create the required database before running the server db_name = {DB_NAME}")
    else:
        LOGGER.info("database checked")


def run() -> None:

    # os.system("uvicorn src.core.server:app --reload --lifespan on --workers 1 --host 0.0.0.0 --port 8080 --log-level debug")
    uvicorn.run(
        app,
        host=SERVER_ADRESS,
        port=SERVER_PORT,
        log_level=SERVER_LOG_LEVEL,
        log_config=LOGGING_CONFIG,
    )
