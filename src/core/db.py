import logging
from gino.ext.starlette import Gino

from src.core.config import DATABASE_URI

LOGGER = logging.getLogger(__name__)


try:
    # create Gino engine
    LOGGER.info(f"Initialise Gino engine and connecting to {DATABASE_URI}")
    db = Gino(dsn=DATABASE_URI)
except Exception as e:
    LOGGER.error(f"Error in Gino engine initialisation => {e}")