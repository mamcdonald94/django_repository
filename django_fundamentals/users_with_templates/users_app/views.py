from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        'users': User.objects.all(),
    }
    return render(request, 'index.html', context)

def create_user(request):
    user1 = User.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email_address = request.POST['email'],
        age = request.POST['age']
    )
    return redirect('/')

# def reset(request):
#     request.session.flush()
#     return redirect('/')