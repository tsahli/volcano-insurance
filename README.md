# Volcano-insurance
An API built with Python  and [Django REST Framework](https://www.django-rest-framework.org/)

---
### Quickstart
Prerequisites:
* Docker. If you don't have Docker, run with `make start-no-docker`

```
cd volcano_insurance
make start
```

### Makefile commands (Be sure to be in the `volcano_insurance` directory)
* `make start` -- start the server in a docker container
* `make start-no-docker` -- start the server without docker
* `make migrate-all` -- make and apply migrations
* `make test` -- run the test suite
* `make format` -- run the black formatter

---
### Localhost Endpoints
* localhost:8080/quotes
    * GET list all quote objects
    * POST create a new quote object
    ```
        // Example POST body
    {
        "previous_policy_cancelled": true,
        "owns_property_to_be_insured": true,
        "property_zip_code": "84096",
        "property_state": "nv"
    }
    ```
* localhost:8080/quotes/{pk}
    * GET return a specific quote object
* localhost:8080/quotes/{quote_number}/checkout
    * GET return a checkout quote for a given quote number

---

### Notes
* Manually tested all endpoints with Postman
* Did not round checkout quote values intentionally, but could be easily done with some changes in `calculate_quote.py`
* Had a lot of fun learning DRF, thanks for the opportunity :)
