"""Models."""
from django.db import models
from datetime import datetime
from localflavor.us.forms import USStateField, USZipCodeField

class Quote(models.Model):
    """Model definition for a quote object."""
    quote_number = models.CharField(max_length=10, unique=True, required=True)
    effective_date = models.DateTimeField(default=datetime.now, required=True)
    previous_policy_cancelled = models.BooleanField(default=False, required=True)
    owns_property_to_be_insured = models.BooleanField(default=False, required=True)
    property_zip_code = USZipCodeField(required=True)
    property_state = USStateField(required=True)

