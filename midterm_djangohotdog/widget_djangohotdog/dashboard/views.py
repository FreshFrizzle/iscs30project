from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Department, WidgetUser
from .forms import WidgetUserForm

def index(request):
    return render(request, 'dashboard/dashboard.html', {'Users':WidgetUser.objects.all})


class WidgetUserDetailView(DetailView):
    model = WidgetUser
    template_name = 'dashboard/widgetuser-details.html'


class WidgetUserCreateView(CreateView):
    model = WidgetUser
    fields = '__all__'
    template_name = 'dashboard/widgetuser-add.html'


class WidgetUserUpdateView(UpdateView):
    model = WidgetUser
    fields = '__all__'
    template_name = 'dashboard/widgetuser-edit.html'