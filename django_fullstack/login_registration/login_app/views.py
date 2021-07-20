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
            request.session['log_user_id'] = user1.id
            return redirect(f'/welcome/{user1.id}')

def login(request):
    if request.method == "POST":
        print("POST")
    # else:
    #     print('GET')
        user = User.objects.filter(email = request.POST['email'])
        print(user)

        if user:
            log_user = user[0]
            print(log_user.id)
            if bcrypt.checkpw(request.POST['password'].encode(), log_user.password.encode()):
                print('password match')
                request.session['log_user_id'] = log_user.id
                return redirect(f'/welcome/{log_user.id}')
            else:
                messages.error(request, "invalid email or password")
        else:
            messages.error(request, "Email does not exist.")

    return redirect('/')

def welcome(request, id):
    if "log_user_id" not in request.session:
            return redirect('/')
    else:
        context = {
            'user1': User.objects.get(id=id)
        }
        return render(request, 'welcome.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')