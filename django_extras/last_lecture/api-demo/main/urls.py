from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard),
    path('event/create', create),
    path('event/<int:id>', one_event)
]
