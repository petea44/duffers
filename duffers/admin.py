from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Golfer, Score, Course, Champs, HoleInOne, GolferStats

admin.site.register(Golfer)
admin.site.register(GolferStats)
admin.site.register(Course)
admin.site.register(Score)
admin.site.register(Champs)
admin.site.register(HoleInOne)
