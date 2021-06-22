from django.conf.urls import url
from django.urls import path
from . import views # ' .' specifies in same directory

urlpatterns = [
    path('', views.index),
    path('another_one/<str:name>', views.another),
    path('third_one', views.third),
    path('hello/<int:num>', views.hello),
    path('redirected', views.redirected),
    path('complete_redirect', views.complete),
    path('<url>', views.catch_all)
]
