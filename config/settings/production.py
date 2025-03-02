import os
from .base import *
from .base import env
# from config import env

DEBUG = False
SECRET_KEY = env("SECRET_KEY")
# Security configuration

# Ensure that the session cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#session-cookie-secure
SESSION_COOKIE_SECURE = True

# Ensure that the CSRF cookie is only sent by browsers under an HTTPS connection.
# https://docs.djangoproject.com/en/stable/ref/settings/#csrf-cookie-secure
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

STATIC_ROOT = env("DJANGO_STATIC_ROOT")
MEDIA_ROOT = env("DJANGO_MEDIA_ROOT")
<<<<<<< HEAD

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
=======
RECAPTCHA_SITE_KEY = env("RECAPTCHA_SITE_KEY")
RECAPTCHA_SECRET_KEY = env("RECAPTCHA_SECRET_KEY")

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]
# =================
# Stripe settings
# =================
STRIPE_COMPRESS_TO_ONE_LINE_ITEM = False
STRIPE_USE_PRICES_API = True

# Override these three.  I suggest creating a file called "settings_local.py", and adding the settings there.
# This file is .gitignore-d so this will avoid your stripe keys going into git.
STRIPE_PUBLISHABLE_KEY = env("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_RETURN_URL_BASE = 'https://artio-sports.com'

# If you don't want to use a settings_local.py, comment or remove this line.
# from settings_local import *

STRIPE_PAYMENT_SUCCESS_URL = "{0}{1}".format(
    STRIPE_RETURN_URL_BASE, "/boutique/checkout/preview-stripe/{0}/")
STRIPE_PAYMENT_CANCEL_URL = "{0}{1}".format(
    STRIPE_RETURN_URL_BASE, "/boutique/checkout/stripe-payment-cancel/{0}/")
>>>>>>> 3a2d8aa8c1b0f4975ce54c17064465ab66e104bd

try:
    from .local import *
except ImportError:
    pass