from django.conf import settings
from django.urls import re_path , path
from django.views.static import serve



from .views import post_list
urlpatterns = [
    path('', post_list, name="blog"),

]


# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]