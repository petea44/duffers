# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from .models import Golfer, Course, Score, Champs, HoleInOne
from django.template import loader
from django.db.models import Avg, Count, Sum
from duffers.models import GolferStats

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
    
    
def handicap(request):
    golfer_list =Golfer.objects.order_by('last_name','first_name')
    template = loader.get_template('duffers/golfers.html')
    for golfers in golfer_list:
        scores_list = Score.objects.filter(golfer_id=golfers.id,hcap="Y")
        differential = 0
        score_count = 0
        for scores in scores_list:
            score_count = score_count+1
            differential= differential + scores.par - scores.course.par
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

def avg_to_par(request):
    golfer_list = Golfer.objects.order_by('last_name', 'first_name')
    template = loader.get_template('duffers/avg.html')
    for  golfers in golfer_list:
        the_par = 2
        while the_par < 5:
            the_par = the_par + 1
            hole_cnt = 0
            stroke_sum = 0
            course_list = Course.objects.all()
            for courses in course_list:
                if courses.par1 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par1'), cnt=Count('par1'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par2 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par2'), cnt=Count('par2'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par3 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par3'), cnt=Count('par3'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par4 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par4'), cnt=Count('par4'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par5 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par5'), cnt=Count('par5'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par6 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par6'), cnt=Count('par6'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par7 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par7'), cnt=Count('par7'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par8 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par8'), cnt=Count('par8'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par9 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par9'), cnt=Count('par9'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par10 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par10'), cnt=Count('par10'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par11 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par11'), cnt=Count('par11'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par12 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par12'), cnt=Count('par12'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par13 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par13'), cnt=Count('par13'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par14 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par14'), cnt=Count('par14'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par15 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par15'), cnt=Count('par15'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par16 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par16'), cnt=Count('par16'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par17 == the_par:
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par17'), cnt=Count('par17'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
                if courses.par18 == the_par: 
                    my_hole = Score.objects.filter(golfer_id=golfers.id, course_id=courses.id).aggregate(sum=Sum('par18'), cnt=Count('par18'))
                    if my_hole['cnt'] > 0:
                        hole_cnt = hole_cnt + my_hole['cnt']
                        stroke_sum = stroke_sum + my_hole['sum']
            if the_par == 3:par3_value = float(stroke_sum) / float(hole_cnt)
            if the_par == 4:par4_value = float(stroke_sum) / float(hole_cnt)   
            if the_par == 5:par5_value = float(stroke_sum) / float(hole_cnt)   
        GolferStats.objects.all().filter(golfer_id=golfers.id).delete()
        GolferStats.objects.create(golfer_id=golfers.id, par3_avg=par3_value, par4_avg=par4_value, par5_avg=par5_value)
           
    context = {
        'hole_cnt': hole_cnt,
        'stroke_sum': stroke_sum,
    }    
    return HttpResponse(template.render(context, request))           
        
def avg_test(request):     
    avg_list = Score.objects.values('course').filter(golfer_id=21).annotate(Avg('par')) 
    template = loader.get_template('duffers/avg.html') 
    context = {
        'avg_list': avg_list,
    }
    return HttpResponse(template.render(context, request))
    
     
     
