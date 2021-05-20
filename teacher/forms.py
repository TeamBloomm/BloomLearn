from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django_countries.widgets import CountrySelectWidget

from teacher.models import FileUpload, TeacherData


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
        fields = ('t_id', 'about_user', 'phone_number', 'country', 'state')
        widgets = {'country': CountrySelectWidget()}

class FileUploadForm(forms.ModelForm):
    #name = forms.CharField(max_length=100)
    #course = forms.CharField(max_length=100)
    #week = forms.IntegerField(max_value=16)
    #file_ = forms.FileField()
    class Meta:
        model = FileUpload
        fields = ('name', 'course', 'week', 'filepath')

class ImageUploadForm(forms.Form):
    name = forms.CharField(max_length=100)
    picture = forms.ImageField()
