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