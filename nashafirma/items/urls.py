from django.urls import path, include

from .views import *


urlpatterns = [
    path('all/', AllItemsViewSet.as_view()),
    path('add/', AddItemViewSet.as_view()),
    path('view/<int:pk>/', ViewItemViewSet.as_view()),
    path('edit/<int:pk>/', EditItemViewSet.as_view()),
    path('delete/<int:pk>/', DeleteItemViewSet.as_view()),
]
