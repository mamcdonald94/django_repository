from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least two characters long"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least two characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        current_user_emails = User.objects.filter(email = postData['email']) # queries a list of existing emails in db, if it already exists, will throw the below error
        if len(current_user_emails) > 0:
            errors['duplicate_email'] = 'Email already exists'
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least eight characters long"
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password'] = "Passwords did not match"
        return errors

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least two characters long"
        if len(postData['description']) < 5:
            errors['description'] = "Description must be at least five characters long"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # books_created = list of books created by the user
    # books_favorited = list of books favorited by the user

class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name="books_created", on_delete=models.CASCADE)
    favorited_by = models.ManyToManyField(User, related_name="books_favorited")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()