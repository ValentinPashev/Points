from django.urls import path, include

from events import views
from events.views import CreateEventView, DashBoardView, EventDetailsView, EditEventView, DeleteEventView, \
    toggle_favourite, DashboardWithPermView

urlpatterns = [
    path('create/', CreateEventView.as_view(), name='create-event'),
    path('', DashBoardView.as_view(), name='dashboard'),
    path('dashboard_admin/', DashboardWithPermView.as_view(), name='dashboard-admin'),

    path("event/<int:pk>/", EventDetailsView.as_view(), name="event_detail"),

    path("toggle-favourite/", toggle_favourite, name="toggle-favourite"),

    path('<int:pk>/', include([
        path('edit/', EditEventView.as_view(), name='edit-event'),
        path('delete/', DeleteEventView.as_view(), name='delete-event'),
        path('approve/', views.approve, name='approve'),
    ]))

]
