from django.contrib import admin
from .models import Department, WidgetUser


class DepartmentAdmin(admin.ModelAdmin):
	model = Department
	list_display = ('dept_name', 'home_unit')


class WidgetUserAdmin(admin.ModelAdmin):
	model = WidgetUser
	list_display = ('first_name', 'middle_name','last_name','department')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(WidgetUser, WidgetUserAdmin)
