from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import auth_login

urlpatterns = [

    path('', views.home, name='index'),
    path('parentAttendance/', views.attendance, name='attendance'),
    path('parentFeedback/', views.feedback, name='feedback'),
    path('parentGrades/', views.grades, name='grades'),
    path('parentAgenda/', views.agenda, name='agenda'),
    url(r'^student_feedback/(?P<id>\d+)/$', views.student_feedback, name='student_feedback'),
    url(r'^student_grade/(?P<id>\d+)/$', views.student_grades, name='student_grade'),
]
