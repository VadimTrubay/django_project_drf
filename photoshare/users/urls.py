from django.urls import path, include

from .views import *

urlpatterns = [
    # path("login/", UserLoginView.as_view(), name="login"),
    # path("register/", UserRegistrationView.as_view(), name='register'),
    # path("logout/", UserLogOutView.as_view(), name="logout"),
    # path('<int:pk>/', UserRetrieveApiView.as_view()),
    path('profile/<int:pk>/', include(
        [path('', ProfileApiView.as_view()),
         path('update/', ProfileEditApiView.as_view()),
         path('delete/', ProfileDeleteApiView.as_view()),
         ]),
         ),
]
