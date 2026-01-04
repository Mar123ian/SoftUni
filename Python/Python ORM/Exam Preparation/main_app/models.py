from django.core.validators import MinLengthValidator, MaxLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import Count


# Create your models here.
class DirectorManager(models.Manager):
    def get_directors_by_movies_count(self):
        return self.all().annotate(movies_count=Count('mv')).order_by('-movies_count', 'full_name')

class IsAwardedMixin(models.Model):
    is_awarded = models.BooleanField(default=False)

    class Meta:
        abstract = True

class LastUpdatedMixin(models.Model):
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2), MaxLengthValidator(120)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown',validators=[MaxLengthValidator(50)])

    class Meta:
        abstract = True

class Director(Person):
    years_of_experience = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])

    objects = DirectorManager()

class Actor(Person, IsAwardedMixin, LastUpdatedMixin):
    pass

class Movie(IsAwardedMixin, LastUpdatedMixin):

    class GenreChoices(models.TextChoices):
        ACTION = 'Action', 'Action'
        COMEDY = 'Comedy', 'Comedy'
        DRAMA = 'Drama', 'Drama'
        OTHER = 'Other', 'Other'

    title = models.CharField(max_length=150, validators=[MinLengthValidator(5), MaxLengthValidator(150)])
    release_date = models.DateField()
    storyline = models.TextField(blank=True, null=True)
    genre = models.CharField(choices=GenreChoices.choices, default=GenreChoices.OTHER, max_length=6, validators=[MaxLengthValidator(6)])
    rating = models.DecimalField(decimal_places=1, max_digits=3, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    is_classic = models.BooleanField(default=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, related_name='mv')
    starring_actor = models.ForeignKey(Actor, on_delete=models.SET_NULL, null=True, blank=True, related_name='stars_movies')
    actors = models.ManyToManyField(Actor, related_name='movies')



