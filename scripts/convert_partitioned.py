import duckdb
from pathlib import Path

con = duckdb.connect()

RAW_PATH = "data"
PARQUET_PATH = "data/parquet"

Path(PARQUET_PATH).mkdir(parents=True, exist_ok=True)

print("Converting GREEN partitioned...")
con.execute(f"""
COPY (
    SELECT *,
           year(lpep_pickup_datetime) as year,
           month(lpep_pickup_datetime) as month
    FROM read_csv_auto('{RAW_PATH}/green_tripdata_*.csv.gz')
)
TO '{PARQUET_PATH}/green'
(FORMAT PARQUET, PARTITION_BY (year, month), COMPRESSION ZSTD);
""")

print("Converting YELLOW partitioned...")
con.execute(f"""
COPY (
    SELECT *,
           year(tpep_pickup_datetime) as year,
           month(tpep_pickup_datetime) as month
    FROM read_csv_auto('{RAW_PATH}/yellow_tripdata_*.csv.gz')
)
TO '{PARQUET_PATH}/yellow'
(FORMAT PARQUET, PARTITION_BY (year, month), COMPRESSION ZSTD);
""")

print("Done.")
