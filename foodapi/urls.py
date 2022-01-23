from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('category', CategoryView, basename='Category')
router.register('fooditems', FoodItemView, basename='Fooditems')


urlpatterns = [
    path("", include(router.urls)),
    
]
