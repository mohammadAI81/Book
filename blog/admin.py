from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment, Blog


class CommentBlog(admin.TabularInline):
    model = Comment
    fields = ['author', 'text']
    extra = 1



@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    list_display = ('title', 'author', 'status', 'datetime_created')    
    list_editable = ('status',)
    list_filter = ('status',)
    list_per_page = 20
    ordering = ('title',)
    readonly_fields = ('datetime_created', 'datetime_modified')
    
    inlines = [
        CommentBlog,
    ]


@admin.register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('author', 'blog', 'datetime_created')
    list_editable = ('blog',)
    list_per_page = 25
    ordering = ('blog',)
    readonly_fields = ('datetime_created', 'datetime_modified')
    