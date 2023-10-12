from django.db import models
from django.urls import reverse
from dashboard.models import WidgetUser
from django.http import HttpResponse
import datetime

class ForumPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(WidgetUser,on_delete=models.CASCADE,)
    pub_datetime = models.DateTimeField(default=datetime.datetime.now())

    class Meta:
        ordering = ('-pub_datetime',)

    def __str__(self):
        return '{} by {}'.format(self.title, self.author)

    def get_absolute_detail_url(self):
        return reverse('Forum:forumpost-detail', kwargs={'pk':self.pk})

class Reply(models.Model):
    body = models.TextField()
    author = models.ForeignKey(WidgetUser,on_delete=models.CASCADE,)
    pub_datetime = models.DateTimeField()
    forum_post = models.ForeignKey(ForumPost,on_delete=models.CASCADE)

    def __str__(self):
        return '{}'.format(self.author)
