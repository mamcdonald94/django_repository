from django.urls import path, include

urlpatterns = [
    path('blogs/', include('apps.blogs.urls')),
    path('surveys/', include('apps.survey.urls')),
]
