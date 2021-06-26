from django.urls import path     
from . import views

urlpatterns = [
    path('', views.generate),
    path('generate', views.generate),
    path('reset', views.reset),
]
