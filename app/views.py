from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def service(request):
    services = Service.objects.all()
    return render(request, 'app/service.html', {'services':services})
