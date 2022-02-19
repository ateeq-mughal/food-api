from .models import *
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from .models import User

class RegistrationSerializer(RegisterSerializer):
    name = serializers.CharField(required = True)
    contactno = serializers.CharField(required = True)

    def save(self, request):
        user = super().save(request)
        contactno = self.validated_data.get("contactno","")
        user.contactno = contactno
        name = self.validated_data.get("name","")
        user.name = name
        user.save()
        return user   


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","name","email","contactno")

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

# class OrderSerializer2(serializers.Serializer):
#     food = serializers.IntegerField()
#     quantity = serializers.IntegerField()

class OrderSerializer(serializers.ModelSerializer):
    # food = OrderSerializer2(many = True)

    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('food',)

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.method in ['POST','UPDATE']:
            self.Meta.depth = 0
        else:
            self.Meta.depth = 2

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
