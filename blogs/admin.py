from django.contrib import admin

from .models import Article, ListItem, CountdownItem


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
admin.site.register(Article, ArticleAdmin)


class ListItemAdmin(admin.ModelAdmin):
    list_display = (u'id', 'item', 'title', 'description', 'pic')
    list_filter = ('item',)
admin.site.register(ListItem, ListItemAdmin)


class CountdownItemAdmin(admin.ModelAdmin):
    list_display = (u'id', 'countdown', 'title', 'description', 'pic')
    list_filter = ('countdown',)
admin.site.register(CountdownItem, CountdownItemAdmin)

