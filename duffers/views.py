# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Golfer, Course, Score, Champs, HoleInOne
from django.template import loader
from django.db.models import Avg, Count

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
    avg_score = Score.objects.filter(golfer_id=my_golfer).aggregate(Avg('par'))
    template = loader.get_template('duffers/scores_by_golfer.html')
    context = {
        'score_list': score_list,
        'avg_score':avg_score,
    }
    return HttpResponse(template.render(context, request))

def scores_by_course(request,my_course):
    scores_list = Score.objects.filter(course_id=my_course).order_by('course','golfer','play_date')
    avg_score = Score.objects.filter(course_id=my_course).aggregate(Avg('par'))
    template = loader.get_template('duffers/scores_by_course.html')
    context = {
        'scores_list': scores_list,
        'avg_score':avg_score,
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
    
    
def hcap(request):
    golfer_list =Golfer.objects.order_by('last_name','first_name')
    template = loader.get_template('duffers/golfers.html')
    for golfers in golfer_list:
      scores_list = Score.objects.filter(golfer_id=golfers.id,hcap="Y")
      differential = 0
      score_count = 0
      for scores in scores_list:
        score_count = score_count+1
        differential= differential + scores.par - scores.course.par
 #    score_count = score_count+1
      if score_count>0:
        myhcap=differential/score_count*.96
      else: myhcap=0 
      if myhcap>36:myhcap=36
      if score_count==0: myhcap=0 
      Golfer.objects.filter(id=golfers.id).update(handicap=myhcap) 
    context = {
        'golfer_list': golfer_list,
    }          
    return HttpResponse(template.render(context, request)) 
     
     
