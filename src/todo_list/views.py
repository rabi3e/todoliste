from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def home(request):

    if request.method=="POST":
        form = ListForm(request.POST or None)
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

def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed =True
    item.save()
    return redirect  ('home') 

def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed =False
    item.save()
    return redirect  ('home') 

def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.warning(request, (' Item Has Been Deleted !!!!'))
    return redirect  ('home') 
