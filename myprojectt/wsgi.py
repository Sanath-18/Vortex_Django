"""
WSGI config for myprojectt project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys
path = os.path.expanduser('~/SANATH2004')
if path not in sys.path:
  sys.path.insert(0,path)
 os.environ['DJANGO_SETTINGS_MODULE'] = 'myprojectt.settings' 
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
