from django.views.generic import CreateView

from events.forms import EventCreateForm
from events.models import Event


# Create your views here.
class CreateEventView(CreateView):
    model = Event
    form_class = EventCreateForm
    success_url = 'index'
    template_name = 'events/create-event.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user.email
        return super().form_valid(form)