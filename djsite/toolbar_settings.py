from settings import *
import sys

sys.path.insert(0,"/ucportal/briantinglecdliborg-solrpy/")

DEBUG_TOOLBAR = True
 
# Always show the toolbar 
DEBUG_TOOLBAR_CONFIG = { 
    'SHOW_TOOLBAR_CALLBACK': lambda req: True, 
} 

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'debug_toolbar',
)

