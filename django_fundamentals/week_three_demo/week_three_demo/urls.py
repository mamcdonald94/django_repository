from django.urls import path, include # include is a built-in function of Django, but must be imported

urlpatterns = [
    path('', include('main.urls')),
]
