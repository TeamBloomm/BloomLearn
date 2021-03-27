from datetime import datetime

# from django.conf import settings
#from django.db import models
from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


class TeacherData(models.Model):
    t_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    about_user = models.CharField(max_length= 500)
    phone_number = PhoneNumberField() #models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length = 100)
    published_date = models.DateTimeField(auto_now_add=True, ) 
    objects = models.DjongoManager()

    def __str__(self):
        return self.first_name

# class Courses(models.Model):    

