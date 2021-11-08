"""
ASGI config for devsearch project.
Asynchronous Server Gateway Interface is a spiritual successor to WSGI, intended to provide a standard interface between async-capable 
It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')

application = get_asgi_application()
