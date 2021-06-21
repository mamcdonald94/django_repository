from django.shortcuts import render, HttpResponse
def index(request):
    return HttpResponse("I am ready to handle a request for '/'!")

