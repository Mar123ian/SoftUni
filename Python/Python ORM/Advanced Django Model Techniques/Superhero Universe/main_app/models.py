from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class RechargeEnergyMixin(models.Model):
    energy = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def recharge_energy(self, amount: int):
        try:
            self.energy += amount
            self.save()
        except ValidationError:
            self.energy = 100
            self.save()

class Hero(RechargeEnergyMixin):
    name = models.CharField(max_length=100)
    hero_title = models.CharField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.superpower_info={
            "SpiderHero": [80, f"{self.name} as Spider Hero is out of web shooter fluid", f"{self.name} as Spider Hero swings from buildings using web shooters"],
            "FlashHero": [65, f"{self.name} as Flash Hero needs to recharge the speed force", f"{self.name} as Flash Hero runs at lightning speed, saving the day"]
        }

    def superpower(self, name):
        required_energy, fail_msg, success_msg = self.superpower_info[name]

        if self.energy<required_energy:
            return fail_msg

        self.energy -= required_energy
        if self.energy == 0:
            self.energy = 1
        self.save()
        return success_msg
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

class SpiderHero(Hero):

    def swing_from_buildings(self):
        return self.superpower(self.__class__.__name__)

    class Meta:
        proxy = True

class FlashHero(Hero):
    def run_at_super_speed(self):
        return self.superpower(self.__class__.__name__)

    class Meta:
        proxy = True







