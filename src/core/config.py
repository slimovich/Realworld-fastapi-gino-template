import os


##########################################################################
# DataBase settings
##########################################################################
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
DB_ADRESS = os.getenv("DB_ADRESS")
DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_ADRESS}/{DB_NAME}"

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
        "uvicorn.access": {"handlers": ["access"], "level": "INFO", "propagate": False},
    },
}
