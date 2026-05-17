from django.shortcuts import render, redirect
from datetime import datetime, timezone
from tema_30.models import Book
from tema_30.forms import BookForm
from root import CONST


def add_books(request):
    """populare tabela book."""

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


def delete_books(request):
    """eliminare date din tabele book."""

    Book.objects.all().delete()
    return redirect('books')


def books_after_2000(request):
    """afisare carti publicate dupa anul 2000."""

    all_books = Book.objects.filter(release_date__year__gt=2000)
    context = {
        'titlu': CONST['nr_tema_30'],
        'version': CONST['version'],
        'books': all_books,
    }
    return render(request, 'tema_30/exercitiu.html', context)


def edit_book(request, pk):
    """
        - editare nume carte
        - validare input name.
    """

    book = Book.objects.get(id=pk)

    if request.method == "POST":
        form = BookForm(request.POST)

        if form.is_valid():
            book.name = form.cleaned_data['name']
            book.save()
            return redirect('books')
        
    else:
        form = BookForm()

    context = {
        'titlu': CONST['nr_tema_30'],
        'version': CONST['version'],
        'book': book,
        'form': form,
    }
    return render(request, 'tema_30/edit_book.html', context)


def books(request):
    """randare template exercitiu.html."""
    
    all_books = Book.objects.all()
    books_2000 = Book.objects.filter(release_date__year__gt=2000)
    context = {
        'titlu': CONST['nr_tema_30'],
        'version': CONST['version'],
        'books': all_books,
        'books_2000': books_2000,
    }
    return render(request, 'tema_30/exercitiu.html', context)
