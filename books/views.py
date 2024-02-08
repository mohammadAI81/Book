import os

from django.shortcuts import render, redirect, get_object_or_404

from .models import Book, Comment, Author


def books(request):
    book = Book.objects.order_by('-datetime_created').all()

    context = {
        'books': book,
    }
    return render(request, 'books/books.html', context)


def create(request):
    authors = Author.objects.all()
    if request.method == 'POST':
        author = Author.objects.get(name=request.POST['author'])
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        if author and title and description and price:
            book = Book(author=author, title=title, description=description, price=price)
            if picture := request.FILES:
                book.photo = picture
            book.save()
            return redirect('book_detail', book.id)
        else:
            return redirect('book_create')

    context = {
        'authors': authors
    }
    return render(request, 'books/create_edit.html', context)


def edit(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        author = request.POST['author']
        title = request.POST['title']
        description = request.POST['description']
        price = request.POST['price']
        if picture := request.FILES:
            book.photo.delete()
            os.remove(book.photo.path)
            book.photo = picture
        book.objects.update(author=author, title=title, description=description, price=price)
        return redirect('book_detail', book.id)

    context = {
        'book': book
    }
    return render(request, 'books/create_edit.html', context)


def detail(request, pk):
    book = get_object_or_404(Book, id=pk)
    comments = book.comment_book.all()
    context = {
        'book': book,
        'comments': comments
    }
    return render(request, 'books/book.html', context)


def delete(request, pk):
    book = get_object_or_404(Book, id=pk)
    if request.method == 'POST':
        if request.POST['status'] == 'yes':
            if book.photo:
                os.remove(book.photo.path)
            book.delete()
            return redirect('home')
    context = {
        'book': book.title
    }
    return render(request, 'books/delete.html', context)


def authors(request):
    author = Author.objects.order_by('-datetime_created').all()

    context = {
        'authors': author
    }

    return render(request, 'books/authors.html', context)


def author(request, pk):
    authorid = Author.objects.get(id=pk)

    context = {
        'author': authorid
    }

    return render(request, 'books/author.html', context)
