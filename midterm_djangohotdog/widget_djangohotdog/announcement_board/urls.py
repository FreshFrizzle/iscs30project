from django.urls import path
from .views import (
        index, AnnouncementDetailView, AnnouncementCreateView, AnnouncementUpdateView
    )

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/details', AnnouncementDetailView.as_view(), name='announcement-details'),
    path('add', AnnouncementCreateView.as_view(), name='announcement-add'),
    path('<int:pk>/edit', AnnouncementUpdateView.as_view(), name='announcement-edit')
]

app_name = "announcement_board"
