from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    ######################### Application Config ########################################
    DEBUG = bool(int(environ.get("CONFIG_DEBUG", "0")))
    ENV = environ.get("CONFIG_ENV", "production")
    ######################### mongo Application Config ##################################
    USER_NAME = environ.get('CONFIG_USER_NAME', None)
    PASSWORD = environ.get('CONFIG_PASSWORD', None)
    TABLE_NAME = environ.get('CONFIG_TABLE_NAME', 'test_table')
    HOST = environ.get('CONFIG_HOST', 'localhost')
    PORT = int(environ.get('CONFIG_PORT', 27017))
    ######################### APM Config ################################################
    APM_SERVICE_NAME = environ.get('CONFIG_APM_SERVICE_NAME', None)
    APM_SERVER_URL = environ.get('CONFIG_APM_SERVER_URL', None)
