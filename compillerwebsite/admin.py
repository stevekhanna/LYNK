from django.contrib import admin
from .models import Student, Assignment, Feedback, Grade

admin.site.register(Student)
admin.site.register(Assignment)
admin.site.register(Feedback)
admin.site.register(Grade)
