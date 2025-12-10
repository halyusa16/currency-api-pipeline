"""
Main pipeline runner
"""

from .fetch import fetch_data
from .transform import transform_data
from .load import load_data
from .logger import get_logger

logger = get_logger()

def main():
    logger.info("Starting currency exchange pipeline. . .")

    data = fetch_data()
    rows = transform_data(data)
    load_data(rows)

    logger.info("Yeay, pipeline completed successfully!")

if __name__ == "__main__":
    main()