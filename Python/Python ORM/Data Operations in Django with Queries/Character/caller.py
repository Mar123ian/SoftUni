import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Character
# Create queries within functions
Character.objects.all().delete()
def update_characters():
    characters = Character.objects.all()

    for character in characters:
        if character.class_name == "Mage":
            character.level += 3
            character.intelligence -= 7
        elif character.class_name == "Warrior":
            character.hit_points //= 2
            character.dexterity += 4
        elif character.class_name in ("Assassin", "Scout"):
            character.inventory = "The inventory is empty"

        character.save()

def fuse_characters(first_character: Character, second_character: Character):
    Character.objects.create(
        name=f"{first_character.name} {second_character.name}",
        class_name="Fusion",
        level=(first_character.level + second_character.level) // 2,
        strength=(first_character.strength + second_character.strength) * 1.2,
        dexterity=(first_character.dexterity + second_character.dexterity) * 1.4,
        intelligence=(first_character.intelligence + second_character.intelligence) * 1.5,
        hit_points=first_character.hit_points + second_character.hit_points,
        inventory = "Bow of the Elven Lords, Amulet of Eternal Wisdom" if first_character.class_name in ("Mage", "Scout") else "Dragon Scale Armor, Excalibur",
    )

    first_character.delete()
    second_character.delete()

def grand_dexterity():
    Character.objects.update(dexterity=30)

def grand_intelligence():
    Character.objects.update(intelligence=40)

def grand_strength():
    Character.objects.update(strength=50)

def delete_characters():
    Character.objects.filter(inventory="The inventory is empty").delete()
