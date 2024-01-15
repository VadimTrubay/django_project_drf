from django.contrib import admin

from .models import Profile


class MyModel(admin.ModelAdmin):
    list_display = ['user']
    list_display_links = ('user',)


admin.site.register(Profile, MyModel)
