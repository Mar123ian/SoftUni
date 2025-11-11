import datetime
import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here

# Create queries within functions
from main_app.models import *

def register_car_by_owner(owner: Owner):
    registration = Registration.objects.filter(car=None).first()
    car = Car.objects.filter(registration=None).first()

    registration.registration_date=datetime.date.today()
    car.registration = registration
    car.owner=owner
    car.save()
    registration.save()

    return f"Successfully registered {car.model} to {owner.name} with registration number {registration.registration_number}."



