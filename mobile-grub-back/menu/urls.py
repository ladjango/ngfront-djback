from django.conf.urls import url, include
from menu import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'menuitems', views.MenuItemViewSet)
router.register(r'categories', views.CategoryViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
