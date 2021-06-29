from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    return render(request, 'index.html')

def money(request):
    if 'farm' in request.POST:
        