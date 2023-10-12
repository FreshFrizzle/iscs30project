# -*- coding: utf-8 -*-
"""
Created on Sat May 13 09:22:56 2023

@author: user
"""

from .models import Assignment
from django import forms

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = "__all__"