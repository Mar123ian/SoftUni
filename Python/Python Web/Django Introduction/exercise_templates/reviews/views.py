from django.forms import modelformset_factory

from .forms import ReviewForm
from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def show_all_reviews(request):
    reviews = Review.objects.all()
    return render(request, 'all_reviews.html', {'reviews': reviews})

def edit_reviews(request):
    Reviews_formset = modelformset_factory(Review, form=ReviewForm, extra=1)
    formset = Reviews_formset(request.POST or None, queryset=Review.objects.all())

    if request.method == 'POST' and formset.is_valid():
        formset.save()
        return redirect('show_all_reviews')

    return render(request, 'edit_reviews.html', {'formset': formset})
