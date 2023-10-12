from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from .forms import ForumPostForm
from .models import ForumPost, Reply

def ForumView(request):
    context ={}
    context["post"] = ForumPost.objects.all() 
    
    return render(request, 'Forum/forum.html', context)


class ForumDetailsView(DetailView):
    model = ForumPost
    template_name = 'Forum/forumpost-details.html'
    

class ForumAddView(CreateView):
    model = ForumPost
    form_class = ForumPostForm
    template_name = 'Forum/forumpost-add.html'

    def get_success_url(self):
        return reverse('Forum:forumpost-detail', kwargs={'pk': self.object.pk})


class ForumEditView(UpdateView):
    model = ForumPost
    form_class = ForumPostForm
    template_name = 'Forum/forumpost-edit.html'

    def get_success_url(self):
        return reverse('Forum:forumpost-detail', kwargs={'pk': self.object.pk})

