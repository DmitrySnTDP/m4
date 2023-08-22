from .views import index, top_sellers
from django.urls import path


urlpatterns = [
    path('',index,name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('index/',index, name='index'),
]