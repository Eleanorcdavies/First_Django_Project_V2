from django.contrib import admin
from .models import Student, School, Certificate_type, Grade, Department, Faculty
# Register your models here.

admin.site.register(Student)
admin.site.register(School)
admin.site.register(Certificate_type)
admin.site.register(Grade)
admin.site.register(Department)
admin.site.register(Faculty)
