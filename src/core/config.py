import os

import inject

##########################################################################
# DataBase settings
##########################################################################
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_ADRESS = os.getenv("POSTGRES_ADRESS")
DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_ADRESS}/{POSTGRES_DB}"

##########################################################################
# Server settings
##########################################################################

SERVER_ADRESS = "127.0.0.1"
SERVER_PORT = 8080
SERVER_LOG_LEVEL = "debug"
SERVER_WORKER_NUMBERS = 1

##########################################################################
# Log settings
##########################################################################

# replicate the dictConfig logging in uvicorn and update the existing formatter.
LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "()": "uvicorn.logging.DefaultFormatter",
            "fmt": "%(asctime)s - %(name)s - %(levelprefix)s %(message)s",
            "use_colors": None,
        },
        "access": {
            "()": "uvicorn.logging.AccessFormatter",
            "fmt": '%(asctime)s - %(name)s - %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
        },
    },
    "handlers": {
        "default": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stderr",
        },
        "access": {
            "formatter": "access",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {"handlers": ["default"], "level": "INFO"},
        "uvicorn.error": {"level": "INFO"},
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False,},
    },
}

##########################################################################
# Dependicies injection settings
##########################################################################


def configure_inject() -> None:
    from src.domain.userManagment.service.userService import UserService
    from src.infrastructure.database.models.user import UserQueries

    def config(binder: inject.Binder) -> None:
        binder.bind(UserService, UserService(UserQueries()))

    inject.configure(config)
