from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(User)
admin.site.register(Category)
admin.site.register(FoodItem)
admin.site.register(Area)
admin.site.register(OrderItem)
admin.site.register(Order)
