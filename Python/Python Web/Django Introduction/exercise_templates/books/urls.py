from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.show_all_books, name='show_all_books'),
    path('<slug:book_slug>/', views.show_book, name='show_book')
    ]