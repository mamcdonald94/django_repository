from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=75)
    location = models.CharField(max_length=75)
    description = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
