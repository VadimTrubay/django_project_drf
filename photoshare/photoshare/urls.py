from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/images/', include('pictures.urls')),
    path('api/comments/', include('comments.urls')),
    path('api/tags/', include('tags.urls')),
    path('api/users/', include('users.urls')),
]
