import pytest
import logging
from apis.auth_api import AuthClient

logger = logging.getLogger(__name__)


@pytest.fixture
def auth_client():
    return AuthClient()


@pytest.mark.auth
def test_valid_login(auth_client):
    response = auth_client.login("mor_2314", "83r5^_")
    
    assert response.status_code in [200, 201]
    assert "token" in response.json()
    token = response.json()["token"]
    assert isinstance(token, str)
    assert len(token) > 0
    logger.info(f"Login successful, token: {token[:20]}...")

@pytest.mark.auth
def test_login_without_body(auth_client):
    response = auth_client.login(None,None)
    print(response.status_code)
    assert response.status_code == 400

@pytest.mark.auth
def test_login_invalid_username(auth_client):
    response = auth_client.login("basem", "2020")
    
    assert response.status_code == 401


@pytest.mark.auth
def test_login_invalid_password(auth_client):
    response = auth_client.login("mor_2314", "wpassword")
    
    assert response.status_code == 401

@pytest.mark.auth
def test_login_with_very_long_username(auth_client):
    long_username = "a" * 200
    response = auth_client.login(long_username, "pass123")

    assert response.status_code in [400, 401]


@pytest.mark.auth
def test_login_empty_credentials(auth_client):
    response = auth_client.login("", "")
    
    assert response.status_code in [400, 401]
