from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^enter_score/$', views.enter_score, name='enter_score'),
    url(r'^post_score/$', views.post_score, name='post_score'),
    url(r'^handicap/$', views.handicap, name='handicap'),
    url(r'^avg_to_par/$', views.avg_to_par, name='avg_to_par'),
    ]