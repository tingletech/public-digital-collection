# this wsgi is configured to live in ucverse-env/ucverse-djsite/deploy.

import os
import sys

# redirect sys.stdout to sys.stderr for bad libraries like geopy that uses
# print statements for optional import exceptions.
sys.stdout = sys.stderr

from os.path import abspath, dirname, join

sys.path.insert(0, abspath(dirname(__file__)))

os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
from django.conf import settings

#sys.path.insert(0, join(settings.PROJECT_ROOT, "apps"))
sys.path.insert(0, settings.PROJECT_ROOT)

sys.stderr.write("TEMPLATE_DIRS:"+str(settings.TEMPLATE_DIRS))

from django.core.handlers.wsgi import WSGIHandler
application = WSGIHandler()
