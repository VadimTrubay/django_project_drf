from django.urls import path

from .views import *


urlpatterns = [
    path('', ImageListApiView.as_view()),
    path('create/', ImageCreateApiView.as_view()),
    path('retrieve/<int:pk>/', ImageRetrieveApiView.as_view()),
    path('update/<int:pk>/', ImageUpdateApiView.as_view()),
    path('delete/<int:pk>/', ImageDeleteApiView.as_view())
]