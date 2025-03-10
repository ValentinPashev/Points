from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, FormView, ListView, DetailView, UpdateView, DeleteView
import json
from events.forms import EventCreateForm, SearchForm
from events.models import Event, FavouriteEvent


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
    paginate_by = 6
    model = Event
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        now = timezone.now()
        events = Event.objects.filter(approved=True, date__gte=now).order_by('date')

        name = self.request.GET.get('name', '')
        location = self.request.GET.get('location', '')
        event_date = self.request.GET.get('date', '')
        branch = self.request.GET.get('branch', '')

        if name:
            events = events.filter(name__icontains=name)
        if location:
            events = events.filter(location__icontains=location)
        if event_date:
            events = events.filter(date__date=event_date)
        if branch:
            events = events.filter(branch=branch)

        return events


class EventDetailsView(DetailView):
    model = Event
    template_name = 'events/event-details.html'
    context_object_name = 'event'

    def get_object(self, queryset=None):
        return get_object_or_404(Event, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.is_authenticated:
            context['is_favourite'] = FavouriteEvent.objects.filter(user=user, event=self.object).all()
        else:
            context['is_favourite'] = False

        return context

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

        if event.created_by != profile.email and not self.request.user.is_superuser:  #Maybe it suppose to be OR instead of AND
            # TODO: Test it!
            return HttpResponseForbidden("You do not have permission to delete this event.")

        return super().dispatch(request, *args, **kwargs)


@csrf_protect
@login_required
@require_POST
def toggle_favourite(request):
    try:
        data = json.loads(request.body)
        event_id = data.get("event_id")

        if not event_id:
            return JsonResponse({"error": "Missing event ID"}, status=400)

        event = Event.objects.get(pk=event_id)

        favourite = FavouriteEvent.objects.filter(user=request.user, event=event)

        if favourite.exists():
            favourite.delete()
            return JsonResponse({"message": "Removed from favourites", "favourite": False})

        FavouriteEvent.objects.create(user=request.user, event=event)
        return JsonResponse({"message": "Added to favourites", "favourite": True})

    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)
    except Event.DoesNotExist:
        return JsonResponse({"error": "Event not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)