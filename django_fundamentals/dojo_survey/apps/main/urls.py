from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('submit_form', views.submit, name='test_submit'),
    path('index.html', views.back, name='test_back'),
    path('result.html', views.result),
]
