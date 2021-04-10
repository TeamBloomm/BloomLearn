from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django_countries.widgets import CountrySelectWidget

from child.models import ChildData


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )



class ChildRegistrationForm(forms.ModelForm):
    # Specify the name of the model to use.
    class Meta:
        model = ChildData
        fields = ('c_id',  'about_user', 'phone_number', 'country', 'state', 'grade', 'guardian_first_name', 'guardian_last_name', 'guardian_email_address')
        widgets = {'country': CountrySelectWidget()}
        
