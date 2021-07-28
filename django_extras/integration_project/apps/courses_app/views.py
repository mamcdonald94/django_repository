from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import Course
from ..login_reg_app.models import User

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
        return redirect('/courses')
    else:
        #course1 =
        Course.objects.create(
            course_name = request.POST['course_name'],
            description = request.POST['description'],
        )
        return redirect('/courses')

def edit_course(request, id):
    context = {
        'this_course': Course.objects.get(id=id)
    }
    return render(request, 'delete_course.html', context)

def remove_course(request, id):
    course1 = Course.objects.get(id=id)
    course1.delete()
    return redirect('/')

def users_courses(request):
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all(),
    }
    return render(request, 'users_courses.html', context)

def add_user(request):
    print(request.POST)
    if request.POST['users_dropdown'] == 'default_user':
        messages.error(request, 'Please choose a user from the dropdown menu to add them to the course')
        return redirect('/courses/users_courses')  
    if request.POST['courses_dropdown'] == 'default_course':
        messages.error(request, 'Please choose a course from the dropdown menu')
        return redirect('/courses/users_courses')            

    this_user = User.objects.get(id=request.POST['users_dropdown'])
    this_course = Course.objects.get(id=request.POST['courses_dropdown'])

    this_user.course = this_course
    this_user.save()
    return redirect('/courses/users_courses')