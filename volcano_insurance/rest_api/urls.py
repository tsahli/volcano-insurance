from django.urls import path
from rest_api import views

urlpatterns = [
    path("quotes/", views.QuoteList.as_view()),
    path("quotes/<int:pk>/", views.QuoteDetail.as_view()),
    path("quotes/<str:quote_number>/checkout", views.CheckoutQuote.as_view()),
]
