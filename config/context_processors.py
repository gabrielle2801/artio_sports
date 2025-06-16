# context_processors.py
from django.conf import settings


def google_analytics(request):
    return {
        'GA_TRACKING_ID': settings.GA_TRACKING_ID
    }