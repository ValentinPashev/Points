from django.urls import path, include
from events.views import CreateEventView, DashBoardView, EventDetailsView, EditEventView, DeleteEventView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('', DashBoardView.as_view(), name='dashboard'),

    path("event/<int:pk>/", EventDetailsView.as_view(), name="event_detail"),

    path('<int:pk>/', include([
        path('edit/', EditEventView.as_view(), name='edit-event'),
        path('delete/', DeleteEventView.as_view(), name='delete-event'),
    ]))

]
