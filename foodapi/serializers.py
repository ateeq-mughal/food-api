from .models import *

from rest_framework import serializers



class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
    

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Area
        fields = '__all__'

