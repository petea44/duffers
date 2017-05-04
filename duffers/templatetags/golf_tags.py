from django import template

register = template.Library()

@register.simple_tag
def cutit(value, arg):
    """Removes all values of arg from the given string"""
    return arg

@register.simple_tag
def score_color(ppar, cpar):
    """ set color for scores based on birdy, par, bogey """
    if ppar == cpar: 
        return "w3-green"
    if ppar<cpar:
        return "w3-red"
    if ppar == (cpar+1):
        return "w3-blue"
    return "black"