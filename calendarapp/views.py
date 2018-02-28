from django.shortcuts import render
def calendar(request):
    return render(request, 'calendarapp/index.html')