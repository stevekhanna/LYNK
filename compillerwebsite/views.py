from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .models import Student, Assignment, Feedback, Grade


def home(request):
    context = {
        'all_students': Student.objects.all()
    }

    return render(request, 'parentHome.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def attendance(request):
    context = {
        'attendance': Student.objects.all()
    }

    return render(request, '../templates/parentAttendance.html', context)


def feedback(request):
    context = {
        'feedback': Student.objects.all()
    }

    return render(request, '../templates/parentFeedback.html', context)


def grades(request):
    context = {
        'grade': Student.objects.all()
    }

    return render(request, '../templates/parentGrades.html', context)


def agenda(request):
    context = {
        'agenda': Student.objects.all()
    }

    return render(request, 'parentAgenda.html', context)


def student_feedback(request, id):
    feedbacks = Feedback.objects.filter(id=id)

    context = {
        'feedback': feedbacks
    }

    return render(request, 'parentFeedback.html', context)


def student_grades(request, id):
    grades = Grade.objects.filter(id=id)

    context = {
        'grades': grades
    }

    return render(request, 'parentGrades.html', context)

@login_required
def profile(request):
    return render(request, 'parentHome.html')

