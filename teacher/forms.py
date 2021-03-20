from django import forms
from django.contrib.auth.forms import UserCreationForm

from teacher.models import TeacherData

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class TeacherRegistrationForm(forms.ModelForm):
    # Specify the name of the model to use.
    class Meta:
        model = TeacherData
        fields = "__all__"
