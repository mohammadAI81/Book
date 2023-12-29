from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment, Blog

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'status', 'datetime_created')    
    list_editable = ('status',)
    list_filter = ('status',)
    list_per_page = 20
    ordering = ('title',)
    readonly_fields = ('datetime_created', 'datetime_modified')


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('author', 'book', 'datetime_created')
    list_editable = ('book',)
    list_per_page = 25
    ordering = ('book',)
    readonly_fields = ('datetime_created', 'datetime_modified')
    