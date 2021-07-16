from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if postData['first_name'] == '':
            errors['first_name'] = 'Whoops! You forgot to put in your first name!'
        elif len(postData['first_name']) < 2:
            errors['first_name'] = 'First name must be at least two characters'
        if postData['last_name'] == '':
            errors['last_name'] = 'Whoops! You forgot to put in your last name!'
        elif len(postData['last_name']) < 2:
            errors['last_name'] = 'Last name must be at least two characters'
        if postData['email'] == '':
            errors['email'] = 'Whoops! You forgot to put in your email!'
        elif len(postData['email']) < 2:
            errors['email'] = 'First name must be at least two characters'
        if not EMAIL_REGEX.match(postData['email']):   
            errors['email'] = "Invalid email address!"
        users_with_email = User.objects.filter(email = postData['email'])
        if len(users_with_email) >= 1:
            errors['duplicate'] = "Email already exists."
        return errors


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()
