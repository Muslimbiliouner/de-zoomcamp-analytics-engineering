import duckdb
from pathlib import Path

con = duckdb.connect()

RAW_PATH = "data"
PARQUET_PATH = "data/parquet"

Path(PARQUET_PATH).mkdir(parents=True, exist_ok=True)

print("Converting Green CSV to Parquet...")
con.execute(f"""
COPY (
    SELECT * FROM read_csv_auto('{RAW_PATH}/green_tripdata_*.csv.gz')
)
TO '{PARQUET_PATH}/green_tripdata.parquet'
(FORMAT PARQUET, COMPRESSION ZSTD);
""")

print("Converting Yellow CSV to Parquet...")
con.execute(f"""
COPY (
    SELECT * FROM read_csv_auto('{RAW_PATH}/yellow_tripdata_*.csv.gz')
)
TO '{PARQUET_PATH}/yellow_tripdata.parquet'
(FORMAT PARQUET, COMPRESSION ZSTD);
""")

print("Done.")
