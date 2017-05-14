from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^maint/', include('maint.urls', namespace="maint")),
    url(r'^duffers/', include('duffers.urls', namespace="duffers")),
    url(r'^admin/', admin.site.urls),
]
