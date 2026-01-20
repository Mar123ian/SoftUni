from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.show_all_reviews, name='show_all_reviews')
    ]