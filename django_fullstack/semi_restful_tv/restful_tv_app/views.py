from django.shortcuts import render, redirect, HttpResponse
from .models import Show

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new.html')

def create_show(request):
    this_show = Show.objects.create(
        title = request.POST['title'],
        network = request.POST['network'],
        release_date = request.POST['release_date'],
        description = request.POST['description']
    )
    return redirect(f'/shows/{this_show.id}')

def show_info(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request, 'show_info.html', context)

def edit_show(request, id):
    context = {
        'this_show': Show.objects.get(id=id)
    }
    return render(request, "edit_show.html", context)

def update(request, id):
    show1 = Show.objects.get(id=id)
    show1.title = request.POST['title']
    show1.network = request.POST['network']
    show1.description = request.POST['description']
    show1.save()
    return redirect(f'/shows/{show1.id}')

def delete(request, id):
    show1 = Show.objects.get(id=id)
    show1.delete()
    return redirect('/shows')