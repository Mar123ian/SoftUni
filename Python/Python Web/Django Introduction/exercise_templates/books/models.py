from django.db import models
from django.utils.text import slugify
from django.core.validators import MinLengthValidator


class Book(models.Model):
    class Genre(models.TextChoices):
        FICTION = "Fiction", "Fiction"
        NON_FICTION = "Non-Fiction", "Non-Fiction"
        FANTASY = "Fantasy", "Fantasy"
        SCIENCE = "Science", "Science"
        HISTORY = "History", "History"
        OTHER = "Other", "Other"

    title = models.CharField(
        max_length=255,
        unique=True
    )

    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )

    isbn = models.CharField(
        max_length=12,
        unique=True,
        validators=[MinLengthValidator(12)]
    )

    genre = models.CharField(
        max_length=20,
        choices=Genre.choices
    )

    publishing_date = models.DateField()

    description = models.TextField()

    image_url = models.URLField()

    slug = models.SlugField(
        max_length=255,
        unique=True,
        blank=True
    )

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


