from django.urls import path

from .views import about, contact, categories_mens, MenPage, OneMenPage, AddPage, message, get_whole_message_men

urlpatterns = [
    path('', MenPage.as_view(), name='men'),
    # path('<int:men_id>/', OneMenPage.as_view(), name='one_men'),
    path('add_page/', AddPage.as_view(), name='add_page'),
    # path('<int:men_id>/', one_men, name='one_men'),
    # path('<slug:men_slug>/', one_men, name='one_men'),
    path('categories_mens/', categories_mens, name='categories_mens'),
    path('message/', message, name='message'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('<int:men_id>/', get_whole_message_men, name='get_whole_message_men')
    # path('add_page/', add_page, name='add_page'),
]
