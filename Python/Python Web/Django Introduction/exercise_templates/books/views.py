from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, FormView, DetailView, UpdateView, DeleteView, ListView

from .models import Book
from .forms import AddBookForm, UpdateBookForm, DeleteBookForm, SearchBookAndFilterForm
from reviews.forms import AddReviewForm
from reviews.utils import save_review_for_book

# Create your views here.
def show_all_books(request):
    books = Book.objects.all()
    return render(request, 'all_books.html', {'books': books})

class ShowAllBooks(ListView):
    template_name = 'all_books.html'
    model = Book
    context_object_name = 'books'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        self.form = SearchBookAndFilterForm(self.request.GET)

        if self.form.is_valid():
            query = self.form.cleaned_data['search_query'].strip()
            genre = self.form.cleaned_data['genre']

            if genre:
                queryset = queryset.filter(genre=genre)

            if query:
                queryset = queryset.filter(title__icontains=query)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context


def show_book(request, book_slug):
    book = Book.objects.get(slug=book_slug)
    form = AddReviewForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        save_review_for_book(form, book)
        return redirect('show_book', book_slug)

    return render(request, 'book_full_info.html', {'book': book, 'form': form})

class ShowBook(DetailView, FormView):
    model = Book
    template_name = 'book_full_info.html'
    slug_field = 'slug'
    slug_url_kwarg = 'book_slug'
    form_class = AddReviewForm

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)

    def get_success_url(self):
        return self.request.path

    def form_valid(self, form):
        save_review_for_book(form, self.object)
        return super().form_valid(form)

class AddBook(CreateView):
    model = Book
    template_name = 'add_book.html'
    form_class = AddBookForm
    success_url = reverse_lazy('show_all_books')

def add_book(request):
    form = AddBookForm(request.POST or None, request.FILES or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('show_all_books')

    return render(request, 'add_book.html', {'form': form})



def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = UpdateBookForm(request.POST or None, request.FILES or None,instance=book)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('show_all_books')

    return render(request, 'edit_book.html', {'form': form})

class EditBook(UpdateView):
    model = Book
    template_name = 'edit_book.html'
    form_class = UpdateBookForm
    success_url = reverse_lazy('show_all_books')

class DeleteBook(DeleteView):
    model = Book
    template_name = 'delete_book.html'
    success_url = reverse_lazy('show_all_books')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DeleteBookForm(instance=self.get_object())
        return context





def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    form = DeleteBookForm(request.POST or None, instance=book)

    if request.method == 'POST' and form.is_valid():
        book.delete()
        return redirect('show_all_books')

    return render(request, 'delete_book.html', {'form': form})



