from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^duffers/', include('duffers.urls')),
    url(r'^admin/', admin.site.urls),
]
