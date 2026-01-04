import datetime
import os
import django
from django.db.models import Q, F

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import *
# Create queries within functions

def populate_db():
    actor1 = Actor(full_name='a')
    actor1.save()
    actor2 = Actor(full_name='b')
    actor2.save()
    director1 = Director(full_name='a')
    director1.save()
    director2 = Director(full_name='b')
    director2.save()
    movie1 = Movie(title='a', release_date=datetime.datetime.now(), rating=2.8, director=director1)
    movie1.save()
    movie1.actors.add(actor1)
    movie1.save()
    movie2 = Movie(title='b', release_date=datetime.datetime.now(), rating=2.9, director=director2)
    movie2.save()
    movie2.actors.add(actor2)
    movie2.save()

#print(Director.objects.get_directors_by_movies_count())

def get_directors(search_name=None, search_nationality=None):
    directors = None
    if search_name is None and search_nationality is None:
        return ""
    if search_name is not None and search_nationality is not None:
        directors = Director.objects.filter(Q(full_name__icontains=search_name) & Q(nationality__icontains=search_nationality))
    elif search_name is None:
        directors = Director.objects.filter(nationality__icontains=search_nationality)
    elif search_nationality is None:
        directors = Director.objects.filter(full_name__icontains=search_name)


    directors = directors.order_by('full_name')

    output=[]
    for d in directors:
        output.append(f"Director: {d.full_name}, nationality: {d.nationality}, experience: {d.years_of_experience}")

    return "\n".join(output)

def get_top_director():
    director = Director.objects.get_directors_by_movies_count().first()

    if director is None:
        return ""
    return f"Top Director: {director.full_name}, movies: {director.movies_count}."

def get_top_actor():

    a = Actor.objects.annotate(movies_count=Count('stars_movies')).order_by('-movies_count', 'full_name').first()
    if a is None:
        return ""
    ms = a.movies.all()
    if ms is None:
        return ""
    movies=[]
    r=0
    for m in ms:
        movies.append(m.title)
        r+=m.rating
    r/=len(ms)
    movies = ", ".join(movies)

    return f"Top Actor: {a.full_name}, starring in movies: {movies}, movies average rating: {r:.1f}"

#get_directors()
#get_top_director()
#get_top_actor()

#-----------------------------------------------------------------------
#-----------------------------------------------------------------------
#-----------------------------------------------------------------------

def get_actors_by_movies_count():
    actors = Actor.objects.annotate(movies_count=Count(('movies'))).order_by('-movies_count', 'full_name')[:3]

    if actors is None:
        return ""

    output=[]
    for a in actors:
        if a.movies_count == 0:
            return ""

        output.append(f"{a.full_name}, participated in {a.movies_count} movies")

    return "\n".join(output)


#print(get_actors_by_movies_count())

def get_top_rated_awarded_movie():
    movie = Movie.objects.filter(is_awarded=True).order_by('-rating', 'title').first()
    if movie is None:
        return ""
    starring_actor_full_name = 'N/A' if movie.starring_actor.full_name is None else movie.starring_actor.full_name

    cast = []
    acts = movie.actors.order_by('full_name')
    for a in acts:
        cast.append(a.full_name)
    cast = ", ".join(cast)
    return f"Top rated awarded movie: {movie.title}, rating: {movie.rating}. Starring actor: {starring_actor_full_name}. Cast: {cast}."


def increase_rating():
    m = Movie.objects.filter(Q(is_classic=True) & Q(~Q(rating=10.0)))
    num_of_updated_movies = m.count()
    m.update(rating=F('rating') + 0.1)

    return f"Rating increased for {num_of_updated_movies} movies." if num_of_updated_movies != 0 else "No ratings increased."







def populate_db():
    Author.objects.all().delete()
    Publisher.objects.all().delete()
    Book.objects.all().delete()

    p1 = Publisher.objects.create(
        name='a',
        country='America',
        established_date=timezone.now(),
    )

    p2 = Publisher.objects.create(
        name='b',
        country='America',
        established_date=timezone.now(),
    )

    a1 = Author.objects.create(
        name='Peter',
    )

    a2 = Author.objects.create(
        name='Ivan',
    )

    a3 = Author.objects.create(
        name='Mike',
    )

    b1 = Book.objects.create(
        title='Book 1',
        main_author=a1,
        publisher=p1,
        publication_date=timezone.now(),
        price=10.00
    )
    b1.co_authors.add(a2, a3)

    b2= Book.objects.create(
        title='Book 2',
        main_author=a2,
        publisher=p2,
        publication_date=timezone.now(),
        price=16.00
    )
    b2.co_authors.add(a3, a1)