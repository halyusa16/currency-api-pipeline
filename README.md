# currency-api-pipeline

## Project Overview

This project demonstrates an ETL pipeline for a real-time currency exchange rate data. The pipeline fetches real-time foreign exchange rates from a public API, transforms the nested JSON response into a normalized tabular format, and loads the data in a SQLite database with timestamps for historical tracking.

## Project Structure

```
currency_pipeline/
├── src/
│   ├── config.py          # Centralized configuration (API URL, DB path, table name)
│   ├── fetch.py           # Extract: API data retrieval
│   ├── transform.py       # Transform: JSON to tabular conversion
│   ├── load.py            # Load: SQLite database operations
│   ├── logger.py          # Logging configuration and setup
│   └── main.py            # Pipeline orchestration and execution
├── data/
│   └── exchange_rates.db  # SQLite database (auto-created on first run)
└── requirements.txt       # Python dependencies
```

### Tools Used

- **Language**: Python
- **Database**: SQLite
- **Python Libraries**:
  - `logging`: For logging the execution processes.
  - `requests`: For interacting with the API.
  - `datetime`: For providing timestamp.

## Data Pipeline Architecture

### Extract (fetch.py)

- The extraction layer connects to the Open Exchange Rates API (`https://open.er-api.com/v6/latest/USD`) to retrieve current exchange rates.
- Returns raw JSON containing exchange rates for multiple currencies relative to USD as the base currency.

### Transform (transform.py)

- The transformation layer converts nested JSON into a flat, database-ready structure.
- Each currency-rate pair is extracted from the JSON object and converted into individual rows.
- A UTC timestamp is added to every row, enabling time-series analysis of exchange rate fluctuations.
- The output is a list of dictionaries with a consistent schema: `timestamp`, `currency`, `rate`.


### Load (load.py)

- The loading layer stores extracted data using SQLite3.
- The database schema supports incremental loading—each pipeline run adds new timestamped records without overwriting historical data.

## Pipeline Orchestration

The `main.py` module serves as the pipeline controller, coordinating the three ETL stages:

1. **fetch_data()**: Retrieves raw data from external API
2. **transform_data()**: Processes and structures the data
3. **load_data()**: Loads transformed data to database

Each stage is logged with timestamps and status messages, providing full observability into pipeline execution.

Error handling at each stage ensures failures are caught and logged appropriately.

Example data:

| timestamp | currency | rate |
|-----------|----------|------|
| 2025-12-10T08:30:00+00:00 | EUR | 0.92 |
| 2025-12-10T08:30:00+00:00 | JPY | 150.7 |
| 2025-12-10T08:30:00+00:00 | IDR | 15400.12 |


## Business Value and Use Cases

While this demonstrates a learning project, the pattern has real-world applications:

**Financial Analytics**: Track currency fluctuations for international business planning, or portfolio management.

**Data Warehousing**: The ETL pattern shown here scales to production data pipelines with more complex transformations and multiple data sources.

**Incremental Loading**: The append-only pattern supports scheduled runs (via cron or Airflow) to build historical datasets over time.
