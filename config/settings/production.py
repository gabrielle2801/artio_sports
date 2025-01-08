from .base import *
from config import env

DEBUG = False

STATIC_ROOT = env("DJANGO_STATIC_ROOT")
MEDIA_ROOT = env("DJANGO_MEDIA_ROOT")

try:
    from .local import *
except ImportError:
    pass
