from django.urls import path
from .views import *

urlpatterns = [
    path("category/", CategoryView.as_view()),
    path("fooditems/", FoodItemView.as_view()),
]
