
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, FormView, ListView
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
        # Вземаме всички събития, които са одобрени и не са изтекли
        now = timezone.now()
        events = Event.objects.filter(approved=True, date__gte=now)

        # Проверяваме дали има параметри за търсене
        name = self.request.GET.get('name', '')
        location = self.request.GET.get('location', '')
        event_date = self.request.GET.get('date', '')

        # Применяме филтрите, ако има въведени стойности
        if name:
            events = events.filter(name__icontains=name)
        if location:
            events = events.filter(location__icontains=location)
        if event_date:
            events = events.filter(date__date=event_date)

        return events