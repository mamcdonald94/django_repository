from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegistrationForm


def index(request):
    form = RegistrationForm()
    context = { 
        "myregistrationform": form 
    }
    return render(request, "index.html", context)

def register(request):
    if request.method == 'POST':
        bound_form = RegistrationForm(request.POST)
        print(bound_form.is_valid())
        print(bound_form.errors)

        return redirect('/')