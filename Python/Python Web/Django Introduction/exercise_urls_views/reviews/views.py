from django.shortcuts import render, get_object_or_404

from models import Review


def show_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)

    return render(request, 'review.html', {'review': review})