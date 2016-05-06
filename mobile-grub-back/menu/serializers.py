from rest_framework import serializers
from menu.models import MenuItem, Category

class MenuItemSerializer(serializers.ModelSerializer):
    image = serializers.ReadOnlyField(source='image.url')
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'image')

class CategorySerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(source='menuitem_set.all', many=True)
    class Meta:
        model = Category
        fields = ('id', 'created', 'name', 'description', 'menu_items')
