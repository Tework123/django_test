from django.db import models
from django.urls import reverse


class Men(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse('one_men', kwargs={'men_slug': self.slug})

    # для изменения имен групп
    class Meta:
        verbose_name = 'Известные мужчинки'
        verbose_name_plural = 'Известные мужчинки'

        # ordering = ['title', 'content']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='URL', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

        ordering = ['id']


# у чела много сообщений
class Message(models.Model):
    text = models.CharField(max_length=300)
    men = models.ForeignKey('Men', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.text
