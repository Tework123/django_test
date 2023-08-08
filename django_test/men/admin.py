from django.contrib import admin

from .models import Men, Category


# эти классы для изменения полей админки
class MenAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Men, MenAdmin)
admin.site.register(Category, CategoryAdmin)
