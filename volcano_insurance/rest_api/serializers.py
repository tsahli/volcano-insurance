"""Serializers."""
from rest_framework import serializers
from rest_api.models import Quote
from datetime import date
import re
import us
from django.utils.crypto import get_random_string


class QuoteSerializer(serializers.Serializer):
    """Serializer for Quote model."""

    id = serializers.ReadOnlyField()
    quote_number = serializers.ReadOnlyField()
    effective_date = serializers.DateField(default=date.today())
    previous_policy_cancelled = serializers.BooleanField(default=False)
    owns_property_to_be_insured = serializers.BooleanField(default=False)
    property_zip_code = serializers.CharField(max_length=50)
    property_state = serializers.CharField(max_length=50)

    def validate_property_zip_code(self, zip_code):
        """Validation for zip code."""
        if not re.match("^(\d{5})([- ])?(\d{4})?$", zip_code):
            raise serializers.ValidationError(
                {"detail": f"{zip_code} is not a valid US zip code."}
            )
        return zip_code

    def validate_property_state(self, state):
        """Validation for US state."""
        found_state = us.states.lookup(state)
        if found_state is None:
            raise serializers.ValidationError(
                {"detail": f"{state} is not a valid US state."}
            )
        return found_state

    def create(self, validated_data):
        """Creates a new Quote object."""
        return Quote.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """DRF needs this to be implemented to get single. Has no other use."""
        return instance
