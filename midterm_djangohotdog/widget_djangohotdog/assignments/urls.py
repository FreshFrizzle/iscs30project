# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 23:55:00 2023

@author: user
"""

from django.urls import path
from .views import assignment_view, AssignmentDetails, AddAssignment, EditAssignment

urlpatterns = [
    path('', assignment_view, name='assignments'),
    path('<int:pk>/details/', AssignmentDetails.as_view(), name='assignment-details'),
    path('add/', AddAssignment.as_view(), name='assignment-add'),
    path('<int:pk>/edit/', EditAssignment.as_view(), name='assignment-edit'),
]

app_name = "assignments"