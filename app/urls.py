
from django.conf import settings
from django.urls import re_path , path
from django.views.static import serve
from django.contrib.auth.views import login , logout
from .views import index, service, contact, product, req, register

urlpatterns = [
    path('', index),
    path('service/', service, name="service"),
    path('contact/', contact, name="contact"),
    path('product/', product, name="product"),
    path('req/', req , name="req"),
    # Login Page
    path('login/', login , {'template_name':'app/login.html'}, name ="login"),
    # Logout Page 
    path('logout/', logout , {'template_name':'app/logout.html'}, name ="logout"),
    # Register 
    path('register/', register , name ="register"),

]


# ... the rest of your URLconf goes here ...

# Media Url
urlpatterns += [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    }),
 ]