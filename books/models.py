from django.db import models


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

