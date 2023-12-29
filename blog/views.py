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
    comments = blog.book_comments.all()
    
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
            if title and discription and status:
                blog = Blog.objects.create(title=title, discription=discription, status=status)
                return redirect('detail_blog', blog.id)
            else:
                return redirect('list_blog')
    
    
    return render(request, 'blog/create_edit.html')

def edit(request, name):
    blog = get_object_or_404(Blog, title=name)
    
    if request.method == 'POST':
        title = request.POST['title']
        discription = request.POST['discription']
        status = request.POST['status']
        Blog.objects.update(title=title, discription=discription, status=status)
        return redirect('detail_blog', blog.id)
    
    
    context = {
        'blog': blog
    }
    
    return render(request, 'blog/create_edit.html', context)

def delete(request, name):
    blog = get_object_or_404(Blog, title=name)
    if request.method == 'POST':
        status = request.POST['status']
        if status == 'Yes':
            blog.delete()
            return redirect('list_blog')
        else:
            return redirect('list_blog')
        
        
    context = {
        'blog': blog
    }
    
    return render(request, 'blog/delete.html', context)
