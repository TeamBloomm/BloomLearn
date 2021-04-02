from django import forms

from .models import Slots
from .models import Session

class SessionForm(forms.ModelForm):

    class Meta:
        model = Session
        fields = ('title', 'text',)
        # DateTimeInput()

class SlotsForm (forms.ModelForm):
    class Meta:
        model = Slots
        fields = ('time', 'date')