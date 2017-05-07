# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



class Golfer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100, null=True)
    handicap = models.IntegerField(default=0)
    def __str__(self):
        return format(self.first_name + " " + self.last_name)
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    address = models.CharField(max_length=250)
    website =  models.CharField(max_length=150)
    email =  models.CharField(max_length=150)
    phone =  models.CharField(max_length=15)
    par = models.IntegerField(default=72)
    yards = models.IntegerField(blank=True, null=True)
    slope = models.IntegerField(blank=True, null=True)
    par1 = models.IntegerField(default=4)
    par2 = models.IntegerField(default=4)
    par3 = models.IntegerField(default=4)
    par4 = models.IntegerField(default=4)
    par5 = models.IntegerField(default=4)
    par6 = models.IntegerField(default=4)
    par7 = models.IntegerField(default=4)
    par8 = models.IntegerField(default=4)
    par9 = models.IntegerField(default=4)
    par10 = models.IntegerField(default=4)
    par11 = models.IntegerField(default=4)
    par12 = models.IntegerField(default=4)
    par13 = models.IntegerField(default=4)
    par14 = models.IntegerField(default=4)
    par15 = models.IntegerField(default=4)
    par16 = models.IntegerField(default=4)
    par17 = models.IntegerField(default=4)
    par18 = models.IntegerField(default=4)
    par_out = models.IntegerField(default=36)
    par_in = models.IntegerField(default=36)
    yards1 = models.IntegerField(blank=True, null=True)
    yards2 = models.IntegerField(blank=True, null=True)
    yards3 = models.IntegerField(blank=True, null=True)
    yards4 = models.IntegerField(blank=True, null=True)
    yards5 = models.IntegerField(blank=True, null=True)
    yards6 = models.IntegerField(blank=True, null=True)
    yards7 = models.IntegerField(blank=True, null=True)
    yards8 = models.IntegerField(blank=True, null=True)
    yards9 = models.IntegerField(blank=True, null=True)
    yards10 = models.IntegerField(blank=True, null=True)
    yards11 = models.IntegerField(blank=True, null=True)
    yards12 = models.IntegerField(blank=True, null=True)
    yards13 = models.IntegerField(blank=True, null=True)
    yards14 = models.IntegerField(blank=True, null=True)
    yards15 = models.IntegerField(blank=True, null=True)
    yards16 = models.IntegerField(blank=True, null=True)
    yards17 = models.IntegerField(blank=True, null=True)
    yards18 = models.IntegerField(blank=True, null=True)
    yards_out = models.IntegerField(blank=True, null=True)
    yards_in = models.IntegerField(blank=True, null=True)

#     def par_in(self):
#         par_in= self.par10 + self.par11 + self.par12 + self.par13 + self.par14 + self.par15 +self.par16 + self.par17 + self.par18
#         return par_in
#     def par_out(self):
#         par_out= self.par9 + self.par1 + self.par2 + self.par3 + self.par4 + self.par5 +self.par6 + self.par7 + self.par8
#         return par_out
#     def par(self):
#         par= self.par9 + self.par1 + self.par2 + self.par3 + self.par4 + self.par5 +self.par6 + self.par7 + self.par8  + self.par10 + self.par11 + self.par12 + self.par13 + self.par14 + self.par15 +self.par16 + self.par17 + self.par18
#         return par
#     def yards_in(self):
#         yards_in= self.yards10 + self.yards11 + self.yards12 + self.yards13 + self.yards14 + self.yards15 +self.yards16 + self.yards17 + self.yards18
#         return yards_in
#     def yards_out(self):
#         yards_out= self.yards9 + self.yards1 + self.yards2 + self.yards3 + self.yards4 + self.yards5 +self.yards6 + self.yards7 + self.yards8
#         return yards_out
#     def yards(self):
#         yards= self.yards9 + self.yards1 + self.yards2 + self.yards3 + self.yards4 + self.yards5 +self.yards6 + self.yards7 + self.yards8  + self.yards10 + self.yards11 + self.yards12 + self.yards13 + self.yards14 + self.yards15 +self.yards16 + self.yards17 + self.yards18
#         return yards
    def __str__(self):
        return format(self.course_name)
    class Meta:
        ordering = ['course_name']

class Score(models.Model):
    golfer = models.ForeignKey(Golfer)
    course = models.ForeignKey(Course)
    par1 = models.IntegerField(default=4)
    par2 = models.IntegerField(default=4)
    par3 = models.IntegerField(default=4)
    par4 = models.IntegerField(default=4)
    par5 = models.IntegerField(default=4)
    par6 = models.IntegerField(default=4)
    par7 = models.IntegerField(default=4)
    par8 = models.IntegerField(default=4)
    par9 = models.IntegerField(default=4)
    par10 = models.IntegerField(default=4)
    par11 = models.IntegerField(default=4)
    par12 = models.IntegerField(default=4)
    par13 = models.IntegerField(default=4)
    par14 = models.IntegerField(default=4)
    par15 = models.IntegerField(default=4)
    par16 = models.IntegerField(default=4)
    par17 = models.IntegerField(default=4)
    par18 = models.IntegerField(default=4)
    par_out = models.IntegerField(default=0)
    par_in = models.IntegerField(default=0)
    par = models.IntegerField(default=0)
    play_date = models.DateField('date published')
    hcap = models.CharField(max_length=1, default="N")
#      
#     def par_in(self):
#         par_in= self.par10 + self.par11 + self.par12 + self.par13 + self.par14 + self.par15 +self.par16 + self.par17 + self.par18
#         return par_in
#     def par_out(self):
#         par_out= self.par9 + self.par1 + self.par2 + self.par3 + self.par4 + self.par5 +self.par6 + self.par7 + self.par8
#         return par_out
#     def par(self):
#         par= self.par9 + self.par1 + self.par2 + self.par3 + self.par4 + self.par5 +self.par6 + self.par7 + self.par8  + self.par10 + self.par11 + self.par12 + self.par13 + self.par14 + self.par15 +self.par16 + self.par17 + self.par18
#         return par
   
    def __str__(self):
        return format(self.course.course_name + ": " + self.golfer.first_name + " " + self.golfer.last_name + " " + self.play_date.strftime('%m/%d/%Y'))

class Champs(models.Model):
    golfer = models.ForeignKey(Golfer)
    year   = models.CharField (max_length=5)
    
    def __str__(self):
        return format(self.golfer.last_name + " : " +   self.year)
    class Meta:
        ordering = ['year']
    

class HoleInOne(models.Model):
    golfer = models.ForeignKey(Golfer)
    course = models.ForeignKey(Course)
    hole   = models.IntegerField(blank=True, null=True)
    yards  = models.IntegerField(blank=True, null=True)
    club   = models.CharField(max_length=20, null=True)
    play_date = models.DateField('date published', null=True)
    
    def __str__(self):
        return format(self.golfer.first_name + " " + self.golfer.last_name)

class GolferStats(models.Model):
    golfer = models.ForeignKey(Golfer)
    par3_avg = models.FloatField(default=0)
    par4_avg = models.FloatField(default=0)
    par5_avg = models.FloatField(default=0)
