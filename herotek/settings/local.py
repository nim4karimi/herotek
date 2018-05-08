from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = '127.0.0.1'

# Local App Install
INSTALLED_APPS +=[
    'debug_toolbar',
]

# local middle ware
MIDDLEWARE = [
    # ...
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# Tempory Data Base
# -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.localherotest'),
    }
}