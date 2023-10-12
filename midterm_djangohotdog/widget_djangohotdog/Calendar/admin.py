from django.contrib import admin
from .models import Event, Location

class EventAdmin(admin.ModelAdmin):
	model = Event
	list_display = ('target_datetime', 'activity', 'estimated_hours', 'location', 'course')

class LocationAdmin(admin.ModelAdmin):
	model = Location
	list_display = ('mode', 'venue')

admin.site.register(Event, EventAdmin)
admin.site.register(Location, LocationAdmin)


