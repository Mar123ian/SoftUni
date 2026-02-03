def save_review_for_book(form, book):
    review = form.save(commit=False)
    review.book = book
    review.save()
