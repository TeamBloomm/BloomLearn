from django import forms
from django.contrib.auth.forms import UserCreationForm

from child.models import Child

class MultipleForm(forms.Form):
    action = forms.CharField(max_length=60, widget=forms.HiddenInput())

class ChildRegistrationForm(forms.ModelForm):
    # Specify the name of the model to use.
    class Meta:
        model = Child
        fields = "__all__"
