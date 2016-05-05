from django.contrib import admin
from .models import MenuItem, Category

class MenuItemAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass


admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
