from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Announcement, Reaction
from .forms import AnnouncementForm

def index(request):
    return render(request, 'announcement_board/announcements.html', {'Announcements': Announcement.objects.all})


class AnnouncementDetailView(DetailView):
    model = Announcement
    template_name = 'announcement_board/announcement-details.html'


class AnnouncementCreateView(CreateView):
    model = Announcement
    fields = ['title', 'body', 'author']
    template_name = 'announcement_board/announcement-add.html'


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    fields = ['title', 'body', 'author']
    template_name = 'announcement_board/announcement-edit.html'
