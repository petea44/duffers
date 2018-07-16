from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^courses/$', views.courses, name='courses'),
    url(r'^golfers/$', views.golfers, name='golfers'),
    url(r'^champs/$', views.champs, name='champs'),
    url(r'^(?P<my_golfer>[0-9]+)/scores_by_golfer/$',views.scores_by_golfer, name='scores_by_golfer'),
    url(r'^(?P<my_course>[0-9]+)/scores_by_course/$',views.scores_by_course, name='scores_by_course'),
    url(r'^(?P<my_golfer>[0-9]+)/hcap_by_golfer/$',views.hcap_by_golfer, name='hcap_by_golfer'),
    ]
