from django.shortcuts import render
from django.http import HttpResponse



def client(request):
    return render(request, 'servers/client.html')
# Create your views here.
