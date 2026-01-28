from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import AddBookForm, UpdateBookForm, DeleteBookForm

# Create your views here.
def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})


def show_book(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    return render(request, 'book_full_info.html', {'book': book})

def add_book(request):
    form = AddBookForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('show_all_books')

    return render(request, 'add_book.html', {'form': form})

def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = UpdateBookForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('show_all_books')

    return render(request, 'edit_book.html', {'form': form})

def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = DeleteBookForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('show_all_books')

    return render(request, 'delete_book.html', {'form': form})
