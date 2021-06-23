from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('result.html', views.submit),
    path('index.html', views.back),
]