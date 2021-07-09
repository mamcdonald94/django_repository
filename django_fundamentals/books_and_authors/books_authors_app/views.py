from django.shortcuts import render, redirect
from .models import Book, Author


def books(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book.html', context)

def create_book(request):
    Book.objects.create(
        title = request.POST['title'],
        desc = request.POST['description']
    )
    return redirect('/books')

def one_book(request, id):
    context = {
        'one_book': Book.objects.get(id=id),
        'authors': Author.objects.all()
    }
    return render(request, 'show_book.html', context)

def add_author(request):
    this_book = Book.objects.get(id=request.POST['book'])
    this_author = Author.objects.get(id=request.POST['author'])

    this_book.authors.add(this_author) # from book side
    # this_author.books.add(this_book) from author side
    return redirect(f'/books/{this_book.id}')

def authors(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'author.html', context)

def create_author(request):
    Author.objects.create(
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        notes = request.POST['notes']
    )
    return redirect('/authors')    

def one_author(request, id):
    context = {
        'one_author': Author.objects.get(id=id),
        'books': Book.objects.all()
    }
    return render(request, 'show_author.html', context)

def add_book(request):
    this_book = Book.objects.get(id=request.POST['book'])
    this_author = Author.objects.get(id=request.POST['author'])

    this_author.books.add(this_book)
    return redirect(f'/authors/{this_author.id}')