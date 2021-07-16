from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt


def home(request):
    return render(request, 'reg_log.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        else:
            hash_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user1 = User.objects.create(
                first_name = request.POST['first_name'],
                last_name = request.POST['last_name'],
                email = request.POST['email'],
                password = hash_pw
            )
            request.session['logged_user'] = user1.id
        return redirect('/login')

def login(request):
    if request.method == "POST":
        user = User.objects.filter(email = request.POST['email'])

        if user:
            log_user = user[0]

            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                request.session['logged_user'] = log_user.id
                return redirect(f'/welcome/{log_user.id}')
        messages.error(request, "Email or password are incorrect.")

    return redirect('/')

def welcome(request, id):
    # if request.method == 'POST':
        context = {
            'user1': User.objects.get(id=id)
        }
        print('hello')
        return render(request, 'welcome.html', context)
    # else:
    #     print(request.POST)
        return redirect('/')

def logout(request):
    request.session.flush()
    return redirect('/')