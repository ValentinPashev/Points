from django.contrib import admin, messages

from .forms import EventReportForm
from .models import EventReport

class EventReportAdmin(admin.ModelAdmin):
    form = EventReportForm
    autocomplete_fields = ['organizers']  # Активира autocomplete в Django Admin
    list_display = ('event', 'completed', 'number_of_days')
    actions = ['approve_report']

    def approve_report(self, request, queryset):
        for report in queryset:
            if not report.completed:
                try:
                    report.distribute_points(request.user)
                    messages.success(request, f"Отчетът за {report.event.name} е одобрен и точките са раздадени.")
                except ValueError as e:
                    messages.error(request, str(e))
            else:
                messages.warning(request, f"Отчетът за {report.event.name} вече е одобрен.")

    approve_report.short_description = "Одобри избраните отчети"

admin.site.register(EventReport, EventReportAdmin)
