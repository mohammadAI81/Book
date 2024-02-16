from django.contrib import admin

from .models import Book, Author


@admin.register(Book)
class AdminBook(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'datetime_created')
    search_fields = ('title', )
    ordering = ('title',)
    list_per_page = 25


@admin.register(Author)
class AdminAuthor(admin.ModelAdmin):
    list_display = ('name', 'datetime_created',)
    ordering = ('-datetime_created',)
    list_per_page = 25
