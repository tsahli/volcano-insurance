"""Models."""
from django.db import models
from datetime import date
from django.utils.crypto import get_random_string


def get_random_quote_string():
    return get_random_string(length=10)


class Quote(models.Model):
    """Model definition for a quote object."""

    quote_number = models.CharField(
        max_length=10, editable=False, default=get_random_quote_string
    )
    effective_date = models.DateField(default=date.today())
    previous_policy_cancelled = models.BooleanField(default=False)
    owns_property_to_be_insured = models.BooleanField(default=False)
    property_zip_code = models.CharField(max_length=50)
    property_state = models.CharField(max_length=50)
