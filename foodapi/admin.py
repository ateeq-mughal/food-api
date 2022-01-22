from django.contrib import admin
from .models import Category, FoodItem, Area

# Register your models here.


admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Area)
