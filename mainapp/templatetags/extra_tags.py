from textwrap import wrap

from django import template

register = template.Library()

@register.filter(name='pprice')
def pretty_price(value):
    """ Разбивка отображения цен по 3 символа: 12 345,00"""
    s = str(value)
    tmp = s[:-3]
    tmp = ' '.join(wrap(tmp[::-1], 3))[::-1]

    return tmp + ',' + s[-2:]
