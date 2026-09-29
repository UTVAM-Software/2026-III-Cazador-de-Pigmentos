import os

from .base import *

DEBUG = False
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

if not ALLOWED_HOSTS:
    raise RuntimeError("Define DJANGO_ALLOWED_HOSTS en producción")

DATABASES = {
    "default": {
        "ENGINE": os.environ["DB_ENGINE"],
        "NAME": os.environ["DB_NAME"],
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", ""),
        "PORT": os.environ.get("DB_PORT", ""),
        "CONN_MAX_AGE": 60,
    }
}

CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
    if origin.strip()
]

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
LOGGING["loggers"]["django"]["level"] = "INFO"