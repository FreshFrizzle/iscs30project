from django.contrib import admin
from .models import Course, Assignment

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    model = Course

class AssignmentAdmin(admin.ModelAdmin):
    model = Assignment
    
    list_display = ("name", "description", "perfect_score", "passing_score", "course")
    
admin.site.register(Course, CourseAdmin)
admin.site.register(Assignment, AssignmentAdmin)