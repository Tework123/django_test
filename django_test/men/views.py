from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.postgres.aggregates import StringAgg
from django.core.cache import cache
from django.db.models import CharField
from django.db.models.functions import Concat, Cast
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from men.forms import AddMen, ContactForm
from men.models import Men, Category, Message
from men.utils import DataMixin


# main page
def main(request):
    mens = Men.objects.all()
    context = {'title': 'main', 'mens': mens}
    return render(request, 'men/main.html', context)


class MenPage(DataMixin, ListView):
    paginate_by = 3
    model = Men
    template_name = 'men/men.html'
    context_object_name = 'object_list'
    # если не найдет нужные данные, то вернет 404
    allow_empty = False

    # передает только неизменяемые данные
    # extra_context = {'title': 'Men'}

    # для динамического контекста надо вот так делать, сюда и датамиксин входит:
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Men')
        context = dict(list(context.items()) + list(c_def.items()))
        return context

    # метод переопределяет стандартный sql запрос модели, related делает жадный запрос, то есть сразу
    # достаются все категории, тупо join
    def get_queryset(self):
        mens = cache.get('mens')

        if not mens:
            mens = Men.objects.filter(is_published=True).select_related('category')

        cache.set('mens', mens, 60)
        return mens


def categories_mens(request):
    categories = Category.objects.all()
    return render(request, 'men/categories_mens.html', {'title': 'categories_mens', 'categories': categories})


class OneMenPage(DetailView):
    model = Men
    template_name = 'men/one_men.html'
    # который будет в html итерироваться
    context_object_name = 'men'
    # меняем стандартное pk(в men.html) на мое кастомное men_id(в urls)
    pk_url_kwarg = 'men_id'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        # аналог current_user
        # print(self.request.user)
        #
        # print(self.kwargs['men_id'])
        # info_about_men = Men.objects.annotate(
        #     messages=StringAgg(Cast('message__text', output_field=CharField()), delimiter=', ')).filter(
        #     id=self.kwargs['men_id'])
        # context['info_about_men'] = info_about_men
        context['title'] = 'Men'
        print(context)

        return context

    def get_queryset(self):
        # аналог current_user
        print(self.request.user)
        print(self.kwargs['men_id'])

        # переопределили главный метод, но выводит один объект, так как DetailView
        return Men.objects.annotate(
            messages=StringAgg(Cast('message__text', output_field=CharField()), delimiter=', ')).filter(
            id=self.kwargs['men_id'])


def about(request):
    mens = Men.objects.raw('SELECT id, title FROM men_men')

    return render(request, 'men/about.html', {'title': 'about', 'mens': mens})


def message(request):
    messages = Message.objects.annotate(('men_id'))
    return render(request, 'men/one_men.html', {'title': 'message', 'messages': messages})


def get_whole_message_men(request, men_id):
    men = Men.objects.filter(pk=men_id).first()
    messages = Message.objects.filter(men=men_id)
    return render(request, 'men/one_men.html', {'title': 'message', 'messages': messages, 'men': men})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddMen
    template_name = 'men/add_page.html'
    # перенаправление для незарегистрированного пользователя
    login_url = reverse_lazy('main')
    # либо ошибка 403
    raise_exception = True
    # автоматическое перенаправление после добавление страницы
    success_url = reverse_lazy('men')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        extra_context = self.get_user_context(title='add_page')
        return dict(list(context.items()) + list(extra_context.items()))


# def add_page(request):
#     if request.method == 'POST':
#         print('post')
#         form = AddMen(request.POST, request.FILES)
#
#         if form.is_valid():
#             form.save()
#             # Men.objects.create(**form.cleaned_data)
#             return redirect('men')
#     else:
#         form = AddMen()
#
#     return render(request, 'men/add_page.html', {'title': 'add_page', 'form': form})

class Contact(FormView):
    form_class = ContactForm
    template_name = 'men/contact.html'
    success_url = reverse_lazy('men')

    # вызывается, если форма заполнена правильно, печатает то, что есть в форме и ридеректит
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('men')


def pageNotFound(request, exception):
    return HttpResponseNotFound('Я не нашел страничку сори мен')
