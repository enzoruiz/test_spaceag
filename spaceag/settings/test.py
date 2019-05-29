import os
from configurations import values
from .base import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Test(Base):
    SECRET_KEY = values.SecretValue()

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:'
        }
    }

    EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
