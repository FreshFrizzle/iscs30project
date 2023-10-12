from django.db import models
from assignments.models import Course
from django.urls import reverse

class Location(models.Model):
	mode_choices = [
	  ('onsite', 'onsite'),
        ('online', 'online'),
        ('hybrid', 'hybrid')
	]
	mode = models.CharField(max_length=6, choices = mode_choices, blank=True)
	venue = models.TextField(max_length=200)

	def __str__(self):
		return '{}, {}'.format(self.mode, self.venue)
	
	def get_absolute_url(self):
		return reverse('calendar:event-details', kwargs={'pk':self.pk})


class Event(models.Model):
	activity = models.TextField(max_length=100)
	target_datetime = models.DateTimeField()
	estimated_hours = models.FloatField(default='0')
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return '{}: {} on {}'.format(self.course, self.activity, self.target_datetime)

	def get_absolute_url(self):
		return f"{self.pk}"