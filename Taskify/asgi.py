"""
ASGI config for Taskify project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from manage import VENV

os.environ.setdefault('DJANGO_SETTINGS_MODULE', VENV)

application = get_asgi_application()
