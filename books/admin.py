from django.contrib import admin

from .models import Book, Comment


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'datetime_created')
    search_fields = ('title', )
    ordering = ('title',)
    list_per_page = 25


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('author', 'book', 'published', 'datetime_created')
    list_editable = ('book',)
    ordering = ('-datetime_created',)
    list_per_page = 25

