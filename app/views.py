from django.shortcuts import render
from .models import Service

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def service(request):
    services = Service.objects.all()
    return render(request, 'app/service.html', {'services':services})

def contact(request):
    return render(request, 'app/contact.html',)

def product(request):
    return render(request, 'app/product.html',)

def price(request):
    return render(request, 'app/price.html')