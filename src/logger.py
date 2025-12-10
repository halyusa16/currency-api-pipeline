"""
Logger for tracking pipeline runs
"""

import logging

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)s] [%(message)s]",
        datefmt="%Y-%m-%d %H: %M: %S",
    )
    return logging.getLogger("currency_pipeline")