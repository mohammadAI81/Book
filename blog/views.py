import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Blog, Comment


def blogs(request):
    blog = Blog.objects.filter(status='pd').order_by('-datetime_created')

    context = {
        'blogs': blog,
    }
    return render(request, 'blog/blogs.html', context)


@login_required(login_url='/account/login/')
def detail(request, num):
    blog = get_object_or_404(Blog, id=num)
    comments = blog.blog_comments.all()
    
    if request.method == 'POST':
        if request.user.is_authenticated:
            user_comment = request.user
            blog_comment = blog
            text_comment = request.POST['comment']
            if user_comment and text_comment and blog_comment:
                comment = Comment(author=user_comment, book=blog_comment, text=text_comment)
                comment.save()
                return redirect('list_blog')
            else:
                return redirect('detail_blog', blog.id)
        else:
            return redirect('detail_blog', blog.id)
    
    context = {
        'blog': blog,
        'comments': comments,
    }
    
    return render(request, 'blog/blog.html', context)


def create(request):
    
    if request.method == 'POST':
        
        if request.user.is_authenticated:
            title = request.POST['title']
            discription = request.POST['discription']
            status = request.POST['status']
            author = request.user
            if title and discription and status:
                blog = Blog(title=title, discription=discription, status=status, author=author)
                if request.FILES:
                    blog.photo = request.FILES['picture']
                blog.save()
                return redirect('detail_blog', blog.id)
            else:
                return redirect('create_blog')

    return render(request, 'blog/create_edit.html')


def edit(request, num):
    blog = get_object_or_404(Blog, id=num)
    if request.method == 'POST':
        if request.FILES:
            if blog.photo:   
                blog.photo.delete()
                os.remove(blog.photo.path)
            blog.photo = request.FILES['picture']
        blog.title = request.POST['title']
        blog.discription = request.POST['discription']
        blog.status = request.POST['status']
        blog.save()
        return redirect('detail_blog', blog.id)

    context = {
        'blog': blog
    }
    
    return render(request, 'blog/create_edit.html', context)


def delete(request, num):
    blog = get_object_or_404(Blog, id=num)
    if request.method == 'POST':
        status = request.POST['status']
        if status == 'Yes':
            if blog.photo:
                os.remove(blog.photo.path)
            blog.delete()
            return redirect('list_blog')
        else:
            return redirect('list_blog')

    context = {
        'blog': blog
    }
    
    return render(request, 'blog/delete.html', context)
