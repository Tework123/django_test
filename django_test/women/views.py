from django.shortcuts import render


def women(request):
    return render(request, 'women/women.html', {'title': 'about'})


def about(request):
    return render(request, 'women/one_men.html', {'title': 'about'})
