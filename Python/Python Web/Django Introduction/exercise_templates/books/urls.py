from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.show_all_books, name='show_all_books'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<id>', views.edit_book, name='edit_book'),
    path('delete/<id>', views.delete_book, name='delete_book'),
    path('<slug:book_slug>/', views.show_book, name='show_book'),

    ]