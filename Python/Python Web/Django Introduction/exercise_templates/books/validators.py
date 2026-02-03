from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class BadWordsValidator:
    def __init__(self, bad_words):
        self.bad_words = bad_words

    def __call__(self, value):
        for word in self.bad_words:
            if word in value:
                raise ValidationError(f"Banned word: {word}")
