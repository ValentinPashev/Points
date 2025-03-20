from django.urls import path
from reports.views import FillReportView, user_autocomplete

urlpatterns = [
    path('report/edit/<int:event_id>/', FillReportView.as_view(), name='fill-report'),
    path('api/user-autocomplete/', user_autocomplete, name='user_autocomplete'),

]
