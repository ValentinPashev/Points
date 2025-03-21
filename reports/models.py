from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile, AppStudent


class EventReport(models.Model):
    event = models.OneToOneField(
        'events.Event', on_delete=models.CASCADE, related_name='reports'
    )
    organizers = models.ManyToManyField(Profile, related_name='organized_events')
    prepared = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name='prepared_reports')
    attended = models.ManyToManyField(Profile, related_name='attended_events', blank=True)
    participated_actively = models.ManyToManyField(Profile, related_name='active_participants', blank=True)

    number_of_days = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)

    points_for_organizers = models.IntegerField(default=10)
    points_for_prepared = models.IntegerField(default=5)
    points_for_attended = models.IntegerField(default=2)
    points_for_participated_actively = models.IntegerField(default=3)

    def distribute_points(self, approved_by: AppStudent):
        """Разпределя точки към участниците в отчета, само ако е одобрен"""
        if not self.completed:
            raise ValueError("Отчетът не е маркиран като завършен!")

        for organizer in self.organizers.all():
            organizer.points += self.points_for_organizers
            organizer.save()

        if self.prepared:
            self.prepared.points_from_events += self.points_for_prepared
            self.prepared.save()

        for attendee in self.attended.all():
            attendee.points += self.points_for_attended
            attendee.save()

        for participant in self.participated_actively.all():
            participant.points += self.points_for_participated_actively
            participant.save()

        self.completed = True
        self.save()