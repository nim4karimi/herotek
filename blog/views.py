from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone
from .models import Entry , Author , Blog
from django.utils import timezone

# Create your views here.

#
# class index(ListView):
#     modal = Entry
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pub_date'] = timezone.now()
#         return context

def post_list(request):
    posts = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
    return render(request, 'blog/bloghome.html', {'posts': posts})