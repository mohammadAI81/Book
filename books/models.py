from django.db import models
from django.contrib.auth import get_user_model


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='book_author')
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='book/cover/%Y/%m', null=True, blank=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='comment_author')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comment_book', blank=True, null=True)
    author_book = models.ForeignKey(Author, on_delete=models.PROTECT, blank=True, null=True)
    text = models.TextField()
    published = models.BooleanField(default=False)
    datetime_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book.title
