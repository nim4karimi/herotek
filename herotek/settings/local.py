from .base import *

DEBUG = True
ALLOWED_HOSTS = ['*']

# print(os.path.dirname(__file__))



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.localherotest'),
    }
}