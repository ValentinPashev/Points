from django.urls import path
from events.views import CreateEventView, DashBoardView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('', DashBoardView.as_view(), name='dashboard')
]