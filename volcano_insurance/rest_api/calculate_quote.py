"""Business logic for calculating a quoite."""

POLICY_TERM_MONTHS = 6
BASE_PRICE = 59.94

# FEES
CANCELLATION_FEE = 0.15
VOLCANO_FEE = 0.25
STATES_WITH_ACTIVE_VOLCANOS = [
    "Alaska",
    "Arizona",
    "California",
    "Colorado",
    "Hawaii",
    "Idaho",
    "Nevada",
    "New Mexico",
    "Oregon",
    "Utah",
    "Washington",
    "Wyoming",
]

# DISCOUNTS
NEVER_CANCELLED_DISCOUNT = 0.10
OWNS_PROPERTY_DISCOUNT = 0.20


class CalculateQuote:
    def __init__(self, quote) -> None:
        self.quote = quote

    def form_checkout_quote_response(self):
        """Forms the response."""
        total_additional_fees = self._calculate_total_additional_fees()
        total_monthly_fees = total_additional_fees / POLICY_TERM_MONTHS

        total_discounts = self._calculate_total_discount()
        total_monthly_discounts = total_discounts / POLICY_TERM_MONTHS

        total_term_premium = BASE_PRICE + total_additional_fees - total_discounts
        monthly_total_premium = total_term_premium / POLICY_TERM_MONTHS

        return {
            "quote_number": self.quote.quote_number,
            "base_premium": BASE_PRICE,
            "total_term_premium": total_term_premium,
            "monthly_total_premium": monthly_total_premium,
            "total_additional_fees": total_additional_fees,
            "total_monthly_fees": total_monthly_fees,
            "total_discounts": total_discounts,
            "total_monthly_discounts": total_monthly_discounts,
        }

    def _calculate_total_discount(self) -> float:
        """Calculates the total amount to be discounted over a policy term."""
        total_discount = 0
        if self.quote.previous_policy_cancelled is False:
            total_discount += BASE_PRICE * NEVER_CANCELLED_DISCOUNT
        if self.quote.owns_property_to_be_insured:
            total_discount += BASE_PRICE * OWNS_PROPERTY_DISCOUNT
        return total_discount

    def _calculate_total_additional_fees(self) -> float:
        """Calculates the total amount of additional fees over a policy term."""
        total_fees = 0
        if self.quote.property_state in STATES_WITH_ACTIVE_VOLCANOS:
            total_fees += BASE_PRICE * VOLCANO_FEE
        if self.quote.previous_policy_cancelled:
            total_fees += BASE_PRICE * CANCELLATION_FEE
        return total_fees
