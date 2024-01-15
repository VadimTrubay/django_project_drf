from django.core.exceptions import ValidationError


def validate_file_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("The file size should not be larger than 5 MB.")
