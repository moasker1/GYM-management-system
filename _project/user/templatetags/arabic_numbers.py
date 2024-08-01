from django import template
from datetime import timedelta

register = template.Library()

@register.filter
def add_days(value, days):
    return value + timedelta(days=days)

@register.filter
def custom_date(value):
    try:
        return value.strftime("%Y-%m-%d").replace('-0', '-')
    except (ValueError, AttributeError):
        return value