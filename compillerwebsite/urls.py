from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.home, name='index'),
    path('parentAttendance/', views.attendance, name='attendance'),
    path('parentFeedback/', views.feedback, name='feedback'),
    path('parentGrades/', views.grades, name='grades'),
    path('p/', views.announcements, name='announcements'),
    path('p/', views.agenda, name='agenda'),
]
