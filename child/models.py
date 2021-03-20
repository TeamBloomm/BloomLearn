import pandas

# from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Child(models.Model):
    first_name = models.CharField(null=False, max_length = 100, primary_key =True)
    last_name = models.CharField(null=False,max_length = 100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', 
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    email_address = models.EmailField(null=False, max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length = 100)
    grade = models.IntegerField()
    password = models.CharField(max_length = 20)
    repeat_pass = models.CharField(max_length = 20)
    guardian = models.EmbeddedField(
        model_container=Guardian,
        null=False,
        blank=False
    )
    published_date = models.DateTimeField(auto_now_add=True) 
    objects = models.DjongoManager()

    def __str__(self):
        return self.first_name

class Guardian(models.Model):
    first_name = models.CharField(max_length = 100, primary_key=True)
    last_name = models.CharField(max_length = 100)
    email_address = models.EmailField(max_length=100)
    
    class Meta:
        abstract = True
# class Courses(models.Model):    