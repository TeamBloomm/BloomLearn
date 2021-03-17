from django import forms
from django.contrib.auth.forms import UserCreationForm

from child.models import Child, Guardian

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class ChildRegistrationForm(forms.ModelForm):
    username = None
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length= 100)
    phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$')
    email_address = forms.CharField(max_length= 100)
    country = forms.CharField(max_length = 100)
    state = forms.CharField(max_length = 100)
    grade = forms.IntegerField()
    password = forms.CharField(widget=forms.PasswordInput)
    repeat_pass = forms.CharField(widget=forms.PasswordInput)
    published_date = forms.DateTimeField()

    class Meta:
        model = Child
        fields = ('first_name', 'last_name', 'phone_number', 'email_address', 'country', 'state', 'grade', 'password', 'repeat_pass')
    
class GuardianRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length= 100)
    email_address = forms.CharField(max_length= 100)
    published_date = forms.DateTimeField()

    class Meta:
        model = Guardian
        fields = ('first_name', 'last_name', 'email_address')
