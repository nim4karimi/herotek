from django.urls import re_path , path
from .views import client

urlpatterns = [
    path('clients/',client, name='clients')

]
