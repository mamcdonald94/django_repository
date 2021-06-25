from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return render(request, 'index.html')

def submit(request):
    request.session['name'] = request.POST['name']
    request.session['dojo'] = request.POST['dojo']
    request.session['lang'] = request.POST['lang']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')

def result(request):
    return render(request, 'result.html')

def back(request):
    return render(request, 'index.html')
