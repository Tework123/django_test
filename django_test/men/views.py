from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect

from men.models import Men, Category


# main page
def main(request):
    mens = Men.objects.all()
    context = {'title': 'main', 'mens': mens}
    return render(request, 'men/main.html', context)


def men(request):
    mens = Men.objects.all()

    return render(request, 'men/men.html', {'title': 'men', 'mens': mens})


def categories_mens(request):
    categories = Category.objects.all()
    return render(request, 'men/categories_mens.html', {'title': 'categories_mens', 'categories': categories})


def one_men(request, men_id):
    men = Men.objects.filter(pk=men_id)
    print(men)
    return render(request, 'men/one_men.html', {'title': 'one_men', 'men': men})


def about(request):
    mens = Men.objects.all()
    return render(request, 'men/main.html', {'title': 'about', 'mens': mens})


def add_page(request):
    mens = Men.objects.all()
    return render(request, 'men/main.html', {'title': 'add_page', 'mens': mens})


def contact(request):
    mens = Men.objects.all()
    return render(request, 'men/main.html', {'title': 'contact', 'mens': mens})


# def men(request, men_id):
#     print(men_id)
#     print(request.GET)
#     if request.POST:
#         print(request.POST)
#     return HttpResponse(f'Страница приложения men{men_id}')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Я не нашел страничку сори мен')
