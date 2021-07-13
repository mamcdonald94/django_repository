from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Show

def shows(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'shows.html', context)

def new(request):
    return render(request, 'new_show.html')

def create_show(request):

    errors = Show.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    else:
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

    errors = Show.objects.basic_validator(request.POST)
    show1 = Show.objects.get(id=id)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show1.id}/edit')
    else:
        show1.title = request.POST['title']
        show1.network = request.POST['network']
        show1.description = request.POST['description']
        show1.save()
        return redirect(f'/shows/{show1.id}')

def delete(request, id):
    show1 = Show.objects.get(id=id)
    show1.delete()
    return redirect('/shows')