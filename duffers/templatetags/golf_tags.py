from django import template
from duffers.models import Golfer, Score
from django.db.models import Avg, Count
register = template.Library()

@register.simple_tag
def cutit(value, arg):
    """Removes all values of arg from the given string"""
    return arg

@register.simple_tag
def the_version():
    return "2017.05.14"
@register.simple_tag
def score_color(ppar, cpar):
    """ set color for scores based on birdy, par, bogey """
    if ppar == 1:
        return "w3-yellow w3-round-xxlarge"
    if ppar == cpar-2:
       return "w3-orange w3-round-xxlarge"
    if ppar == cpar: 
        return "w3-green w3-round-large"
    if ppar<cpar:
        return "w3-red w3-round-large"
    if ppar == (cpar+1):
        return "w3-blue w3-round-large"
    return ""

@register.simple_tag
def my_golfer(golfer_id):
    golfguy = Golfer.objects.filter(id=golfer_id)
    for myguy in golfguy:
        thename = myguy.last_name
    return thename

@register.simple_tag
def crse_avg(my_golfer, my_course):
    myquery = Score.objects.filter(golfer_id=my_golfer, course_id=my_course).aggregate(avg=Avg('par'))
    #for key, value in myquery:
      # my_avg = value
    return  int(round(myquery['avg']))
        
    
     