from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses.html", context)

def add_course(request):
    errors = Course.objects.basic_validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        #course1 =
        Course.objects.create(
            course_name = request.POST['course_name'],
            description = request.POST['description']
        )
        return redirect('/')

def edit_course(request, id):
    context = {
        'this_course': Course.objects.get(id=id)
    }
    return render(request, 'delete_course.html', context)

def remove_course(request, id):
    course1 = Course.objects.get(id=id)
    course1.delete()
    return redirect('/')