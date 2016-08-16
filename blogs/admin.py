from django.contrib import admin

from .models import Article, ListItem, CountdownItem


class ListItemAdmin(admin.StackedInline):
    model = ListItem


class CountdownItemAdmin(admin.StackedInline):
    model = CountdownItem


class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        u'id',
        'title',
        'text',
        'description',
        'pic',
        'pub_date',
        'author',
        'author_pic',
        'slug',
        'category',
        'is_approved',
    )
    list_filter = ('pub_date', 'is_approved')
    search_fields = ('slug',)
    inlines = [ListItemAdmin,CountdownItemAdmin]
admin.site.register(Article, ArticleAdmin)


