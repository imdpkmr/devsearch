"""
WSGI config for devsearch project.
Web Server Gateway Interface is a simple calling convention for web servers to forward requests to web application or frameworks written in Python programming language.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'devsearch.settings')

application = get_wsgi_application()
