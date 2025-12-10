"""
Parses and transforms JSON into rows
"""

from datetime import datetime, timezone
from .logger import get_logger

logger = get_logger()

def transform_data(data):
    logger.info("Transforming data...")

    timestamp = datetime.now().isoformat()

    rates = data.get("rates", {})

    rows = []
    for currency, rate in rates.items():
        rows.append({
            "timestamp": timestamp,
            "currency": currency,
            "rate": rate
        })

    logger.info(f"Generated {len(rows)} rows of rates.")
    return rows