from django.contrib.auth import views as auth_views
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('', views.register, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('parentHome/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('parentAttendance/', views.attendance, name='attendance'),
    path('parentFeedback/', views.feedback, name='feedback'),
    path('parentGrades/', views.grades, name='grades'),
    path('parentAgenda/', views.agenda, name='agenda'),
    url(r'^student_feedback/(?P<id>\d+)/$', views.student_feedback, name='student_feedback'),
    url(r'^student_grade/(?P<id>\d+)/$', views.student_grades, name='student_grade'),
]
