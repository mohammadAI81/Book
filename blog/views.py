from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog, Comment

def blogs(request):
    blogs = Blog.objects.filter(status = 'pd').order_by('-datetime_created').all()

    context = {
        'blogs': blogs,
    }
    return render(request, 'blog/blogs.html', context)

def detail(request, num):
    blog = get_object_or_404(Blog, id=num)
    
    
    return

def create(request):
    
    return 

def edit(request, name):
    blog = get_object_or_404(Blog, title=name)
    
    
    return 

def delete(request, name):
    
    return 
