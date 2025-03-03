from events.models import Event


class BaseEventForm:
    class Meta:
        model = Event
        fields = '__all__'

class EventCreateForm(BaseEventForm):
    pass