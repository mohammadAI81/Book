from django.shortcuts import render

from blog.models import Blog
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