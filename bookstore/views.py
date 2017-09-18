from django.shortcuts import render

from .models import Author, Book

def index(request):
    """
    This is the base index page.
    """
    authors_count = Author.objects.count()
    books_count = Book.objects.count()

    return render(request, "bookstore/index.html", context={
        "authors_count": authors_count,
        "books_count": books_count
    })
