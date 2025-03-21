from django import forms
from django.core.exceptions import ValidationError
from accounts.models import Profile
from .models import EventReport

class EventReportForm(forms.ModelForm):
    organizers_emails = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Въведете имейли, разделени със запетая'})
    )
    prepared_email = forms.EmailField(required=False)
    attended_emails = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Въведете имейли, разделени със запетая'}),
        required=False
    )
    participated_actively_emails = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Въведете имейли, разделени със запетая'}),
        required=False
    )

    class Meta:
        model = EventReport
        fields = [
            'number_of_days',
            'points_for_organizers',
            'points_for_prepared',
            'points_for_attended',
            'points_for_participated_actively',
            'completed'
        ]


