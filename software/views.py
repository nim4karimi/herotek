from django.shortcuts import render
from django.http import HttpResponse



def software(request):
    return render(request, 'main/base.html')
# Create your views here.
