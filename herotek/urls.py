
#from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include ,re_path
from captcha_admin import admin
from django.contrib.auth.models import User
# This should stay the same
admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('blog/', include('blog.urls')),
    path('apiv1/', include('apiv1.urls')),

]


urlpatterns += [
    re_path(r'^markdownx/', include('markdownx.urls')),
    re_path(r'^summernote/', include('django_summernote.urls')),
]


if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        re_path(r'^__debug__/', include(debug_toolbar.urls)),
    ] #+ urlpatterns