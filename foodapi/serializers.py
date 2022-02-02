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


class OrderItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = OrderItem
        fields = '__all__'

# class OrderSerializer2(serializers.Serializer):
#     food = serializers.IntegerField()
#     quantity = serializers.IntegerField()

class OrderSerializer(serializers.ModelSerializer):
    # food = OrderSerializer2(many = True)

    class Meta:
        model = Order
        fields = '__all__'
        # read_only_fields = ('food',)

    # def create(self, validated_data):
    #     print(validated_data)
    #     # food = validated_data.pop("order_item")
    #     # x = OrderItemSerializer(data=food , many=True)
    #     # if not x.is_valid():
    #     #     print(x)
    #     #     print(x.errors)
    #     # order = OrderItem.objects.bulk_create(food)
    #     # print(order)
    #     return super().create(validated_data)