from django.shortcuts import render
from .models import Service , Prod

# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def service(request):
    services = Service.objects.all()
    return render(request, 'app/service.html', {'services':services})

def contact(request):
    return render(request, 'app/contact.html',)

def product(request):
    prods = Prod.objects.all()
    return render(request, 'app/product.html', {'prods': prods})

def req(request):
    return render(request, 'app/req.html')