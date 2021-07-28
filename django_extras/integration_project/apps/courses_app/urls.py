from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('create', add_course),
    path('<int:id>/edit', edit_course),
    path('<int:id>/destroy', remove_course),
    path('users_courses', users_courses),
    path('add_user', add_user),
]