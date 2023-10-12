from django.db import models
from django.urls import reverse


class Department(models.Model):
    dept_name = models.CharField(max_length=100)
    home_unit = models.CharField(max_length=50)

    def __str__(self):
        return '{}, {}'.format(self.dept_name, self.home_unit)


class WidgetUser(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
    
    def get_absolute_url(self):
        return reverse('dashboard:widgetuser-details', kwargs={'pk':self.pk})

