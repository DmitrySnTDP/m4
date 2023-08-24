from .views import index, top_sellers, advertisement_post
from django.urls import path


urlpatterns = [
    path('',index,name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('index/',index, name='index'),
    path('advertisement-post/',advertisement_post, name='adv-post')
]