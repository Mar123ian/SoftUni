from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.ShowAllBooks.as_view(), name='show_all_books'),
    path('add/', views.AddBook.as_view(), name='add_book'),
    path('edit/<pk>', views.EditBook.as_view(), name='edit_book'),
    path('delete/<pk>', views.DeleteBook.as_view(), name='delete_book'),
    path('<slug:book_slug>/', views.ShowBook.as_view(), name='show_book'),

    ]