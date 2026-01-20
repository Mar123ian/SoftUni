from django import template

register = template.Library()
@register.filter('capitalize_title')
def capitalize_title(value):
    return value.upper()



