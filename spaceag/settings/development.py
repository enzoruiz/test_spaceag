import os
from configurations import values
from .base import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Development(Base):
    DEBUG = values.BooleanValue(True)

    SECRET_KEY = values.SecretValue()

    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    DATABASE_HOST = os.environ.get('DATABASE_HOST')
    POSTGRES_DB = os.environ.get('POSTGRES_DB')

    DATABASE_URL = 'postgis://%s:%s@%s/%s' % (
        POSTGRES_USER, POSTGRES_PASSWORD, DATABASE_HOST, POSTGRES_DB
    )
    DATABASES = values.DatabaseURLValue(DATABASE_URL)

    ALLOWED_HOSTS = ['*']
