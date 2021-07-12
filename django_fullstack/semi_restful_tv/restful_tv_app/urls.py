from django.urls import path, include
from .views import *

urlpatterns = [
    path('', shows),
    path('shows/', shows),
    path('shows/new', new),
    path('shows/create', create_show),
    path('shows/<int:id>', show_info),
    path('shows/<int:id>/edit', edit_show),
    path('shows/<int:id>/update', update),
    path('shows/<int:id>/destroy', delete)
]