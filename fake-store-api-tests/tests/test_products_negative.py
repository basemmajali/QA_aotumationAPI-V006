import pytest
import logging
from apis.products_api import ProductsClient

logger = logging.getLogger(__name__)


@pytest.fixture
def products_client():
    
    return ProductsClient()


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
