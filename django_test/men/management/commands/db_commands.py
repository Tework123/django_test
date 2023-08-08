import random

from django.core.management import BaseCommand

from men.models import Men, Category


class Command(BaseCommand):
    help = 'hello everyone'

    def handle(self, *args, **kwargs):
        categories = ['cs', 'dota', 'warcraft']
        categories_objects = []
        for i in categories:
            object = Category.objects.create(name=i)
            categories_objects.append(object)

        mens = ['dendi', 'happy', 'foggy', 'simons', 'miracle']
        for i in mens:
            Men.objects.create(title=i, content=i,
                               category=random.choices(categories_objects, weights=(1, 1, 1), k=1)[0])

        print('***Commands complete***')
