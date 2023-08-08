from django.urls import path

from .views import authentication, login, register

urlpatterns = [
    path('', authentication, name='authentication'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),

]
