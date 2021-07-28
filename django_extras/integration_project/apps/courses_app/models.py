from django.db import models


class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['course_name']) < 5:
            errors['course_name'] = 'Course name must be at least five characters long'
        if len(postData['description']) < 15:
            errors['description'] = 'Course description must be at least 15 characters long'
        return errors

class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = CourseManager()
    # users = list of users associated with the course