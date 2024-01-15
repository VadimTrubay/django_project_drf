import hashlib
from uuid import uuid4


def generate_name_image():
    name = hashlib.sha256(str(uuid4()).encode('utf-8')).hexdigest()
    return f"photo_share/{name}"
