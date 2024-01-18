from django.urls import path

from .views import *

urlpatterns = [
    path('all/', AllOrdersViewSet.as_view()),
    path('add/', AddOrderViewSet.as_view()),
    path('view/<int:pk>/', ViewOrderViewSet.as_view()),
    path('edit/<int:pk>/', EditOrderViewSet.as_view()),
    path('delete/<int:pk>/', DeleteOrderViewSet.as_view()),
]
