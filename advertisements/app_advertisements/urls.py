from .views import index, top_sellers, advertisement_post, advertisement_detail
from django.urls import path


urlpatterns = [
    path('',index,name='main-page'),
    path('top-sellers/', top_sellers, name = 'top-sellers'),
    path('advertisement-post/',advertisement_post, name='adv-post'),
    path('advertisement/<int:pk>',advertisement_detail, name='adv-detail')
]