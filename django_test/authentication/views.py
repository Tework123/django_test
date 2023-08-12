from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import RegisterForm


class Register(CreateView):
    form_class = RegisterForm
    print(form_class)

    template_name = 'authentication/register.html'
    success_url = reverse_lazy('authentication')



class Login:
    pass


def authentication(request):
    return render(request, 'authentication/authentication.html', {'title': 'authentication'})


def login(request):
    pass


def register(request):
    pass
