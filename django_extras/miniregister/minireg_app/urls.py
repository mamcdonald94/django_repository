from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('register', register),
    path('dashboard/<int:user_id>', dashboard),
]