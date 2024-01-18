from django.urls import path, include
from rest_framework import routers

from .views import *

routers_product = routers.DefaultRouter()
routers_product.register(r'product', ProductViewSet, basename='product')


urlpatterns = [
    path('', AllProductsViewSet.as_view()),
    path('', include(routers_product.urls)),
]