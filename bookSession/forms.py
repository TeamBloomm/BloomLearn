from django import forms
from .models import Session, timeSlots

class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"

    def __init__(self, **kwargs):
        kwargs["format"] = "'%H:%M'"
        super().__init__(**kwargs)

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('title', 'sessionDate', 'duration', 'teacher')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["sessionDate"].widget = DateInput()
        self.fields["sessionTime"].widget = TimeInput()

class timeSlotsForm(forms.ModelForm):
    class Meta:
        model = timeSlots
        fields = ('slotDate', 'startTime', 'endTime')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["slotDate"].widget = DateInput()
        self.fields["startTime"].widget = TimeInput()
        self.fields["endTime"].widget = TimeInput()
