from django.db import models
from django.contrib.auth import get_user_model


class Blog(models.Model):
    STATUS_PUB = 'pd'
    STATUS_DRA = 'dr'
    STATUS = (
        (STATUS_PUB, 'Published'),
        (STATUS_DRA, 'Draft'),
    )

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='auhtor_blog',
                               null=True)
    photo = models.FileField(upload_to='blog/cover/%Y/%m', blank=True)
    title = models.CharField(max_length=255)
    discription = models.TextField()
    status = models.CharField(default=STATUS_PUB, choices=STATUS, max_length=2)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_comments')
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comments', null=True)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.text[:15]
