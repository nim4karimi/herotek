from django.shortcuts import render , redirect
from .models import Service , Prod

# Import builtin Create Form 
from django.contrib.auth.forms import UserCreationForm
# Custom Cregester form
from app.forms import RegisterationFrom



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


#Register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('/')
    else:
        form = UserCreationForm()
        args = {'form':form}
        return render(request, 'app/reg_form.html', args)
