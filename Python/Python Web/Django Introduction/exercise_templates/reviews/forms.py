from django.forms import modelform_factory
from .models import Review

ReviewForm = modelform_factory(Review, fields=('author', 'body', 'rating'))

class AddReviewForm(ReviewForm):
    pass