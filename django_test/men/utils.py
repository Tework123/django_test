from django.db.models import Count

from .models import Men, Category


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        count_mens_from_category = Category.objects.annotate(count_mens=Count('men__id'))
        context['count_mens_from_category'] = count_mens_from_category
        # вырезание поля словаря, если пользователь не авторизован
        if not self.request.user.is_authenticated:
            print('hello dodik')
        # mens = Men.objects.all()
        # print(mens)
        # context['mens'] = mens

        return context
