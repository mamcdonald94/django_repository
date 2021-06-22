from django.shortcuts import render, HttpResponse, redirect

def index(request): # methods ALWAYS take in a request
    return HttpResponse('Hello World')

def another(request, name):
    return HttpResponse(f'this one is different. right, {name}?')

def third(request):
    return HttpResponse('this one is too')

def hello(request, num):
    print(num)
    return render(request, "index.html")

def redirected(request):
    return redirect('/complete_redirect')

def complete(request):
    return render(request, "redirect.html")

def catch_all(request, url):
    return render(request, 'catch.html')
