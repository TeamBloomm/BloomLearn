from datetime import datetime

# from django.conf import settings
from django import forms
from djongo import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.conf import settings

from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField

class Guardian(models.Model):
    first_name = models.CharField(max_length = 100, primary_key =True)
    last_name = models.CharField(max_length = 100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return self.first_name
    
    class Meta: 
        abstract = True

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"

class ChildData(models.Model):
    c_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    about_user = models.CharField(max_length= 500)
    phone_number = PhoneNumberField() #models.CharField(validators=[phone_regex], max_length=17) # validators should be a list
    country = CountryField(blank_label='(select country)')
    state = models.CharField(max_length = 100)
    grade = models.IntegerField()
    guardian = models.EmbeddedField(
        model_container=Guardian,
        model_form_class=GuardianForm
        )
    published_date = models.DateTimeField(auto_now_add=True, ) 
    objects = models.DjongoManager()

    def __str__(self):
        return self.first_name

# class Courses(models.Model):    
