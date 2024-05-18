from django.contrib import admin

from .models import Product


class MyProduct(admin.ModelAdmin):
    list_display = ('id', 'product')
    list_display_links = ('id', 'product')


admin.site.register(Product, MyProduct)
