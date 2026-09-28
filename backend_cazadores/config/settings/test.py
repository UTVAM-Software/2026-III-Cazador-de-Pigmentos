import secrets

from .base import *

DEBUG = False
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.test.sqlite3",
    }
}

LOGGING["loggers"]["django"]["level"] = "WARNING"

if not SECRET_KEY:
    SECRET_KEY = secrets.token_urlsafe(50)