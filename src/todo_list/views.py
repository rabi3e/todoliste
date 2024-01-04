from django.shortcuts import render
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method=="POST":
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            items = List.objects.all
            messages.success(request, ('wawwww  Item Has Been Added to List!!!!'))
            return render(request, 'home.html', {'items': items})
            
    else :
        items = List.objects.all
        return render(request, 'home.html', {'items': items})

def about(request):
    return render(request, 'about.html', {})