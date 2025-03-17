from django.urls import path
from reports.views import FillReport, user_autocomplete, create_event_report

urlpatterns = [
    path('report/edit/<int:event_id>/', FillReport.as_view(), name='fill-report'),
    path('api/user-autocomplete/', user_autocomplete, name='user_autocomplete'),
    path('event-report/create/', create_event_report, name='create_event_report'),

]
