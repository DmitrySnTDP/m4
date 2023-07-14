from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')


def lessonFour(request):
    return HttpResponse('Урок номер 4')


def top_sellers(request):
    return render(request, 'top-sellers.html')