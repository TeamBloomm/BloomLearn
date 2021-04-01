from datetime import datetime

from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

from teacher.models import CourseData 

class Guardian(models.Model):
    first_name = models.CharField(max_length = 100, primary_key =True)
    last_name = models.CharField(max_length = 100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name
    
    class Meta: 
        abstract = True

class Subject(models.Model):
    models.CharField(max_length=10, blank=True)

    class Meta:
        abstract = True


class ChildData(models.Model):
    c_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    about_user = models.TextField(max_length= 500)
    phone_number = PhoneNumberField() #models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length = 100)
    grade = models.IntegerField()
    guardian_first_name = models.CharField(max_length = 100, primary_key =True)
    guardian_last_name = models.CharField(max_length = 100)
    guardian_email_address = models.EmailField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True, ) 
    subjects = models.ArrayField(
        model_container=Subject
    )
    Courses = models.ArrayReferenceField(
        to=CourseData,
        on_delete=models.CASCADE
    )
    objects = models.DjongoManager(

    )

    def __str__(self):
        return self.first_name    
