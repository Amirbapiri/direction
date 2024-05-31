from .base import *
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="django-insecure-9_ma23*x$b5pupj9uud_#)uui!o+z1gst3v(t*ory)jzf1=mzl",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = ["http://localhost:8080", "http://0.0.0.0:8080"]

CORS_ALLOW_ALL_ORIGINS = True

ALLOWED_HOSTS = ["0.0.0.0", "localhost"]
