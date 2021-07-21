from django.db import models
import re
# Create your models here.

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        if len(postData['name']) < 2:
            errors['name'] = "Name must be at least two characters long"
        if len(postData['alias']) < 2:
            errors['alias'] = "Alias must be at least two characters long"
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        current_user_emails = User.objects.filter(email = postData['email']) # queries a list of existing emails in db, if it already exists, will through the below error
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
        return errors

class AuthorManager(models.Manager):
    def author_validator(self, postData):
        errors = {}
        if len(postData['author_name']) < 2:
            errors['author_name'] = "Author name must be at least two characters long"
        author_in_db = Author.objects.filter(name=postData['author_name']) # queries a list of existing authors in db, if it already exists, will throw the below error
        if len(author_in_db) > 0:
            errors['duplicate_author'] = 'Author already exists'
        return errors

class ReviewManager(models.Manager):
    def review_validator(self, postData):
        errors = {}
        if len(postData['content']) < 10:
            errors['content'] = "Review must be at least 10 characters long"
        return errors

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # user_reviews = list of reviews associated with the user

class Book(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()
    # authors = list of authors associated with the book
    # book_reviews = list of reviews associated with the book

class Author(models.Model):
    name = models.CharField(max_length=255)
    books = models.ManyToManyField(Book, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = AuthorManager()

class Review(models.Model):
    content = models.TextField()
    rating = models.IntegerField()
    user_review = models.ForeignKey(User, related_name="user_reviews", on_delete=models.CASCADE)
    book_reviewed = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ReviewManager()