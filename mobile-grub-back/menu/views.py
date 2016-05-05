from menu.models import MenuItem, Category
from menu.serializers import MenuItemSerializer, CategorySerializer
from rest_framework import viewsets

class MenuItemViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides 'list', 'create', 'retrieve',
    'update', and 'destroy' actions.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
