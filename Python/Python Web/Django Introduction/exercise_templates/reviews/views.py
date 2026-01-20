from django.shortcuts import render
from .models import Review

# Create your views here.
def show_all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'all_reviews.html', {'reviews': reviews})