from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home),
    path('register', register),
    path('login', login),
    path('welcome/<int:id>', welcome),
    path('logout', logout), 
]