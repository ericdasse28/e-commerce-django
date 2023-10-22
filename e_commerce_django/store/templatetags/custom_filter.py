from django import template

register = template.Library()


@register.filter(name="currency")
def currency(number):
    return f"{number} €"


@register.filter(name="multiply")
def multiply(number, other_number):
    return number * other_number
