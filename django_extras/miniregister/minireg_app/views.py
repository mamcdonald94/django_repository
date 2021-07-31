from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User


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
            context = {
                "errors": form_errors.values()
            }
            return render(request, "index.html", context)
        else:
            this_user = User.objects.create(
                first_name = bound_form.cleaned_data['first_name'],
                last_name = bound_form.cleaned_data['last_name'],
                email = bound_form.cleaned_data['email'],
                password = bound_form.cleaned_data['password']
            )
            return redirect(f'/dashboard/{this_user.id}')


    return redirect('/')

def dashboard(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard.html', context)