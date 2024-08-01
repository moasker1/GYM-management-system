from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_days(value, days):
    return value + timedelta(days=days)

@register.filter
def custom_date(value, date_format):
    if value:
        return value.strftime(date_format).replace('/0', '/').lstrip("0")
    return ""