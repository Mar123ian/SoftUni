from django.shortcuts import render
from .models import Book

# Create your views here.
def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def show_book(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    return render(request, 'book_full_info.html', {'book': book})