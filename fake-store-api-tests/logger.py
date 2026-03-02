import logging
import sys

# Configure logging to file
handler = logging.FileHandler("logs.log")
handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s"))
logging.root.addHandler(handler)
logging.root.setLevel(logging.INFO)

def get_logger(name: str = __name__):
    return logging.getLogger(name)