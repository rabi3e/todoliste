from django.shortcuts import render
from .models import List
# Create your views here.
def home(request):

    items = List.objects.all

    return render(request, 'home.html', {'items': items})

def about(request):
    return render(request, 'about.html', {})