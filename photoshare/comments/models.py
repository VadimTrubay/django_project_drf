from django.db import models
from django.contrib.auth.models import User


class Comment(models.Model):
    comment = models.CharField(max_length=50, unique=True, verbose_name='comment')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')

    def __str__(self):
        return f"{self.comment}"
