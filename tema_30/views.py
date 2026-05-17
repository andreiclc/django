from django.shortcuts import render, redirect
from datetime import datetime, timezone
from tema_30.models import Book
from root import CONST


def add_books(request):
    books = [
        {
            'name': 'Dune',
            'author': 'Frank Herbert',
            'release_date': datetime(1965, 8, 1, tzinfo=timezone.utc)
        },
        {
            'name': 'Harry Potter',
            'author': 'J.K. Rowling',
            'release_date': datetime(1997, 6, 26, tzinfo=timezone.utc)
        },
        {
            'name': 'Lord of the Rings',
            'author': 'J.R.R. Tolkien',
            'release_date': datetime(1954, 7, 29, tzinfo=timezone.utc)
        },
        {
            'name': 'Mistborn: The Final Empire',
            'author': 'Brandon Sanderson',
            'release_date': datetime(2006, 7, 17, tzinfo=timezone.utc)
        },
        {
            'name': 'The Witcher: The Last Wish',
            'author': 'Andrzej Sapkowski',
            'release_date': datetime(1993, 1, 1, tzinfo=timezone.utc)
        },
    ]

    for book in books:
        Book.objects.create(**book)

    return redirect('books')


def books(request):
    """randare template exercitiu.html."""
    all_books = Book.objects.all()
    context = {
        'titlu': CONST['nr_tema_30'],
        'version': CONST['version'],
        'books': all_books,
    }
    return render(request, 'tema_30/exercitiu.html', context)







