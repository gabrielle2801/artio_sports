import datetime
from django import template
from django.utils import timezone
from django.utils.formats import date_format

register = template.Library()

@register.simple_tag
def next_sunday():
    today = timezone.now().astimezone().date()  # Remplace localtime() par astimezone()
    days_ahead = 6 - today.weekday()  # dimanche = 6
    if days_ahead <= 0:
        days_ahead += 7
    sunday = today + datetime.timedelta(days=days_ahead)
    # On reformate la date (sans fuseau) proprement
    return date_format(sunday, format="l d F Y", use_l10n=True)
