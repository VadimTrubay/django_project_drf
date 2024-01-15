from django.db import models
from django.core import validators
from django.contrib.auth.models import User

from pictures.validators import validate_file_size
from comments.models import Comment
from tags.models import Tag


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'user_{instance.public_id}/{filename}'


class Image(models.Model):
    public_id = models.CharField(max_length=150, unique=True, verbose_name='public id')
    description = models.CharField(max_length=150, verbose_name='description')
    image = models.ImageField(
        upload_to=image_directory_path,
        validators=[
            validate_file_size,
            validators.FileExtensionValidator(
                allowed_extensions=['jpg', 'jpeg', 'png']
            ),
        ],
        verbose_name='image',
    )
    qr_code_url = models.CharField(max_length=150, unique=True, verbose_name='qr code url')
    created_at = models.DateField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateField(auto_now=True, verbose_name='updated at')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='comment')
    tags = models.ManyToManyField(Tag, verbose_name='tag')
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='user')

    def __str__(self):
        return f"{self.public_id}"
