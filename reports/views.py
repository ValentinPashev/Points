from accounts.models import AppStudent
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from .models import EventReport
from events.models import Event
from .forms import EventReportForm

class FillReportView(UpdateView):
    model = EventReport
    form_class = EventReportForm
    template_name = 'reports/fill_report.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        event_id = self.kwargs['event_id']
        return get_object_or_404(EventReport, event__id=event_id)

    def form_valid(self, form):
        event_report = form.save(commit=False)
        event_report.completed = True
        event_report.save()

        organizers = form.cleaned_data['organizers']
        event_report.organizers.set(organizers)

        attended = form.cleaned_data['attended']
        event_report.attended.set(attended)

        participated_actively = form.cleaned_data['participated_actively']
        event_report.participated_actively.set(participated_actively)

        event_report.save()

        return redirect('event_detail', pk=event_report.pk)

    # def get_object(self, queryset=None):
    #     event_id = self.kwargs['event_id']
    #     return get_object_or_404(EventReport, event__id=event_id)

    # def form_valid(self, form):
    #
    #     dict_of_students = {
    #         'organizers': list(self.kwargs['organizers']),
    #         'prepared': list(self.kwargs['prepared']),
    #         'participated_actively': list(self.kwargs['participated_actively']),
    #         'attended': list(self.kwargs['attended'])
    #
    #     }
    #
    #     for role, email in dict_of_students.items():
    #         if role == 'organizers':
    #             user = get_object_or_404(AppStudent, email=email).profile
    #             user.points_from_events += form.cleaned_data['points_for_organizers']
    #
    #         elif role == 'prepared':
    #             user = get_object_or_404(AppStudent, email=email).profile
    #             user.points_from_events += form.cleaned_data['points_for_prepared']
    #         elif role == 'participated_actively':
    #             user = get_object_or_404(AppStudent, email=email).profile
    #             user.points_from_events += form.cleaned_data['points_for_participated_actively']
    #         elif role == 'attended':
    #             user = get_object_or_404(AppStudent, email=email).profile
    #             user.points_from_events += form.cleaned_data['points_for_attended']
    #


def user_autocomplete(request):
    query = request.GET.get('term', '')
    users = AppStudent.objects.filter(email__icontains=query)[:10]
    results = [{'id': user.id, 'text': user.email, 'name': user.profile.__str__()} for user in users]
    return JsonResponse(results, safe=False)
