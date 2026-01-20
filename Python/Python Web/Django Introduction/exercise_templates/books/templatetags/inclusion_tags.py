from django import template
from books.models import Book

register = template.Library()

@register.inclusion_tag('book_short_info.html')
def books_short_info(book):
    return {'book': book}
