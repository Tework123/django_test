from django.urls import path

from .views import authentication, Register, Login, logout_user

urlpatterns = [
    path('', authentication, name='authentication'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),

]
