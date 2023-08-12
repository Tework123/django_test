from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from men.models import Men


class RegisterForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Нейм хочу', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль не хочу', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    # class Meta:
    #     model = User
    #     fields = ('username', 'password1', 'password2', 'email')
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-input'}),
    #     }
