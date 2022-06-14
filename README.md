# Volcano-insurance
An API built with Python  and [Django REST Framework](https://www.django-rest-framework.org/)

---

### Makefile commands
* `make start` -- start the server running locally
* `make migrate-all` -- make and apply migrations
* `make test` -- run the test suite
* `make format` -- run the black formatter

---
### Localhost Endpoints
* localhost:8000/quotes/
    * GET list all quote objects
    * POST create a new quote object
* localhost:8000/quotes/{pk}
    * GET return a specific quote object
* localhost:800/quotes/{quote_number}/checkout
    * GET return a checkout quote for a given quote number