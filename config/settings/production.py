import os
from .base import *
# from config import env

DEBUG = False

STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT")
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT")

try:
    from .local import *
except ImportError:
    pass