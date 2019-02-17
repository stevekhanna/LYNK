from django.shortcuts import render

#from .models import Member, Research, Publication, NewsArticle, Opportunity, Style


def home(request):

    return render(request, '../templates/index.html')