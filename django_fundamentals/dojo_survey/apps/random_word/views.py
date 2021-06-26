from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string



def generate(request):
    counter = request.session.get('counter')
    if counter is None:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    context = {
        'number': get_random_string(length=14)
    }
    return render(request, 'generate.html', context)

def reset(request):
    counter = request.session.get('counter')
    if counter > 1:
        request.session['counter'] = 1
    context = {
        'number': get_random_string(length=14)
    }
    return render(request, 'generate.html', context)
