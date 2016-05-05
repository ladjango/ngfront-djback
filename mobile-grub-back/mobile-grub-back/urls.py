
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^', include('menu.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


