from django.shortcuts import render

from .models import Student, Assignment, Feedback, Grade


def home(request):
    context = {
        'all_students': Student.objects.all()
    }

    return render(request, 'parentHome.html', context)


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
