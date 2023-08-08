from django.shortcuts import render


def authentication(request):
    return render(request, 'authentication/authentication.html', {'title': 'authentication'})


def login(request):
    pass


def register(request):
    pass
