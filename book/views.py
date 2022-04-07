from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import Book, Author

# Create your views here.


def books(request):
    context = {
        'books': Book.objects.all(),
        'title': 'Книги',

    }
    return render(request, 'book/books.html', context)


def books_sorted_by_names(request):
    context = {
        'books': Book.objects.all().order_by('name'),
        'title': 'Книги, сортування за назвою А - Я'
    }
    return render(request, 'book/books.html', context)


def books_sorted_by_names_desc(request):
    context = {
        'books': Book.objects.all().order_by('-name'),
        'title': 'Книги, сортування за назвою Я - А'
    }
    return render(request, 'book/books.html', context)


def books_sorted_by_count(request):
    context = {
        'books': Book.objects.all().order_by('count'),
        'title': 'Книги, сортування за кількістю'
    }
    return render(request, 'book/books.html', context)


def book_by(request, bookid):

    context = {
        'book': Book.get_by_id(bookid),
        'authors': get_authors(Book.get_by_id(bookid).authors.all()),
    }
    return render(request, 'book/book.html', context)


def get_authors(authorslist):
    authors = [
        f'{author.surname} {author.name} {author.patronymic}' for author in authorslist]
    return ', '.join(authors)


def add_book(request):
    print('CREATE')
    if request.method == 'POST':
        form = AddBookPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = AddBookPostForm()
    return render(request, 'book/add_book.html', {'form': form})


def update_book(request, bookid):
    print('UPDATE')
    book = Book.objects.get(pk=bookid)
    form = AddBookPostForm(instance=book)
    if request.method == 'POST':
        print('POST')
        form = AddBookPostForm(request.POST, instance=book)
        if form.is_valid():
            print('VALID')
            form.save()
            return redirect('books')
    return render(request, 'book/add_book.html', {'form': form})

# def add_book(request, bookid = 0):
#
#    if request.method == 'GET':
#        if bookid == 0:
#            form = AddBookPostForm()
#        else:
#            book = Book.objects.get(pk=bookid)
#            form = AddBookPostForm(instance=book)
#        return render(request, 'book/add_book.html', {'form':form})
#    else:
#        if bookid == 0:
#            form = AddBookPostForm(request.POST)
#        else:
#            book = Book.objects.get(pk=bookid)
#            form = AddBookPostForm(request.POST, instance=book)
#        if form.is_valid():
#            form.save()
#        return redirect('books')
#   return render(request, 'book/add_book.html', {'form': form})
