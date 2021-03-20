from datetime import datetime

# from django.conf import settings
#from django.db import models
from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class TeacherData(models.Model):
    first_name = models.CharField(max_length = 100, primary_key =True)
    last_name = models.CharField(max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    email_address = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length = 100)
    password = models.CharField(max_length = 20)
    repeat_pass = models.CharField(max_length = 20)
    published_date = models.DateTimeField(auto_now_add=True, ) 
    objects = models.DjongoManager()

    def __str__(self):
        return self.first_name

# class Courses(models.Model):    
