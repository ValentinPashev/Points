from django import forms
from accounts.models import AppStudent
from .models import EventReport

class EventReportForm(forms.ModelForm):
    organizers = forms.ModelMultipleChoiceField(
        queryset=AppStudent.objects.all(),
        widget=forms.SelectMultiple(attrs={
            'class': 'autocomplete',
            'data-max-selections': '3'
        })
    )

    class Meta:
        model = EventReport
        fields = ['event', 'organizers', 'number_of_days', 'prepared', 'attended', 'participated_actively',
                  'points_for_organizers',
                  'points_for_prepared',
                  'points_for_participated_actively',
                  'points_for_attended']


    def clean_organizers(self):
        organizers = self.cleaned_data.get('organizers')
        if organizers and organizers.count() > 3:
            raise forms.ValidationError("Може да изберете максимум 3 организатори.")
        return organizers
