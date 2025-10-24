from django.db import models


# Create your models here.
class Book(models.Model):
    class Genre(models.TextChoices):
        FICTION = "fiction", "fiction"
        NON_FICTION = "non-fiction", "non-fiction"
        SCIENCE_FICTION = "science fiction", "science fiction"
        HORROR = "horror", "horror"

    title = models.CharField(max_length=30)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=20, choices=Genre.choices)
    publication_date = models.DateField(editable=False, auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    is_available = models.BooleanField(default=True)
    rating = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return self.title
