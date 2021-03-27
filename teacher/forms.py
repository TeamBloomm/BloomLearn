from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django_countries.widgets import CountrySelectWidget

from teacher.models import TeacherData


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password1' ,'password2' )


class TeacherRegistrationForm(forms.ModelForm):
    # Specify the name of the model to use.
    class Meta:
        model = TeacherData
        fields = "__all__"
        widgets = {'country': CountrySelectWidget()}
