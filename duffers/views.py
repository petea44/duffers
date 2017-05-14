# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Golfer, Course, Score, Champs, HoleInOne
from django.template import loader
from django.db.models import Avg, Count, Sum
from duffers.models import GolferStats
from duffers.forms import NameForm

def index(request):
    template = loader.get_template('duffers/index.html')
    return HttpResponse(template.render())



def golfers(request):
    golfer_list =Golfer.objects.order_by('last_name','first_name')
    template = loader.get_template('duffers/golfers.html')
    context = {
        'golfer_list': golfer_list,
    }
    return HttpResponse(template.render(context, request))

def courses(request):
    course_list = Course.objects.order_by('course_name')     
    template = loader.get_template('duffers/course.html')
    context = {
        'course_list': course_list,
    }
    return HttpResponse(template.render(context, request))

def scores_by_golfer(request,my_golfer):
    score_list = Score.objects.filter(golfer_id=my_golfer).order_by('course','golfer','play_date')
    avg_list = GolferStats.objects.filter(golfer_id=my_golfer)
    template = loader.get_template('duffers/scores_by_golfer.html')
    context = {
        'score_list': score_list,
        'avg_list': avg_list,
    }
    return HttpResponse(template.render(context, request))

def scores_by_course(request,my_course):
    scores_list = Score.objects.filter(course_id=my_course).order_by('course','golfer','play_date')
    template = loader.get_template('duffers/scores_by_course.html')
    context = {
        'scores_list': scores_list,
    }
    return HttpResponse(template.render(context, request))
    
def champs(request):
    champs_list = Champs.objects.order_by('-year')  
    holes_list = HoleInOne.objects.order_by('play_date')      
    template = loader.get_template('duffers/champs.html')
    context = {
        'champs_list': champs_list,'holes_list': holes_list,
    }
    return HttpResponse(template.render(context, request))    
    
    

    
     
     
