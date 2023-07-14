from .views import index, lessonFour
from django.urls import path


urlpatterns = [
    path('',index),
    path('lesson4/',lessonFour)
]