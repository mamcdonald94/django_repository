from django.db import models

class User(models.Model):
    name = models.CharField(max_length=45)
    weight = models.IntegerField()
    age = models.IntegerField()
    always_hungry = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # tacos = [contains every taco associated with a user]

class Taco(models.Model):
    name = models.CharField(max_length=75)
    toppings = models.TextField()
    meat = models.BooleanField()
    spicy = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name= 'tacos', on_delete=models.CASCADE)
