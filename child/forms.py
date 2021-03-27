from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django_countries.widgets import CountrySelectWidget

from child.models import ChildData, Guardian


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )

class GuardianForm(forms.ModelForm):
    class Meta:
        model = Guardian
        fields = "__all__"

class ChildRegistrationForm(forms.ModelForm):
    # Specify the name of the model to use.
    class Meta:
        model = ChildData
        fields = "__all__"
        widgets = {'country': CountrySelectWidget()}
        
