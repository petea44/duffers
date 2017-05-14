# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from duffers.models import Course, Golfer, Score, GolferStats
from django.template import loader
from django.contrib.contenttypes.views import shortcut
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Avg, Count, Sum

from maint.forms import HolesForm, ScoreForm
# from duffers.views import avg_to_par
# Create your views here.
def enter_score(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    form1 = ScoreForm()
    form2 = HolesForm()
    template = loader.get_template('maint/enterScores.html')
    context = {
        'form1' : form1,
        'form2' : form2,
    }
    return HttpResponse(template.render(context, request))

def post_score(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    Score.objects.create(golfer_id=request.POST['golfer'],
                         course_id=request.POST['course'],
                         play_date=request.POST['play_date'],
                         hcap=request.POST['hcap'],
                         par1=request.POST['par1'],
                         par2=request.POST['par2'],
                         par3=request.POST['par3'],
                         par4=request.POST['par4'],
                         par5=request.POST['par5'],
                         par6=request.POST['par6'],
                         par7=request.POST['par7'],
                         par8=request.POST['par8'],
                         par9=request.POST['par9'],
                         par10=request.POST['par10'],
                         par11=request.POST['par11'],
                         par12=request.POST['par12'],
                         par13=request.POST['par13'],
                         par14=request.POST['par14'],
                         par15=request.POST['par15'],
                         par16=request.POST['par16'],
                         par17=request.POST['par17'],
                         par18=request.POST['par18'],
                         par_in=request.POST['par_in'],
                         par_out=request.POST['par_out'],
                         par=request.POST['par']
                         )
    if request.POST['hcap'] == "Y":
        scores_list = Score.objects.filter(golfer_id=request.POST['golfer'],hcap="Y")
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
        Golfer.objects.filter(id=request.POST['golfer']).update(handicap=myhcap) 
    form1 = ScoreForm()
    form2 = HolesForm()
    template = loader.get_template('maint/enterScores.html')
    context = {
        'form1' : form1,
        'form2' : form2,
        'mymesg' : 'score entered',
    }  
    return HttpResponse(template.render(context, request))


def handicap(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
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
    golfer_list =Golfer.objects.order_by('last_name','first_name')
    context = {
        'golfer_list': golfer_list,
    }          
    return HttpResponse(template.render(context, request)) 


def avg_to_par(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    golfer_list = Golfer.objects.order_by('last_name', 'first_name')
    template = loader.get_template('duffers/golfers.html')
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
        'golfer_list': golfer_list,
        'stroke_sum': stroke_sum,
    }    
    return HttpResponse(template.render(context, request))  