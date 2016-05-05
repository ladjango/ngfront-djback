from rest_framework import serializers
from menu.models import MenuItem, Category

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'name', 'description', 'image')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'created', 'name', 'description')
