import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'scrape.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

sys.stdout = sys.stderr # prevent crashes on print

path = '/var/www/scrape'
if path not in sys.path:
    sys.path.append(path)
path = '/var/www'
if path not in sys.path:
    sys.path.append(path)
