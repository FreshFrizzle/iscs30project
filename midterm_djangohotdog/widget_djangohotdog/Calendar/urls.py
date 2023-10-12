from django.urls import path 
from .views import calendar_view, EventDetailView, EventAddView, EventUpdateView

urlpatterns = [
	path('', calendar_view, name='index'),
	path('events/<int:pk>/details/', EventDetailView.as_view(), name='event-details'),
	path('events/add/', EventAddView.as_view(), name='event-add'),
	path('events/<int:pk>/edit/', EventUpdateView.as_view(), name='event-edit'),
]

app_name = "Calendar"