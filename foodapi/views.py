from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.mixins import ListModelMixin
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class CategoryView(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class FoodItemView(ModelViewSet):
    
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()