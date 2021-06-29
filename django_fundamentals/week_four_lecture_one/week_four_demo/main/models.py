from django.db import models


class Truck(models.Model):
    name = models.CharField(max_length=50)
    slogan = models.TextField()
    food_type = models.CharField(max_length=100)
    star_rating = models.IntegerField()
    expensive = models.BooleanField()
    speciality = models.CharField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_ad = models.DateTimeField(auto_now=True)
