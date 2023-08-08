from django.urls import path

from .views import about, women

urlpatterns = [
    path('', women, name='women'),
    path('about/', about, name='about'),

]
