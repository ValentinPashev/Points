class EventSearchMixin:
    """ Миксин за търсене на събития по филтри """

    def filter_events(self, events, request):
        name = request.GET.get('name', '')
        location = request.GET.get('location', '')
        event_date = request.GET.get('date', '')
        branch = request.GET.get('branch', '')

        if name:
            events = events.filter(name__icontains=name)
        if location:
            events = events.filter(location__icontains=location)
        if event_date:
            events = events.filter(date__date=event_date)
        if branch:
            events = events.filter(branch=branch)

        return events