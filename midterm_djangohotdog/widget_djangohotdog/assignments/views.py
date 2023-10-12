from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Assignment
from .forms import AssignmentForm

def assignment_view(request):
    context = {}
    context['Assignments'] = Assignment.objects.all
    return render(request, 'assignments.html', context)

class AssignmentDetails(DetailView):
    model = Assignment
    template_name = 'assignments/assignment-details.html'
    
class AddAssignment(CreateView):
    model = Assignment
    form = AssignmentForm
    fields = '__all__'
    template_name = 'assignments/assignment-add.html'
    
    def post(self, request, *args, **kwargs):
        form = AssignmentForm(request.POST)
        if form.is_valid():
            new_assignment = form.save()
            redirect_link = '../' + new_assignment.get_absolute_url() + '/details/'
            return HttpResponseRedirect(redirect_link)
        else:
            return render(request, self.template_name, {'form': form})
       
class EditAssignment(UpdateView):
    model = Assignment
    fields = '__all__'
    template_name = 'assignments/assignment-edit.html'
    
    success_url = '../details/'
        
    

    
    
    
    
    
    
    
    
    
    
    
    