from django import template

register = template.Library()

@register.filter(name='pprice')
def pretty_price(value):
    """Разбивка отображения цен по 3 символа: 12 345,00"""
    return f'{value:,}'.replace(',', ' ').replace('.', ',')
