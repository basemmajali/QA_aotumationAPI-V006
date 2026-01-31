# Fake Store API – Test Cases

## 1. Introduction

This document lists the main test cases covered by the automated tests.

Scope:

* Authentication (Login)
* Products
* Carts

The test cases include:

* Positive scenarios
* Negative scenarios
* Basic edge cases

---

## 2. Authentication 

| TC ID   | Description                  | Endpoint         | Input                       | Expected Result            |
| ------- | ---------------------------- | ---------------- | --------------------------- | -------------------------- |
| AUTH-01 | Login with valid credentials | POST /auth/login | Valid username and password | Status 200, token returned |
| AUTH-02 | Login with invalid username  | POST /auth/login | Invalid username            | Status 401                 |
| AUTH-03 | Login with invalid password  | POST /auth/login | Invalid password            | Status 401                 |
| AUTH-04 | Login with empty credentials | POST /auth/login | Empty username and password | Status 400 or 401          |
| AUTH-04 | Login with empty credentials | POST /auth/login | Empty username and password | Status 400 or 401          |
| AUTH-06 | Login with very long username| POST /auth/login | Username > 100 characters   | Status 400 or validation error |
| AUTH-05 | Login without request body   | POST /auth/login | No payload                  | Status 400                 |
| AUTH-06 | Login with long username     | POST /auth/login | Very long username          | Status 400 or 401          |

---

## 3. Products 

| TC ID   | Description                         | Endpoint                 | Input / Params | Expected Result                  |
| ------- | ----------------------------------- | ------------------------ | -------------- | -------------------------------- |
| PROD-01 | Get all products                    | GET /products            | None           | Status 200, list returned        |
| PROD-02 | Get product by valid ID             | GET /products/{id}       | id = 1         | Status 200, product returned     |
| PROD-03 | Get product categories              | GET /products/categories | None           | Status 200, list returned        |
| PROD-04 | Get products with limit             | GET /products            | limit = 5      | Limited number of items returned |
| PROD-05 | Get products sorted ascending       | GET /products            | sort = asc     | Sorted list returned             |
| PROD-06 | Get products sorted descending      | GET /products            | sort = desc    | Sorted list returned             |
| PROD-07 | Validate product schema             | GET /products/{id}       | id = 1         | Response matches schema          |
| PROD-08 | Validate response time              | GET /products            | None           | Response within acceptable time  |
| PROD-09 | Get product with invalid ID         | GET /products/{id}       | id = -1        | Handled without crash            |
| PROD-10 | Get product with non-existing ID    | GET /products/{id}       | id = 99999     | Empty or handled response        |
| PROD-11 | Get product with string ID          | GET /products/{id}       | id = abc       | Handled without crash            |
| PROD-12 | Get product with special characters | GET /products/{id}       | id = @@@       | Handled without crash            |
| PROD-13 | Get products with negative limit    | GET /products            | limit = -1     | Handled without crash            |
| PROD-14 | Get products with string limit      | GET /products            | limit = abc    | Handled without crash            |
| PROD-15 | Get products with limit = 0         | GET /products            | limit = 0      | Empty or default list            |
| PROD-16 | Get products with large limit       | GET /products            | limit = 1000   | List returned                    |
| PROD-17 | Validate required fields exist      | GET /products/{id}       | id = 1         | Required fields are present      |
| PROD-18 | Validate product schema fields      | GET /products/{id}       | id = 1         | All main fields exist            |

---

## 4. Carts 

| TC ID   | Description                         | Endpoint             | Input / Params      | Expected Result             |
| ------- | ----------------------------------- | -------------------- | ------------------- | --------------------------- |
| CART-01 | Get all carts                       | GET /carts           | None                | Status 200                  |
| CART-02 | Get carts by valid user ID          | GET /carts/user/{id} | userId = 1          | Status 200                  |
| CART-03 | Get carts by invalid user ID        | GET /carts/user/{id} | userId = 99999      | Empty or handled response   |
| CART-04 | Get carts with negative user ID     | GET /carts/user/{id} | userId = -1         | Handled without crash       |
| CART-05 | Get carts using date range          | GET /carts           | startDate & endDate | Filtered list returned      |
| CART-06 | Get carts with invalid date format  | GET /carts           | Invalid dates       | Handled without crash       |
| CART-07 | Get carts with future date range    | GET /carts           | Future dates        | Empty or handled response   |
| CART-08 | Get carts sorted ascending          | GET /carts           | sort = asc          | Sorted list returned        |
| CART-09 | Get carts sorted descending         | GET /carts           | sort = desc         | Sorted list returned        |
| CART-10 | Get carts with limit                | GET /carts           | limit = 5           | Limited number of carts     |
| CART-11 | Get carts with negative limit       | GET /carts           | limit = -5          | Handled without crash       |
| CART-12 | Get carts where startDate > endDate | GET /carts           | startDate > endDate | Empty or handled response   |
| CART-13 | Validate cart schema                | GET /carts/{id}      | id = 1              | Response matches schema     |
| CART-14 | Validate required fields exist      | GET /carts/user/{id} | userId = 1          | Required fields are present |
| CART-15 | Get carts with string user ID       | GET /carts/user/{id} | userId = abc        | Handled without crash       |

---

## 5. Test Case Summary

| Area           | Number of Test Cases |
| -------------- | -------------------- |
| Authentication | 6                    |
| Products       | 18                   |
| Carts          | 15                   |
| **Total**      | **39**               |

