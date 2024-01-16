from django.db import models
from django.contrib.auth.models import User

from comments.models import Comment
from tags.models import Tag


class Image(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    comment = models.ForeignKey(Comment, blank=True, null=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.image}"
