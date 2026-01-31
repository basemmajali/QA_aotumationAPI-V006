import requests
import logging
from config.config import config

logger = logging.getLogger(__name__)


class APIClient:
    def __init__(self, base_url=config.BASE_URL):
        self.base_url = base_url
        self.headers = {
            "Content-Type": "application/json"
        }
        self.timeout = config.REQUEST_TIMEOUT

    def get(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"GET {url}")
        try:
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            logger.info(f"Status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise

    def post(self, endpoint, json_data=None):
        url = f"{self.base_url}{endpoint}"
        logger.info(f"POST {url}")
        try:
            response = requests.post(url, json=json_data, headers=self.headers, timeout=self.timeout)
            logger.info(f"Status: {response.status_code}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Request failed: {e}")
            raise
            return response
