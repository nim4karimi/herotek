from .base import *

ALLOWED_HOSTS = ['.herotek.ir']
DEBUG = False


# Tempory Data Base
# -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.hero'),
    }
}



# SSL Config
# ----------
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE= True


# Analytic
# --------
GOOGLE_ANALYTICS_PROPERTY_ID = 'UA-115020420-1'
# WOOPRA_DOMAIN = 'herotek.ir'
# HUBSPOT_PORTAL_ID = '4365011'