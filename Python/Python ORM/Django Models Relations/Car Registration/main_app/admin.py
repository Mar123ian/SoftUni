from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'owner', 'car_details')

    @staticmethod
    def car_details(obj):

        try:
            own = str(obj.owner.name)
        except Exception:
            own = "No owner"

        try:
            reg = str(obj.registration.registration_number)
        except Exception:
            reg = "No registration number"

        return f"Owner: {own}, Registration: {reg}"

    car_details.short_description = "Car Details"