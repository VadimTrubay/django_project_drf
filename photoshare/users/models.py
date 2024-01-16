from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    profile_picture = models.ImageField(upload_to='profile_picture', verbose_name='profile_picture')
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=50, default='')
    phone = models.CharField(max_length=25, default='')

    def __str__(self):
        return f"{self.user}"

