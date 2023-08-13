from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Men, Category


# эти классы для изменения полей админки
class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}
    # для изменения полей будут отображаться эти:
    fields = ('title', 'slug', 'content', 'photo', 'is_published', 'category','time_create', 'get_html_photo')
    # неизменяемые поля надо сначала сюда добавить
    readonly_fields = ('time_create', 'get_html_photo')

    # добавляем фоточки в админку, название функции сами придумали, потом надо его в
    # list_display прописать, object - объект класса Men, у каждого ищется фото, если нет -
    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Мини фоточка'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Men, MenAdmin)
admin.site.register(Category, CategoryAdmin)

# изменение заголовков админки
admin.site.site_title = 'Админка не твоя'
admin.site.site_header = 'А что это тут у нас, админка дада'
# полный список в документации
