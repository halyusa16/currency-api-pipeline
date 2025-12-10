"""
Fetches data from API
"""

import requests
from .config import API_URL
from .logger import get_logger

logger = get_logger()

def fetch_data():
    logger.info("Fetching data from API...")

    response = requests.get(API_URL)
    response.raise_for_status()

    data = response.json()
    logger.info("Data fetched successfully.")

    return data