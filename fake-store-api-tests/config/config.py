import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class Config:
    BASE_URL = "https://fakestoreapi.com"
    REQUEST_TIMEOUT = 10
    LOG_LEVEL = "INFO"
    LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    REPORT_PATH = os.path.join(BASE_DIR, "reports", "report.html")
    VALID_USER_ID = 1
    INVALID_USER_ID = 99999
    VALID_PRODUCT_ID = 1
    INVALID_PRODUCT_ID = -1

config = Config()
