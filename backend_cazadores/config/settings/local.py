import os

from .base import *

DEBUG = True
ALLOWED_HOSTS = os.getenv(
    "DJANGO_ALLOWED_HOSTS", "localhost,127.0.0.1"
).split(",")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.local.sqlite3",
    }
}

LOGGING["loggers"]["django"]["level"] = "DEBUG"

if not SECRET_KEY:
    raise RuntimeError("Define DJANGO_SECRET_KEY en el archivo .env")