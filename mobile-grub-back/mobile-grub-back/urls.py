from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url, patterns
from django.contrib import admin


urlpatterns = [
    url(r'^', include('menu.urls')),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += static('/uploads/', document_root='uploads/')
