from django.contrib import admin
from django.utils.html import format_html
from .models import Image

class MyImage(admin.ModelAdmin):
    list_display = ['id', 'image', 'tags_display', 'description', 'comment', 'user', 'created_at', 'updated_at']
    list_display_links = ('id', 'image', 'tags_display', 'description', 'comment', 'user', 'created_at', 'updated_at')

    def image_display(self, obj):
        return format_html('<img src="{}" width="50" height="50" />', obj.image.url)

    image_display.short_description = 'Image'

    def tags_display(self, obj):
        return ', '.join(tag.tag for tag in obj.tags.all())

    tags_display.short_description = 'Tags'

admin.site.register(Image, MyImage)
