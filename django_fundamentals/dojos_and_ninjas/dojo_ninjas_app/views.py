from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Dojo, Ninja


def index(request):
    context = {
        'dojos': Dojo.objects.all(),
        'ninjas': Ninja.objects.all(),
    }
    return render(request, 'index.html', context)

def dojo(request):
    dojo = Dojo.objects.create(
        name = request.POST['name'],
        city = request.POST['city'],
        state = request.POST['state']
    )
    return redirect('/')

def ninja(request):
    ninja = Ninja.objects.create(
        first_name = request.POST['fname'],
        last_name = request.POST['lname'],
        dojo = Dojo.objects.get(id=request.POST['dojo'])
    )
    return redirect('/')