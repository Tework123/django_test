from django import template

from men.models import Category

register = template.Library()


# эту штуку надо подключать в html файл, треш ненужный
@register.simple_tag()
def get_categories():
    return Category.objects.all()
