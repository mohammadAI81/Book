from django.shortcuts import render

from blog.models import Blog, Comment
from books.models import Book


def home(request):
    blogs = Blog.objects.filter(status='pd').order_by('-datetime_created').all()[:3]
    books = Book.objects.all()
    
    context = {
        'blogs': blogs,
        'books': books
    }
    
    return render(request, 'pages/home.html', context)


def about(request):
    
    return render(request, 'pages/about.html')


def contact(request):
    
    return render(request, 'pages/contact.html')


def search(request):
    blogs = Blog.objects.order_by('-datetime_created')
    books = Book.objects.order_by('-datetime_created')

    if request.method == 'GET':
        # Get data
        search_user = request.GET['s']

        books = books.filter(title__icontains=search_user)
        blogs = blogs.filter(title__icontains=search_user)

    context = {
        'books': books,
        'blogs': blogs,
        'value': request.GET
    }

    return render(request, 'pages/search.html', context)
