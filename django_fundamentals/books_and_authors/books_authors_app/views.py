from django.http.response import HttpResponse
from django.shortcuts import render, redirect, HttpResponse


def index(request):
    return HttpResponse('this is working')