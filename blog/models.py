from django.db import models
from django.conf import settings


class Blog(models.Model):
    STATUS_PUB = 'pd'
    STATUS_DRA = 'dr'
    STATUS = (
        (STATUS_PUB, 'Published'),
        (STATUS_DRA, 'Draft'),
    )
    
    # photo
    title = models.CharField(max_length=255)
    discription = models.TextField()
    status = models.CharField(default='pd', choices=STATUS, max_length=2)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='auhtor_comments')
    book = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='book_comments')
    text = models.TextField()
    datetime_create = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text[:15]
