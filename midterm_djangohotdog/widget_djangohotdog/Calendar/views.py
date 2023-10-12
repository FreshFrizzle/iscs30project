from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.http.response import HttpResponseRedirect
from .models import Event, Location
from .forms import EventForm

def calendar_view(request):
     context = {}
     context["events"] = Event.objects.all()  
     return render(request, 'calendar.html', context)

class EventDetailView(DetailView):
     model = Event
     template_name = "calendar/event-details.html"

class EventAddView(CreateView):
     model = Event
     fields = '__all__'
     template_name = "calendar/event-add.html"

     def post(self, request,*args,**kwargs):
          form = EventForm(request.POST) 
	
          if form.is_valid():
               new_event = form.save()
               url = "../" + new_event.get_absolute_url() +"/details/"
               return HttpResponseRedirect(url)
          else:
               return render(request, self.template_name, {'form': form})

class EventUpdateView(UpdateView):
     model = Event
     fields = '__all__'
     template_name = "calendar/event-edit.html"

     success_url = "../details"

