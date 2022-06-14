from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.test import APIClient


class ViewsTests(APITestCase):

    client = APIClient()

    def test_get_quote_list(self):
        """It returns a list of quotes."""
        response = self.client.get("http://testserver/quotes")
        assert response.status_code == status.HTTP_200_OK

    def test_post_with_valid_body(self):
        """It accepts posts with a valid body."""
        response = self.client.post(
            "/quotes",
            {
                "previous_policy_cancelled": "True",
                "owns_property_to_be_insured": "True",
                "property_zip_code": "84096",
                "property_state": "ut",
            },
            format="json",
        )
        assert response.status_code == status.HTTP_201_CREATED

    def test_post_with_invalid_body(self):
        """It returns an error when posting with an invalid post body."""
        response = self.client.post(
            "/quotes",
            {
                "previous_policy_cancelled": "True",
                "owns_property_to_be_insured": "True",
                "property_zip_code": "84096",
                "property_state": "zzzz",
            },
            format="json",
        )
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_get_quote_detail_does_not_exist(self):
        """It returns a 404 the requested quote detail does not exist."""
        response = self.client.get("http://testserver/quotes/1")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_checkout_quote_does_not_exist(self):
        """It returns a 404 if the checkout quote does not exist."""
        response = self.client.get("http://testserver/quotes/foobar/checkout")
        assert response.status_code == status.HTTP_404_NOT_FOUND
