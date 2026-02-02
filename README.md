# Fake Store API Tests

Simple API tests for the public Fake Store API using Python and pytest.

---

## Prerequisites

* Python 3.10 or newer
* pip

---

## Installation

1. Open a terminal and go to the project folder:

```
cd fake-store-api-tests
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

---

## Run Tests

Run all tests:

```
python -m pytest
```

Run one test file:

```
python -m pytest tests/test_products.py
```

Run tests by marker:

```
python -m pytest -m auth
python -m pytest -m products
python -m pytest -m carts
python -m pytest -m negative
```

Verbose output:

```
python -m pytest -v
python -m pytest -vv
```

---

## Test Report

Generate an HTML report:

```
python -m pytest --html=reports/report.html --self-contained-html
```

The report will be saved in the `reports` folder.
Note: The project is configured so running `pytest` will generate the report automatically.

---

## Project Structure

```
fake-store-api-tests/
├── api/                 # API client modules
│   ├── api_client.py
│   ├── auth_api.py
│   ├── products_api.py
│   └── carts_api.py
├── tests/               # Test cases
│   ├── test_auth.py
│   ├── test_products.py
│   ├── test_carts.py
│   └── test_carts_edge.py
├── schemas/             # JSON schemas
├── config/              # Config values (base URL, timeouts)
├── reports/             # Generated reports
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## What the Tests Cover

* Authentication: valid and invalid login cases.
* Products: list, single product, categories, limits, sorting, schema checks, and edge cases.
* Carts: list, carts by user, date filtering, sorting, limits, schema checks, and edge cases.

---

## Test Count

* Total automated tests: 41

---

## Tech Stack

* Python
* pytest
* requests
* jsonschema
* pytest-html
* logging (standard library)


## Logging

- **File:** `fake-store-api-tests/logger.py` 
- **Log file:** `fake-store-api-tests/logs.log` 
- **What is logged:** HTTP method, endpoint, request payload (when present), response status code, and response body
- **How to generate logs:** run the tests (logs are appended automatically):

```bash
cd fake-store-api-tests
python -m pytest -q
```

---

## Common Issues

* Import errors: run `pytest` from the project root.
* Network issues: tests use a public API and require internet access.
* Timeouts: request timeout can be changed in `config/config.py`.

---


