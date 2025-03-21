from django.urls import path
from reports.views import user_autocomplete, approve_event_report, update_event_report

urlpatterns = [
    path('report/edit/<int:event_id>/', update_event_report, name='update_event_report'),
    path('report/approve/<int:report_id>/', approve_event_report, name='approve_event_report'),
    path('api/user-autocomplete/', user_autocomplete, name='user_autocomplete'),

]
