from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return HttpResponse('This app is working!')
