from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('add_dojo', views.dojo),
    path('add_ninja', views.ninja),
]