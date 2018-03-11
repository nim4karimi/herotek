"""herotek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import re_path , path
from django.views.static import serve
from django.contrib.auth.views import login
from .views import index , service , contact , product, req
urlpatterns = [
    path('', index),
    path('service/', service , name="service"),
    path('contact/', contact , name="contact"),
    path('product/', product , name="product"),
    path('req/', req , name="req"),
    # Login Page
    path('login/', login , {'template_name':'app/login.html'}, name ="login"),
]


# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]