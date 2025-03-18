from django.shortcuts import get_object_or_404
from django.views.generic import UpdateView
from accounts.models import AppStudent
from events.models import Event
from reports.models import EventReport
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import EventReportForm


# Create your views here.

class FillReport(UpdateView):
    model = EventReport
    form_class = EventReportForm
    template_name = 'reports/fill_report.html'

    def get_object(self, queryset=None):
        event_id = self.kwargs['event_id']
        return get_object_or_404(EventReport, event_id=event_id)

    def form_valid(self, form):
        event = get_object_or_404(Event, event_id=self.kwargs['event_id'])
        event.completed = True
        event.save()
        form.save()

        return redirect('event_detail', pk=self.object.pk)



def user_autocomplete(request):
    query = request.GET.get('term', '')
    users = AppStudent.objects.filter(email__icontains=query)[:10]
    results = [{'id': user.id, 'text': user.email} for user in users]
    return JsonResponse(results, safe=False)

def create_event_report(request):
    """Създаване на отчет за събитие."""
    form = EventReportForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('home')  # Пренасочване след записване

    return render(request, 'reports/event_report_form.html', {'form': form})

