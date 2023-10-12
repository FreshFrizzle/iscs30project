from django.db import models
from django.urls import reverse

class Announcement(models.Model):
    title = models.CharField(max_length=200, blank=True)
    body = models.TextField(blank=True)
    author = models.ForeignKey("dashboard.WidgetUser", blank=True, on_delete=models.CASCADE)
    pub_datetime = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
       return self.title 

    def get_absolute_url(self):
        return reverse('announcement_board:announcement-details', kwargs={'pk':self.pk})
    

class Reaction(models.Model):
    reaction_choices = [
        ('Like', 'Like'),
        ('Love', 'Love'),
        ('Angry', 'Angry')
    ]
    name = models.CharField(max_length=5, choices=reaction_choices, blank=True)
    tally = models.IntegerField(default=0)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE)
     
    def __str__(self):
       return f"{self.announcement} - {self.name}" 
