# Generated by Django 4.2.4 on 2023-08-08 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_category_men_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['id'], 'verbose_name': 'Категории', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='men',
            options={'ordering': ['title', 'content'], 'verbose_name': 'Известные мужчинки', 'verbose_name_plural': 'Известные мужчинки'},
        ),
        migrations.AlterField(
            model_name='men',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Заголовок'),
        ),
    ]
