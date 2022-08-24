from django import template

register = template.Library()

@register.filter(name='cut_new')
def cut_new(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')