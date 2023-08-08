from django.urls import path

from .views import about, contact, men, one_men, categories_mens

urlpatterns = [
    path('', men, name='men'),
    path('<int:men_id>/', one_men, name='one_men'),
    path('categories_mens/', categories_mens, name='categories_mens'),

    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add_page/', contact, name='contact'),
]
