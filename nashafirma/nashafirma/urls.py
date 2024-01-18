from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/items/', include('orders.urls')),
    path('api/products/', include('products.urls')),
]
