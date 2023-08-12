from django.urls import path

from .views import authentication, login, register, Register, Login

urlpatterns = [
    path('', authentication, name='authentication'),
    # path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
]
