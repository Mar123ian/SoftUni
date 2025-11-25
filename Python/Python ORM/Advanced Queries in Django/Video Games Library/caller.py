import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import *
# Run and print your queries
game2 = VideoGame.objects.create(title="Cyberpunk 2077", genre="RPG",

release_year=2020, rating=7.2)

game3 = VideoGame.objects.create(title="Red Dead Redemption 2", genre="Adventure",

release_year=2018, rating=9.7)

game4 = VideoGame.objects.create(title="FIFA 22", genre="Sports", release_year=2021,

rating=8.5)

game5 = VideoGame.objects.create(title="Civilization VI", genre="Strategy",

release_year=2016, rating=8.8)

print(VideoGame.objects.average_rating())