from django.forms import modelform_factory
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from django.template.base import kwarg_re
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView, DeleteView
from events.forms import EventCreateForm, SearchForm
from events.models import Event


# Create your views here.
class CreateEventView(CreateView):
    model = Event
    form_class = EventCreateForm
    success_url = reverse_lazy('index')
    template_name = 'events/create-event.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user.email
        return super().form_valid(form)


class DashBoardView(ListView, FormView):
    template_name = 'events/dashboard.html'
    context_object_name = 'events'
    form_class = SearchForm
    paginate_by = 8
    model = Event
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_queryset(self):
        now = timezone.now()
        events = Event.objects.filter(approved=True, date__gte=now)

        name = self.request.GET.get('name', '')
        location = self.request.GET.get('location', '')
        event_date = self.request.GET.get('date', '')

        if name:
            events = events.filter(name__icontains=name)
        if location:
            events = events.filter(location__icontains=location)
        if event_date:
            events = events.filter(date__date=event_date)

        return events

class EventDetailsView(DetailView):
    model = Event
    template_name = 'events/event-details.html'
    context_object_name = 'event'

    def get_object(self, queryset=None):
        return get_object_or_404(Event, pk=self.kwargs['pk'])



class EditEventView(UpdateView):
    model = Event
    template_name = 'events/edit_event.html'
    success_url = reverse_lazy('dashboard')

    def get_form_class(self):
        if self.request.user.is_superuser:
            return modelform_factory(Event, fields='__all__')
        else:
            return modelform_factory(Event, fields=('name', 'date', 'description', 'location', 'type', 'branch'))


class DeleteEventView(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('dashboard')

    def get_initial(self):
        pk = self.kwargs.get(self.pk_url_kwarg)
        event = Event.objects.get(pk=pk)
        return event.__dict__

    def dispatch(self, request, *args, **kwargs):
        pk = self.kwargs.get(self.pk_url_kwarg)
        event = self.get_object()
        profile = self.request.user

        if event.created_by != profile.email and not self.request.user.is_superuser:
            return HttpResponseForbidden("You do not have permission to delete this event.")

        return super().dispatch(request, *args, **kwargs)