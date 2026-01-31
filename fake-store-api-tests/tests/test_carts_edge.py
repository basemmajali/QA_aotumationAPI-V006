import pytest
import logging
from apis.carts_api import CartsClient

logger = logging.getLogger(__name__)


@pytest.fixture
def carts_client():
    return CartsClient()


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_invalid_sort_parameter(carts_client):
    response = carts_client.get("/carts?sort=invalid")
    
    assert response.status_code in [200, 400]


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_with_zero_limit(carts_client):
    response = carts_client.get_carts_with_limit(0)
    
    assert response.status_code == 200
    carts = response.json()
    assert isinstance(carts, list)


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_with_negative_limit(carts_client):
    response = carts_client.get_carts_with_limit(-5)
    
    assert response.status_code in [200, 400]


@pytest.mark.carts
@pytest.mark.negative
def test_get_carts_start_date_after_end_date(carts_client):
    response = carts_client.get_carts_by_date("2024-12-31", "2024-01-01")
    
    assert response.status_code in [200, 400]
    data = response.json()
    if isinstance(data, list):
        assert len(data) == 0


@pytest.mark.carts
@pytest.mark.negative
def test_get_user_carts_with_string_id(carts_client):
    response = carts_client.get("/carts/user/abc")
    
    assert response.status_code in [200, 400, 404]
