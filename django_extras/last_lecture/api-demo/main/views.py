from django.shortcuts import render, redirect
from .models import Event

# Create your views here.
def dashboard(request):
    context = {
        'events': Event.objects.all()
    }
    return render(request, 'index.html', context)

def create(request):
    event = Event.objects.create(
        title = request.POST['title'],
        location = request.POST['location'],
        description = request.POST['description']
    )
    return redirect('/')

def one_event(request, id):
    context = {
        'event': Event.objects.get(id=id) 
    }

    return render(request, 'one_event.html', context)