"""
Load data into SQLite database
"""

import sqlite3
from .config import DB_PATH, TABLE_NAME
from .logger import get_logger

logger = get_logger()

def create_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(f"""
        CREATE TABLE IF NOT EXISTS {TABLE_NAME}(
            timestamp TEXT,
            currency TEXT,
            rate REAL)
            """)
    
    conn.commit()
    conn.close()


def load_data(rows):
    logger.info("Loading data into SQLite... wkaka")

    create_table()

    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    for row in rows:
        cur.execute(f"""
            INSERT INTO {TABLE_NAME}
            (timestamp, currency, rate)
            VALUES (?, ?, ?)
            """, 
            (row["timestamp"], 
                row["currency"], 
                row["rate"]))
        
    conn.commit()
    conn.close()

    logger.info(f"Loaded {len(rows)} rows into database.")