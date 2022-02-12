from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Area(models.Model):
    name = models.CharField(max_length=255)
    delivery_charges = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static', null=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    unit = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    section_id = models.IntegerField()
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static')

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    food = models.ForeignKey(FoodItem, null=True, on_delete=models.SET_NULL)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=7, decimal_places=2)


class Order(models.Model):
    area = models.ForeignKey(Area, null=True, on_delete=models.SET_NULL)
    order_item = models.ManyToManyField(OrderItem, related_name='order')
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField()
