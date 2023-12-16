from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment, Blog

@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'status', 'datetime_created')    
    list_display_links = ('title',)
    list_editable = ('status',)
    list_per_page = 15
    ordering = ('title',)
    fieldsets = (
        ('Import Fields', {'fields': ('title', 'discription', 'status')}),
        ('Other Fields', {'fields': ('datetime_created', 'datetime_modified')}),
    )
    readonly_fields = ('datetime_created', 'datetime_modified')


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('author', 'book', 'datetime_created')
    list_editable = ('book',)
    list_per_page = 15
    ordering = ('book',)
    fieldsets = (
        ('Import Fields', {'fields': ('author', 'book', 'text')}),
        ('Other Fields', {'fields': ('datetime_created', 'datetime_modified')}),
    )
    readonly_fields = ('datetime_created', 'datetime_modified')
    