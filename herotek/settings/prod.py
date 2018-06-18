from .base import *

ALLOWED_HOSTS = ['.herotek.ir', '51.255.213.190', 'www.herotek.ir']
DEBUG = False


# Tempory Data Base
# -----------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'herotek',
        'USER': 'nima',
        'PASSWORD': '%BpigXM1S6vyYzdRygAT7Y6TLxtJyL',
        'HOST': 'localhost',
        'PORT': '',
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
#WOOPRA_DOMAIN = 'herotek.ir'
#HUBSPOT_PORTAL_ID = '4365011'

