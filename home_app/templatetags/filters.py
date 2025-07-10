import datetime

from django import template

register = template.Library()


@register.filter()
def number_cuter(number):
    # Convert the number to a string
    number_str = str(number)

    # Check if the number is negative
    if number_str.startswith('-'):
        sign = '-'
        number_str = number_str[1:]
    else:
        sign = ''

    # Separate the digits into groups of three
    groups = []
    while number_str:
        groups.append(number_str[-3:])
        number_str = number_str[:-3]

    # Join the groups with commas and return the result
    return sign + ','.join(reversed(groups))


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
