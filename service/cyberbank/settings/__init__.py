# flake8: noqa

import os
from dotenv import load_dotenv

load_dotenv()


if not os.getenv('DJANGO_ENV') == 'prod':
    from .development import *
else:
    from .production import *
