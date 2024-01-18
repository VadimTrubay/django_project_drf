from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('all/', AllProductsViewSet.as_view()),
    path('add/', AddProductViewSet.as_view()),
    path('view/<int:pk>/', ViewProductViewSet.as_view()),
    path('edit/<int:pk>/', EditProductViewSet.as_view()),
    path('delete/<int:pk>/', DeleteProductViewSet.as_view()),
]