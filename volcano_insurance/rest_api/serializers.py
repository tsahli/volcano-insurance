"""Serializers."""
from rest_framework import serializers
from rest_api.models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    """Serializer for Quote model."""
    class Meta:
        model = Quote
        fields = [
            "id",
            "quote_number",
            "effective_date",
            "previous_policy_cancelled",
            "owns_property_to_be_insured",
            "property_zip_code",
            "property_state",
        ]
