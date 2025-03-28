from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms import modelform_factory
from django.http import HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import require_POST
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
import json
from events.forms import EventCreateForm
from events.mixins import EventSearchMixin
from events.models import Event, FavouriteEvent


# Create your views here.
class CreateEventView(CreateView):
    model = Event
    form_class = EventCreateForm
    success_url = reverse_lazy('index')
    template_name = 'events/create-event.html'

    def form_valid(self, form):
        user_profile = self.request.user.profile

        if user_profile.branch == '':
            return redirect('profile', pk=self.request.user.id)

        form.instance.created_by = self.request.user.email
        form.instance.branch = user_profile.branch
        return super().form_valid(
            form)  #:TODO synchronize poster and branch so there can not be made event without a certain user complite his profile!


class DashBoardView(EventSearchMixin, ListView):
    template_name = 'events/dashboard.html'
    context_object_name = 'events'
    paginate_by = 6
    model = Event
    success_url = reverse_lazy('index')

    def get_queryset(self):
        now = timezone.now()
        events = self.model.objects.filter(approved=True, date__gt=now)
        return self.filter_events(events, self.request)


class DashboardWithPermView(PermissionRequiredMixin, EventSearchMixin, ListView):
    template_name = 'events/admin_dashboard.html'
    context_object_name = 'events'
    paginate_by = 6
    model = Event
    permission_required = 'events.can_approve_events'
    success_url = reverse_lazy('index')

    def has_permission(self):
        user = self.request.user
        if user.has_perm(self.permission_required):
            return True

        user_groups = user.groups.all()
        for group in user_groups:
            if group.permissions.filter(codename='can_approve_events').exists():
                return True

        return False

    def handle_no_permission(self):
        print(self.request.user.get_all_permissions())
        return redirect('index')

    def get_queryset(self):
        now = timezone.now()
        user_profile = self.request.user.profile
        events = self.model.objects.filter(approved=False, date__gt=now, committee=user_profile.committee)

        return self.filter_events(events, self.request)


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

        if event.created_by != profile.email and not self.request.user.is_superuser:  # Maybe it suppose to be OR instead of AND
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


def approve(request, pk):
    event = get_object_or_404(Event, id=pk)
    user = request.user

    if user.can_approve_events or user.has_perm('events.can_approve_events'):
        event.approved = True
        event.save()

    else:
        return HttpResponseForbidden("You do not have permission to approve this event.")

    return redirect(request.META.get('HTTP_REFERER'))

    # TODO: The events its set up as approved BUT i need to adjust it at the html because its not showing up properly and make a group with permissions who can approve and who can't
