from django.shortcuts import render

from .models import Student, NewsArticle, Assignment


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


def announcements(request):
    context = {
        'announcement': NewsArticle.objects.first()
    }

    return render(request, '../templates/parentAnnouncements.html', context)


def agenda(request):
    context = {
        'agenda': Student.objects.all()
    }

    return render(request, '../templates/parentAgenda.html', context)
