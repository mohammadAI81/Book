from django.db import models
from django.conf import settings
from datetime import datetime

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
    status = models.CharField(default=STATUS_PUB, choices=STATUS, max_length=2)
    datetime_created = models.DateTimeField(auto_now_add=True, null=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, related_name='auhtor_comments')
    book = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='book_comments')
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True, null=True)
    datetime_modified = models.DateTimeField(auto_now=True, null=True)
    
    def __str__(self):
        return self.text[:15]
