from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Успешно')


def lessonFour(request):
    return HttpResponse('Урок номер 4')