from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Entry , Author , Blog
from django.utils import timezone



class EntryDetailView(DetailView):
    model = Entry
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

class EntryListView(ListView):

    model = Entry

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context



# Create your views here.

#
# class index(ListView):
#     modal = Entry
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['pub_date'] = timezone.now()
#         return context

# def post_list(request):
#     posts = Entry.objects.filter(pub_date__lte=timezone.now()).order_by('pub_date')
#     return render(request, 'blog/bloghome.html', {'posts': posts})
#