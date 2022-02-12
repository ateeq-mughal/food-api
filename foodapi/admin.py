from django.contrib import admin
from .models import Category, FoodItem, Area, OrderItem, Order

# Register your models here.


admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Area)
admin.site.register(OrderItem)
admin.site.register(Order)
