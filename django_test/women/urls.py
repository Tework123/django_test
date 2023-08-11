from django.urls import path

from .views import women

urlpatterns = [
    path('', women, name='women'),
    # path('about/', about, name='about'),

]
