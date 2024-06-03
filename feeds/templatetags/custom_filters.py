# myapp/templatetags/custom_filters.py

from django import template
from datetime import datetime

register = template.Library()

# Dictionaries for French translation
DAYS_FR = {
    'Monday': 'Lundi',
    'Tuesday': 'Mardi',
    'Wednesday': 'Mercredi',
    'Thursday': 'Jeudi',
    'Friday': 'Vendredi',
    'Saturday': 'Samedi',
    'Sunday': 'Dimanche'
}

MONTHS_FR = {
    'January': 'Janvier',
    'February': 'Février',
    'March': 'Mars',
    'April': 'Avril',
    'May': 'Mai',
    'June': 'Juin',
    'July': 'Juillet',
    'August': 'Août',
    'September': 'Septembre',
    'October': 'Octobre',
    'November': 'Novembre',
    'December': 'Décembre'
}


@register.filter
def format_datetime(value):
    if value is None:
        return ""
    try:
        # Convert the string to a datetime object
        dt = datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')
    except ValueError:
        try:
            dt = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S%z')
        except ValueError:
            dt = datetime.strptime(value, '%a, %d %b %Y %H:%M:%S %z')

    # Translate the day and month to French
    day_name = DAYS_FR[dt.strftime('%A')]
    month_name = MONTHS_FR[dt.strftime('%B')]

    # Format the datetime object using strftime
    return dt.strftime(f'{day_name} %d {month_name} %Y à %H:%M')
