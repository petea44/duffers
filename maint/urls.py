from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^enter_score/$', views.enter_score, name='enter_score'),
    url(r'^post_score/$', views.post_score, name='post_score'),
    url(r'^handicap/$', views.handicap, name='handicap'),
    url(r'^avg_to_par/$', views.avg_to_par, name='avg_to_par'), 
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/duffers'}, name='logout'),
    ]