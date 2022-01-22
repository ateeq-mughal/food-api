from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static')

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


class Area(models.Model):
    name = models.CharField(max_length=255)
    delivery_charges = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.name