from django.db import models
from django.db.models.base import Model

# Create your models here.

# School Models

# In the One-to-many, the student is the One
class Student(models.Model):
    fullname = models.CharField(max_length= 100)
    year_of_graduation = models.IntegerField()
    



# In the One-to-many, these are the "Many"" attributes, the student is the "One"
# I chose to protect these classes so you don't get confused when deleting
class School(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length = 100, default = "default_school_name")

class Certificate_type(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length = 100)

#Grade as in the letter grade of their class as it is a many to one, meaning it can't be their year in school because one student can only be in one grade. Therefore, it is the letter grade of their classes.

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    type = models.CharField(max_length = 100)

class Department(models.Model):
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    name = models.CharField(max_length = 100)
    faculty = models.CharField(max_length= 100)

class Faculty(models.Model):
    name = models.CharField(max_length = 100)



