from django.urls import path, include

urlpatterns = [
    path('main/', include('apps.main.urls')),
    path('random_word/', include('apps.random_word.urls')),
]
