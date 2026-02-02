import pytest
import json
import os
from jsonschema import validate
from apis.carts_api import CartsClient


@pytest.fixture
def carts_client():
    return CartsClient()


@pytest.fixture
def cart_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "../schemas/cart_schema.json")
    with open(schema_path) as f:
        return json.load(f)


@pytest.mark.carts
def test_get_all_carts(carts_client):
    response = carts_client.get_all_carts()
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)
    assert len(carts) > 0


@pytest.mark.carts
def test_get_carts_by_valid_user_id(carts_client):
    user_id = 1
    response = carts_client.get_carts_by_user(user_id)
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_by_invalid_user_id(carts_client):
    response = carts_client.get_carts_by_user(99999)
    assert response.status_code in [200, 404]
    data = response.json()
    if isinstance(data, list):
        assert len(data) == 0


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_by_negative_user_id(carts_client):
    response = carts_client.get_carts_by_user(-1)
    assert response.status_code in [200, 400, 404]


@pytest.mark.carts
def test_get_carts_with_date_range(carts_client):
    response = carts_client.get_carts_by_date("2024-01-01", "2024-12-31")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
def test_get_carts_with_invalid_date_format(carts_client):
    response = carts_client.get_carts_by_date("01/01/2024", "12/31/2024")
    assert response.status_code in [200, 400]


@pytest.mark.carts
def test_get_carts_with_future_date_range(carts_client):
    response = carts_client.get_carts_by_date("2025-01-01", "2026-12-31")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
def test_get_carts_sorted_ascending(carts_client):
    response = carts_client.get_carts_sorted("asc")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
def test_get_carts_sorted_descending(carts_client):
    response = carts_client.get_carts_sorted("desc")
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
def test_get_carts_with_limit(carts_client):
    limit = 3
    response = carts_client.get_carts_with_limit(limit)
    assert response.status_code == 200
    carts = response.json()
    assert len(carts) <= limit


@pytest.mark.carts
def test_cart_schema_validation(carts_client, cart_schema):
    response = carts_client.get_carts_by_user(1)
    assert response.status_code == 200
    carts = response.json()
    if len(carts) > 0:
        validate(instance=carts[0], schema=cart_schema)


@pytest.mark.carts
def test_cart_contains_required_fields(carts_client):
    response = carts_client.get_carts_by_user(1)
    assert response.status_code == 200
    carts = response.json()
    if len(carts) > 0:
        cart = carts[0]
        required_fields = ["id", "userId", "date", "products"]
        for field in required_fields:
            assert field in cart, f"Missing required field: {field}"
