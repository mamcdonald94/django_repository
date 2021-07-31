from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegistrationForm
from .models import User
import bcrypt


def index(request):
    form = RegistrationForm()
    context = { 
        "myregistrationform": form 
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == 'POST':
        bound_form = RegistrationForm(request.POST)
        form_errors = bound_form.errors
    if form_errors:
            for key, error in form_errors.items():
                messages.error(request, error)
            return redirect('/')
    else:
        hash_pw = bcrypt.hashpw(bound_form.cleaned_data['password'].encode(), bcrypt.gensalt()).decode()
        this_user = User.objects.create(
            first_name = bound_form.cleaned_data['first_name'],
            last_name = bound_form.cleaned_data['last_name'],
            email = bound_form.cleaned_data['email'],
            password = hash_pw
        )
        return redirect(f'/dashboard/{this_user.id}')




def dashboard(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')