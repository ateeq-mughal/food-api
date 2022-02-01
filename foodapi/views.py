from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

# Create your views here.

class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    

class FoodItemView(ModelViewSet):
    
    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]


class AreaView(ModelViewSet):
    
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class OrderItemView(ModelViewSet):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer


class OrderView(ModelViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]

class CreateOrderView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self,request):
        user = self.request.user
        area = self.request.data.get("area"," ")
        order_items = request.data.pop("order_item")
        order_item_keys = []
        price = 0
        for order_item in order_items:
            food = FoodItem.objects.filter(id = order_item["food"]).first()
            print(food.price)
            price += int(food.price) * int(order_item["quantity"])
            order_obj = OrderItem.objects.create(food = food, quantity= order_item["quantity"])
            order_item_keys.append(order_obj.id)
        area = Area.objects.filter(id = area).first()
        order = Order.objects.create( user = user , area = area , price = price )
        order.food.set(order_item_keys)
        order.save()
        return Response({"id":order.id})