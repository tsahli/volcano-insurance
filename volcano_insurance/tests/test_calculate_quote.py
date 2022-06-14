from django.test import TestCase
from rest_api.models import Quote
from rest_api.calculate_quote import (
    CalculateQuote,
    POLICY_TERM_MONTHS,
    CANCELLATION_FEE,
    VOLCANO_FEE,
    NEVER_CANCELLED_DISCOUNT,
    OWNS_PROPERTY_DISCOUNT,
    BASE_PRICE,
)


class CalculateQuoteTest(TestCase):
    def test_quotes_are_applying_fees_correctly(self):
        """When all fees are applicable, the fee should be correct"""
        quote = Quote.objects.create(
            previous_policy_cancelled=True,
            owns_property_to_be_insured=False,
            property_zip_code="84096",
            property_state="Utah",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        assert result.get("total_additional_fees") == (BASE_PRICE * VOLCANO_FEE) + (BASE_PRICE * CANCELLATION_FEE)

    def test_quotes_are_calculating_monthly_fees_correctly(self):
        """A quote's monthly fee should equal the total fee / POLICY_TERM_MONTHS"""
        quote = Quote.objects.create(
            previous_policy_cancelled=False,
            owns_property_to_be_insured=False,
            property_zip_code="84096",
            property_state="Utah",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        total_fees = result.get("total_additional_fees")
        assert result.get("total_monthly_fees") == total_fees / POLICY_TERM_MONTHS

    def test_quotes_with_all_discounts_are_applied(self):
        """When all possible discounts are applicable, total discount should be correct"""
        quote = Quote.objects.create(
            previous_policy_cancelled=False,
            owns_property_to_be_insured=True,
            property_zip_code="84096",
            property_state="Nevada",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        assert result.get("total_discounts") == (BASE_PRICE * NEVER_CANCELLED_DISCOUNT) + (BASE_PRICE * OWNS_PROPERTY_DISCOUNT)

    def test_quotes_are_calculating_monthly_discounts_correctly(self):
        """A quotes monthly discount should equal the total discount / POLICY_TERM_MONTHS"""
        quote = Quote.objects.create(
            previous_policy_cancelled=False,
            owns_property_to_be_insured=True,
            property_zip_code="84096",
            property_state="Nevada",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        total_discounts = result.get("total_discounts")
        assert result.get("total_monthly_discounts") == total_discounts / POLICY_TERM_MONTHS

    def test_total_term_premium_is_calculated_correctly(self):
        """Total term premium should equal the sum of all additional fees minus discounts."""
        quote = Quote.objects.create(
            previous_policy_cancelled=False,
            owns_property_to_be_insured=True,
            property_zip_code="84096",
            property_state="Utah",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        total_applicable_fees = (BASE_PRICE * VOLCANO_FEE)
        total_applicable_discounts = (BASE_PRICE * OWNS_PROPERTY_DISCOUNT) + (BASE_PRICE * NEVER_CANCELLED_DISCOUNT)
        assert result.get("total_term_premium") == BASE_PRICE + total_applicable_fees - total_applicable_discounts

    def test_total_monthly_premium_is_calculated_correctly(self):
        """Total monthly premium should equal the total term premium / POLICY_TERM_MONTHS"""
        quote = Quote.objects.create(
            previous_policy_cancelled=False,
            owns_property_to_be_insured=True,
            property_zip_code="84096",
            property_state="Utah",
        )
        result = CalculateQuote(quote).form_checkout_quote_response()
        total_term_premium = result.get("total_term_premium")
        assert result.get("monthly_total_premium") == total_term_premium / POLICY_TERM_MONTHS
