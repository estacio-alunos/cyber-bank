# flake8: noqa

from settings.development import  *
from dotenv import load_dotenv
import os

load_dotenv()

ALLOWED_HOSTS: list = [
    'localhost',
    '127.0.0.1',
]

DATABASES = {
    "default": {
        "ENGINE": os.getenv('CB_ENGINE'),
        "NAME": os.getenv('CB_NAME'),
        "USER": os.getenv('CB_USER'),
        "PASSWORD": os.getenv('CB_PASSWORD'),
        "HOST": os.getenv('CB_HOST'),
        "PORT": os.getenv('CB_PORT'),
    }
}