from django.conf import settings
from django.urls import re_path , path
from django.views.static import serve

from .views import EntryDetailView , EntryListView


urlpatterns = [

    #List View
    path('', EntryListView.as_view(), name='entry-list'),

    #Detail View
    path('<slug:slug>/', EntryDetailView.as_view() , name='entry-detail'),

]


# ... the rest of your URLconf goes here ...

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]