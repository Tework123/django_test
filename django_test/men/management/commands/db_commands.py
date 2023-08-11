import random

from django.core.management import BaseCommand
from faker import Faker

from men.models import Men, Category, Message


class Command(BaseCommand):
    help = 'hello everyone'

    def handle(self, *args, **kwargs):
        fake = Faker()

        categories = ['cs', 'dota', 'warcraft']
        categories_objects = []
        for i in categories:
            object = Category.objects.create(name=i)
            categories_objects.append(object)

        mens = ['dendi', 'happy', 'foggy', 'simons', 'miracle']
        mens_objects = []
        for i in mens:
            object = Men.objects.create(title=i, content=i,
                                        category=random.choices(categories_objects, k=1)[0])

            mens_objects.append(object)

        for i in range(20):
            object = Message.objects.create(text=fake.name(), men=random.choices(mens_objects, k=1)[0])

        print('***Commands complete***')
