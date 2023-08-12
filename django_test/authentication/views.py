from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from authentication.forms import RegisterForm, LoginForm


class Register(CreateView):
    form_class = RegisterForm

    template_name = 'authentication/register.html'
    success_url = reverse_lazy('men')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('men')


class Login(LoginView):
    form_class = LoginForm
    template_name = 'authentication/login.html'

    # лучше прописать в settings перенаправление после успешного входа
    # def get_success_url(self):
    #     return reverse_lazy('main')


def logout_user(request):
    logout(request)
    return redirect('login')


def authentication(request):

    return render(request, 'authentication/authentication.html', {'title': 'authentication'})
