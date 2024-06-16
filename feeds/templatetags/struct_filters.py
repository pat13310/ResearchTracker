from django import template
from datetime import datetime
import time
import pytz

register = template.Library()


@register.filter
def to_datetime(value):
    if isinstance(value, (time.struct_time, tuple)):
        dt = datetime(*value[:6])
        # Convertir à votre fuseau horaire local
        local_tz = pytz.timezone('Europe/Paris')  # Remplacez par votre fuseau horaire local
        dt = pytz.utc.localize(dt).astimezone(local_tz)
        return dt
    return value
