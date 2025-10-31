import os
from typing import List

import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models
# Create and check models
# Run and print your queries
from main_app.models import Workout
from django.db.models import Q

def show_workouts():
    workouts = Workout.objects.filter(Q(workout_type="Calisthenics") | Q(workout_type="CrossFit")).order_by('id')
    return "\n".join(f"{workout.name} from {workout.workout_type} type has {workout.difficulty} difficulty!" for workout in workouts)

def get_high_difficulty_cardio_workouts():
    return Workout.objects.filter(workout_type="Cardio", difficulty="High").order_by('instructor')

def set_new_instructors():
    instructors = {
        "Cardio": "John Smith",
        "Strength": "Michael Williams",
        "Yoga": "Emily Johnson",
        "CrossFit": "Sarah Davis",
        "Calisthenics": "Chris Heria"
    }

    workouts = Workout.objects.all()
    for workout in workouts:
        workout.instructor = instructors[workout.workout_type]

    Workout.objects.bulk_update(workouts, ["instructor"])

def set_new_duration_times():
    times = {
        "John Smith": "15 minutes",
        "Sarah Davis": "30 minutes",
        "Chris Heria": "45 minutes",
        "Michael Williams": "1 hour",
        "Emily Johnson": "1 hour and 30 minutes"
    }

    workouts = Workout.objects.all()
    for workout in workouts:
        workout.duration_time = times[workout.instructor]

    Workout.objects.bulk_update(workouts, ["duration_time"])

def delete_workouts():
    Workout.objects.exclude(Q(workout_type="Calisthenics") | Q(workout_type="Strength")).delete()




