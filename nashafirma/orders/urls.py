from django.urls import path, include
from rest_framework import routers

from .views import *

routers_order = routers.DefaultRouter()
routers_order.register(r'order', OrderViewSet, basename='order')

routers_items = routers.DefaultRouter()
routers_items.register(r'item', ItemsViewSet, basename='item')

urlpatterns = [
    path('', AllOrdersViewSet.as_view()),
    path('', include(routers_order.urls)),
    path('', AllItemsViewSet.as_view()),
    path('', include(routers_items.urls)),
]