from django.urls import path

from .views import *


urlpatterns = [
    path('', TagListApiView.as_view()),
    path('create/', TagCreateApiView.as_view()),
    path('retrieve/<int:pk>/', TagRetrieveApiView.as_view()),
    path('update/<int:pk>/', TagUpdateApiView.as_view()),
    path('delete/<int:pk>/', TagDeleteApiView.as_view())
]