from django.db import models
from datetime import datetime

class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if postData['title'] == '':
            errors['title'] = 'Whoops! You forgot to put in the show title!'
        elif len(postData['title']) < 2:
            errors['title'] = 'Show title must be at least two characters long'
        if len(postData['network']) == 0:
            errors['network'] = 'Whoops! You forgot to put in the network name!'
        if len(postData['release_date']) == 0:
            errors['release_date'] = 'Whoops! You forgot to put in the release date!'
        if len(postData['description']) == 0:
            errors['description'] = 'Whoops! You forgot to put in a description!'
        # if len(postData['title']) < 2:
        #     errors['title'] = 'Show title must be at least two characters long'
        if len(postData['network']) < 3:
            errors['network'] = 'Network must be at least three characters long'
        if datetime.strptime(postData['release_date'], '%Y-%m-%d') > datetime.now():
            errors['release_date'] = 'Release date must be in the past!'
        if len(postData['description']) < 10:
            errors['description'] = 'Description must be at least 10 characters long'
        print(postData)
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = ShowManager()