from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('courses/create', add_course),
    path('courses/<int:id>/edit', edit_course),
    path('courses/<int:id>/destroy', remove_course),
]