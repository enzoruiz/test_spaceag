import os
from configurations import values
from .base import Base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Development(Base):
    DEBUG = values.BooleanValue(True)

    SECRET_KEY = values.SecretValue()

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': '',
            'HOST': 'db',
            'PORT': '5432',
        }
    }

    ALLOWED_HOSTS = ['*']
