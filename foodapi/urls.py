from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('category', CategoryView, basename='Category')
router.register('fooditems', FoodItemView, basename='Fooditems')
router.register('area', AreaView, basename='Area')
router.register('orderitem', OrderItemView, basename='OrderItem')
router.register('order', OrderView, basename='Order')



urlpatterns = [
    path("", include(router.urls)),
    path('accounts/', include('allauth.urls')),
    path('create-order/',CreateOrderView.as_view()),
    path('order-history/',OrderHistoryView.as_view()),
]
