from django.shortcuts import redirect
from django.urls import path, reverse, include
from . import views

urlpatterns = [
    path('', views.redirect_empty_path, name='redirect_empty_path'),
    path('destinations/', include([
            path('<slug:destination_slug>/<int:year>/', views.show_destinations_for_year, name='show_destinations_for_year'),
            path('', views.show_all_destinations, name='show_all_destinations'),
            path('<slug:destination_slug>', views.show_destination, name='show_destination'),
    ]))
]