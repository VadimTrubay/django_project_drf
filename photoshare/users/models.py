from django.contrib.auth.models import User
from django.core import validators
from django.db import models

from users.validators import validate_file_size


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.user}/{filename}'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='user')
    profile_picture = models.ImageField(
        upload_to=user_directory_path,
        default='profile_pictures/profile_picture_default.jpg',
        validators=[
            validate_file_size,
            validators.FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            ),
        ],
        verbose_name='profile_picture',
    )

