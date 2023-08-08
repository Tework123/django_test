from django.db import models


class Men(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    # для изменения имен групп
    class Meta:
        verbose_name = 'Известные мужчинки'
        verbose_name_plural = 'Известные мужчинки'

        ordering = ['title', 'content']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категории'
        verbose_name_plural = 'Категории'

        ordering = ['id']
