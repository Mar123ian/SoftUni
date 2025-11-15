from django.db import models

try:
    # Assuming the custom field is defined in the same app under fields.py
    from .fields import MaskedCreditCardField
except Exception:  # Fallback import path if structured differently
    from masked_credit_card_field import MaskedCreditCardField  # type: ignore


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)

    def __str__(self) -> str:
        return f"{self.card_owner}"
