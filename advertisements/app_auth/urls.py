
from django.urls import path
from .views import profile_view, login_view, logout



urlpatterns = [
    path('profile/',profile_view,name='profile'),
    path('login/', login_view, name = 'login'),
    path('logout/',logout , name='logout')
]