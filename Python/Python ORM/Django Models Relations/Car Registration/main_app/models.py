from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=50)

class Car(models.Model):
    model = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='cars', null=True, blank=True)

class Registration(models.Model):
    registration_number = models.CharField(max_length=10, unique=True)
    registration_date = models.DateField(null=True, blank=True)
    car = models.OneToOneField(Car, on_delete=models.CASCADE, related_name='registration', null=True, blank=True)