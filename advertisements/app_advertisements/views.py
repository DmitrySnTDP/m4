from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    advertisements = advertisements.objects.all()
    context = {'advertisements':advertisements}
    return render(request, 'index.html', context)


def lessonFour(request):
    return HttpResponse('Урок номер 4')


def top_sellers(request):
    return render(request, 'top-sellers.html')