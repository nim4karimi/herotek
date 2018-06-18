from django.urls import re_path , path
from .views import software

urlpatterns = [
    path('',software, name='software'),

]
