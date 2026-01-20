from django.urls import path

from . import views

urlpatterns = [
    path('review/<int:review_id>/', views.show_review, name='show_review'),
]