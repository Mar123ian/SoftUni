from reviews.models import Review
from books.models import Book
from decimal import Decimal
from datetime import date

books_data = [
    {
        "title": "Django for Beginners",
        "price": Decimal("24.99"),
        "isbn": "123456789100",
        "genre": "Non-Fiction",
        "publishing_date": date(2023, 3, 10),
        "description": "A step-by-step guide to learning Django.",
        "image_url": "https://example.com/django.jpg",
        "reviews": [
            ("Ivan", "Много добра книга за начинаещи.", "4.80"),
            ("Maria", "Ясно обяснена и практична.", "4.60"),
        ],
    },
    {
        "title": "The Science of AI",
        "price": Decimal("34.50"),
        "isbn": "123456789101",
        "genre": "Science",
        "publishing_date": date(2022, 6, 15),
        "description": "Understanding artificial intelligence concepts.",
        "image_url": "https://example.com/ai.jpg",
        "reviews": [
            ("Petar", "Много информативна.", "4.90"),
            ("Elena", "Добро въведение в AI.", "4.50"),
        ],
    },
    {
        "title": "Fantasy Kingdom",
        "price": Decimal("19.99"),
        "isbn": "123456789102",
        "genre": "Fantasy",
        "publishing_date": date(2021, 9, 1),
        "description": "Epic fantasy adventure in a magical world.",
        "image_url": "https://example.com/fantasy.jpg",
        "reviews": [
            ("Georgi", "Страхотен свят!", "5.00"),
            ("Anna", "Много увлекателна.", "4.70"),
            ("Nikolay", "Чете се на един дъх.", "4.80"),
        ],
    },
    {
        "title": "Modern Science Explained",
        "price": Decimal("28.00"),
        "isbn": "123456789103",
        "genre": "Science",
        "publishing_date": date(2020, 11, 20),
        "description": "Explains modern scientific discoveries.",
        "image_url": "https://example.com/science.jpg",
        "reviews": [
            ("Viktor", "Много добре структурирана.", "4.40"),
        ],
    },
    {
        "title": "History of the World",
        "price": Decimal("31.75"),
        "isbn": "123456789104",
        "genre": "Non-Fiction",
        "publishing_date": date(2019, 5, 5),
        "description": "A journey through world history.",
        "image_url": "https://example.com/history.jpg",
        "reviews": [
            ("Daniela", "Много интересна.", "4.60"),
            ("Stoyan", "Подробна и полезна.", "4.30"),
        ],
    },
]

for book_data in books_data:
    reviews = book_data.pop("reviews")
    book = Book.objects.create(**book_data)

    for author, body, rating in reviews:
        Review.objects.create(
            author=author,
            body=body,
            rating=Decimal(rating),
            book=book
        )

print("✔ Базата е успешно напълнена с книги и отзиви")
