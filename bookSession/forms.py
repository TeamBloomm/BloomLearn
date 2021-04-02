from django import forms

from .models import Slots
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ('title', 'text',)

class SlotsForm (forms.ModelForm):
    class Meta:
        model = Slots
        fields = ('time', 'date')