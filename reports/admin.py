from django.contrib import admin

from .forms import EventReportForm
from .models import EventReport

class EventReportAdmin(admin.ModelAdmin):
    form = EventReportForm
    autocomplete_fields = ['organizers']  # Активира autocomplete в Django Admin

admin.site.register(EventReport, EventReportAdmin)