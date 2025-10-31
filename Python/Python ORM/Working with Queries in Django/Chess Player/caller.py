import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
from main_app.models import ChessPlayer

def bulk_create_chess_players(args: List[ChessPlayer]):
    ChessPlayer.objects.bulk_create(args)

def delete_chess_players():
    ChessPlayer.objects.filter(title="no title").delete()

def change_chess_games_won():
    ChessPlayer.objects.filter(title="GM").update(won=30)

def change_chess_games_lost():
    ChessPlayer.objects.filter(title="no title").update(lost=25)

def change_chess_games_drawn():
    ChessPlayer.objects.update(games_drawn=10)

def grand_chess_title_GM():
    ChessPlayer.objects.filter(rating__gte=2400).update(title="GM")

def grand_chess_title_IM():
    ChessPlayer.objects.filter(rating__range=(2300, 2399)).update(title="IM")

def grand_chess_title_FM():
    ChessPlayer.objects.filter(rating__range=(2200, 2299)).update(title="FM")

def grand_chess_title_regular_player():
    ChessPlayer.objects.filter(rating__lte=2199).update(title="regular player")



