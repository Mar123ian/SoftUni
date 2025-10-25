from django.db import models


class Character(models.Model):
    CLASS_MAGE = "Mage"
    CLASS_WARRIOR = "Warrior"
    CLASS_ASSASSIN = "Assassin"
    CLASS_SCOUT = "Scout"

    CLASS_CHOICES = [
        (CLASS_MAGE, CLASS_MAGE),
        (CLASS_WARRIOR, CLASS_WARRIOR),
        (CLASS_ASSASSIN, CLASS_ASSASSIN),
        (CLASS_SCOUT, CLASS_SCOUT),
    ]

    name = models.CharField(max_length=100)
    class_name = models.CharField(max_length=20, choices=CLASS_CHOICES)
    level = models.PositiveIntegerField()
    strength = models.PositiveIntegerField()
    dexterity = models.PositiveIntegerField()
    intelligence = models.PositiveIntegerField()
    hit_points = models.PositiveIntegerField()
    inventory = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.class_name}) Lv.{self.level}"
