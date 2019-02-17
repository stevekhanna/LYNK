from django.shortcuts import render

#from .models import Member, Research, Publication, NewsArticle, Opportunity, Style


def home(request):

    return render(request, '../templates/index.html')

def attendance(request):

    return render(request, '../templates/parentAttendance.html')

def feedback(request):

    return render(request, '../templates/parentFeedback.html')

def grades(request):

    return render(request, '../templates/parentGrades.html')

def announcements(request):

    return render(request, '../templates/parentAnnouncements.html')

def agenda(request):

    return render(request, '../templates/parentAgenda.html')