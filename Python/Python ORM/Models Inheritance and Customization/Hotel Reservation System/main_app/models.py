import datetime
from datetime import timedelta

from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Q

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

class Room(models.Model):
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)
    number = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    total_guests = models.PositiveIntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.total_guests > self.capacity:
            raise ValidationError("Total guests are more than the capacity of the room")

        super().save(*args, **kwargs)
        return f"Room {self.number} created successfully"

class BaseReservation(models.Model):

    class Meta:
        abstract = True

    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def reservation_period(self):
        return (self.end_date - self.start_date).days

    def calculate_total_cost(self):
        return round((self.room.price_per_night * self.reservation_period()), 2)

    def save(self, *args, **kwargs):
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after or in the same end date")

        regular_reservations = RegularReservation.objects.filter((Q(start_date__range=(self.start_date,
                                                                                       self.end_date)) | Q(
            end_date__range=(self.start_date, self.end_date))) | Q(start_date__gt=self.start_date,
                                                                   end_date__lte=self.end_date), room=self.room)
        special_reservations = SpecialReservation.objects.filter((Q(start_date__range=(self.start_date,
                                                                                       self.end_date)) | Q(
            end_date__range=(self.start_date, self.end_date))) | Q(start_date__gt=self.start_date,
                                                                   end_date__lte=self.end_date), room=self.room)

        if not (len(regular_reservations) == 0 and len(special_reservations) == 0):
            raise ValidationError(f"Room {self.room.number} cannot be reserved")

        super().save(*args, **kwargs)

class RegularReservation(BaseReservation):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return f"Regular reservation for room {self.room.number}"

class SpecialReservation(BaseReservation):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        return f"Special reservation for room {self.room.number}"

    def extend_reservation(self, days: int):
        try:
            self.end_date += timedelta(days=days)
            self.save()
        except ValidationError:
            raise ValidationError("Error during extending reservation")
        return f"Extended reservation for room {self.room.number} with {days} days"






















