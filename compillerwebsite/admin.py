from django.contrib import admin
from .models import Student, NewsArticle, Assignment, Style

admin.site.register(Student)
admin.site.register(NewsArticle)
admin.site.register(Assignment)
admin.site.register(Style)