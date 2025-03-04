from django import forms

from events.models import Event


class BaseEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

class EventCreateForm(BaseEventForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'description', 'location', 'type',]

        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }