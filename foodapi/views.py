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

class CategoryView(GenericAPIView, ListModelMixin):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    def get(self, request):
        
        return self.list(request)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FoodItemView(GenericAPIView, ListModelMixin):
    
    serializer_class = FoodItemSerializer
    queryset = FoodItem.objects.all()

    def get(self, request):
        
        return self.list(request)

    def post(self, request):
        serializer = FoodItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)