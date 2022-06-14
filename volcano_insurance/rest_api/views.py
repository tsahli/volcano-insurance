from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_api.models import Quote
from rest_api.serializers import QuoteSerializer
from .calculate_quote import CalculateQuote


class QuoteList(APIView):
    def get(self, request, format=None):
        """List all Quotes."""
        quotes = Quote.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """Post a new Quote."""
        serializer = QuoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuoteDetail(APIView):
    def __get_quote_or_404(self, pk):
        """Returns quote object or raises a 404."""
        try:
            return Quote.objects.get(pk=pk)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        """Get a single Quote by primary key."""
        quote = self.__get_quote_or_404(pk)
        serializer = QuoteSerializer(quote, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CheckoutQuote(APIView):
    def __get_checkout_quote_or_404(self, quote_number):
        """Returns a checkout quote or raises a 404"""
        try:
            return Quote.objects.get(quote_number=quote_number)
        except Quote.DoesNotExist:
            raise Http404

    def get(self, request, quote_number, format=None):
        """Checkout a quote by quote number."""
        quote = self.__get_checkout_quote_or_404(quote_number)
        calculated_quote = CalculateQuote(quote).form_checkout_quote_response()
        return Response(calculated_quote)
