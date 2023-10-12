from django import forms
from .models import WidgetUser


class WidgetUserForm(forms.ModelForm):
    class Meta:
        model = WidgetUser
        fields = ['first_name', 
                  'middle_name', 
                  'last_name',
                  'department'
        ]