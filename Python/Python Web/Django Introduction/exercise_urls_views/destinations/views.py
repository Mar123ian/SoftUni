from django.shortcuts import render, redirect, get_object_or_404

from destinations.models import Destination


# Create your views here.
def show_destination(request, destination_slug):
    destination = get_object_or_404(Destination, slug=destination_slug)
    reviews = destination.reviews.order_by("-created_at")
    return render(request, 'destination.html', {'destination': destination, 'reviews': reviews})

def show_all_destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'all_destinations.html', {'destinations': destinations})

def redirect_empty_path(request):
    return redirect('show_all_destinations')

def show_destinations_for_year(request, destination_slug, year):
    destination = get_object_or_404(Destination, slug=destination_slug, reviews__created_at__year=year)
    reviews = destination.reviews.order_by("-created_at")
    return render(request, 'destination.html', {'destination': destination, 'reviews': reviews})



