from django.contrib import admin
from django.urls import path, include

from pictures.views import *
from comments.views import *
from tags.views import *
from users.views import *
from rest_framework import routers


routers_img = routers.DefaultRouter()
routers_img.register(r'images', ImageViewSet, basename='images')

routers_comm = routers.SimpleRouter()
routers_comm.register(r'comments', CommentViewSet, basename='comments')

routers_tag = routers.SimpleRouter()
routers_tag.register(r'tags', TagViewSet, basename='tags')

routers_usr = routers.SimpleRouter()
routers_usr.register(r'users', UserViewSet, basename='users')

routers_prof = routers.SimpleRouter()
routers_prof.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers_img.urls)),
    path('api/', include(routers_comm.urls)),
    path('api/', include(routers_tag.urls)),
    path('api/', include(routers_usr.urls)),
    path('api/', include(routers_prof.urls)),
]
