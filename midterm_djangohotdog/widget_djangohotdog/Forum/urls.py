from django.shortcuts import render
from django.urls import path
from .views import ForumView, ForumDetailsView, ForumAddView, ForumEditView

urlpatterns = [
    path('', ForumView, name='forum'),
    path('<int:pk>/details/', ForumDetailsView.as_view(), name='forumpost-detail'),
    path('add/', ForumAddView.as_view(), name='post-add'),
    path('<int:pk>/edit/', ForumEditView.as_view(), name='post-edit'),
]

app_name = "Forum"
