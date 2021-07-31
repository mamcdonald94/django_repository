from django.core.exceptions import ValidationError
from django.db import models
import re
# our validator
def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            'first/last name must be longer than: 2'
        )

def email_validator(value):    
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    if not EMAIL_REGEX.match(value):   
        raise ValidationError(
            "please input a valid email address"
        )

def password_validator(value):
    PW_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')
    if not PW_REGEX.match(value):
        raise ValidationError(
            "password must be at least 8 characters, contain one uppercase letter, one lowercase letter, and one number"
        )



class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=45, validators= [email_validator], null=True)
    password = models.CharField(max_length=55, validators=[password_validator], null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)