from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_form', views.submit),
    path('index.html', views.back),
    path('result.html', views.result),
]
