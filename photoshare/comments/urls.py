from django.urls import path

from .views import *


urlpatterns = [
    path('', CommentListApiView.as_view()),
    path('create/', CommentCreateApiView.as_view()),
    path('retrieve/<int:pk>/', CommentRetrieveApiView.as_view()),
    path('update/<int:pk>/', CommentUpdateApiView.as_view()),
    path('delete/<int:pk>/', CommentDeleteApiView.as_view())
]