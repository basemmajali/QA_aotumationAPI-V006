import requests
from config.config import config
from logger import get_logger

logger = get_logger(__name__)


class APIClient:
    def __init__(self, base_url=config.BASE_URL):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        self.timeout = config.REQUEST_TIMEOUT

    def get(self, endpoint):
        """Execute GET request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Request | GET {endpoint}")
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            self._log_response("GET", endpoint, None, response)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def post(self, endpoint, json_data=None):
        """Execute POST request."""
        url = f"{self.base_url}{endpoint}"
        logger.info(f"Request | POST {endpoint} | Payload: {json_data}")
        try:
            response = requests.post(url, json=json_data, headers=self.headers, timeout=self.timeout)
            self._log_response("POST", endpoint, json_data, response)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def _log_response(self, method: str, endpoint: str, payload, response):
        """Log the response details."""
        try:
            body = response.json()
        except ValueError:
            body = response.text

        logger.info(
            f"Response | {method} {endpoint} | "
            f"Status: {response.status_code} | "
            f"Payload: {payload} | "
            f"Body: {body}"
        )
