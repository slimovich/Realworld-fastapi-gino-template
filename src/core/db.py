import logging

from gino.ext.starlette import Gino

from src.core.config import DATABASE_URI

LOGGER = logging.getLogger(__name__)


# create Gino engine
LOGGER.info(f"Initialise Gino engine and connecting to {DATABASE_URI}")
db = Gino(dsn=DATABASE_URI)
