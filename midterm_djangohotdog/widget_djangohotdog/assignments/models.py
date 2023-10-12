from django.db import models

# Create your models here.


class Course(models.Model):
    code = models.CharField(max_length = 10)
    title = models.CharField(max_length = 50)
    section = models.CharField(max_length = 3)
    
    def __str__(self):
        return "{}-{}".format(self.code, self.section)
    
    def get_absolute_url(self):
        return str(self.pk)
    
    
class Assignment(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 200)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    perfect_score = models.IntegerField(default = 0)
    passing_score = models.IntegerField(default = 0, editable = False)
    
    def save(self, *args, **kwargs):
        if self.perfect_score > 0:
            self.passing_score = self.perfect_score * 0.6
        super().save(*args, **kwargs)
    
    def __str__(self):
        return "\
            Assignment Name: {} <br>\
            Description: {} <br>\
            Perfect Score: {} <br>\
            Passing Score: {} <br>\
            Course/Section: {} <br>\
            ".format(
            self.name, self.description, self.perfect_score, 
            self.passing_score, self.course
            )
    
    def get_absolute_url(self):
        return str(self.pk)
    