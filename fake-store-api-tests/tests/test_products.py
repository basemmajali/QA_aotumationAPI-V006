import pytest
import logging
import json
import os
from jsonschema import validate
from apis.products_api import ProductsClient
from config.config import config

logger = logging.getLogger(__name__)


@pytest.fixture
def products_client():
    
    return ProductsClient()


@pytest.fixture
def product_schema():
    schema_path = os.path.join(os.path.dirname(__file__), "../schemas/product_schema.json")
    with open(schema_path) as f:
        return json.load(f)


@pytest.mark.products
def test_get_all_products(products_client):
    response = products_client.get_all_products()
    
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0


@pytest.mark.products
def test_get_product_by_valid_id(products_client):
    response = products_client.get_product_by_id(1)
    
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert "title" in product
    assert "price" in product
    assert "category" in product


@pytest.mark.products
@pytest.mark.negative
def test_get_product_by_invalid_id(products_client):
    response = products_client.get_product_by_id(-1)
    
    assert response.status_code == 200


@pytest.mark.products
def test_get_product_nonexistent_id(products_client):
    response = products_client.get_product_by_id(99999)
    
    assert response.status_code == 200


@pytest.mark.products
def test_get_all_categories(products_client):
    response = products_client.get_categories()
    
    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)
    assert len(categories) > 0
    assert "electronics" in categories
    assert "jewelery" in categories


@pytest.mark.products
def test_get_products_with_limit(products_client):
    limit = 5
    response = products_client.get_products_with_limit(limit)
    
    assert response.status_code == 200
    products = response.json()
    assert len(products) == limit


@pytest.mark.products
def test_get_products_limit_zero(products_client):
    response = products_client.get_products_with_limit(0)
    
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)


@pytest.mark.products
def test_get_products_sorted_ascending(products_client):
    response = products_client.get_products_sorted("asc")
    
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0


@pytest.mark.products
def test_get_products_sorted_descending(products_client):
    response = products_client.get_products_sorted("desc")
    
    assert response.status_code == 200
    products = response.json()
    assert len(products) > 0


@pytest.mark.products
def test_product_schema_validation(products_client, product_schema):
    response = products_client.get_product_by_id(1)
    
    assert response.status_code == 200
    product = response.json()
    
    validate(instance=product, schema=product_schema)


@pytest.mark.products
def test_get_products_response_time(products_client):
    import time
    
    start = time.time()
    response = products_client.get_all_products()
    elapsed = time.time() - start
    
    assert response.status_code == 200
    assert elapsed < 3.0
    logger.info(f"Response time: {elapsed:.2f}s")


@pytest.mark.products
def test_single_product_has_all_required_fields(products_client):
    response = products_client.get_product_by_id(1)
    
    assert response.status_code == 200
    product = response.json()
    
    required_fields = ["id", "title", "price", "category", "description", "image"]
    for field in required_fields:
        assert field in product, f"Missing required field: {field}"

@pytest.mark.products
@pytest.mark.negative
def test_get_products_with_invalid_limit(products_client):
    response = products_client.get_products_with_limit(-5)
    
    assert response.status_code in [200, 400]


@pytest.mark.products
@pytest.mark.negative
def test_get_products_with_string_limit(products_client):
    client = ProductsClient()
    response = client.get("/products?limit=abc")
    
    assert response.status_code in [200, 400]


@pytest.mark.products
@pytest.mark.negative
def test_get_products_with_very_large_limit(products_client):
    response = products_client.get_products_with_limit(999999)
    
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)


@pytest.mark.products
@pytest.mark.negative
def test_invalid_category_filter(products_client):
    response = products_client.get("/products/category/nonexistent")
    
    assert response.status_code in [404, 200]
    data = response.json()
    if isinstance(data, list):
        assert len(data) == 0


@pytest.mark.products
@pytest.mark.negative
def test_get_product_with_string_id(products_client):
    response = products_client.get("/products/abc")
    
    assert response.status_code == 200


@pytest.mark.products
@pytest.mark.negative
def test_get_product_with_special_characters(products_client):
    response = products_client.get("/products/!@#$%")
    
    assert response.status_code == 200
