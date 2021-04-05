from datetime import datetime

from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from languages.fields import LanguageField

class FileUpload(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    week = models.IntegerField()
    filepath = models.FileField(upload_to='files/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}: {self.filepath}"

class ImageUpload(models.Model):
    _id = models.CharField(max_length=100, primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='pictures/')
    
class TeacherData(models.Model):
    t_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Username'
    )
    about_user = models.TextField(max_length= 500)
    phone_number = PhoneNumberField() #models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length = 100)
    published_date = models.DateTimeField(auto_now_add=True, ) 
    objects = models.DjongoManager()
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

class CourseData(models.Model):
    _id = models.CharField(max_length=100, verbose_name='Course Title', primary_key=True, unique=True)
    teacher = models.ForeignKey(
        TeacherData,
        on_delete=models.CASCADE,
    )
    enrolled_students = models.ArrayReferenceField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    description = models.TextField(max_length= 500)
    language = LanguageField(max_length=50)
    Cost = models.PositiveIntegerField()
    Content = models.ArrayReferenceField(
        to=FileUpload,
        on_delete=models.CASCADE,
    )
    #Badge= 
    #Feedback = 
    #Announcement =