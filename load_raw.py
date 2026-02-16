import duckdb
import requests
from pathlib import Path

BASE_URL = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download"
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

con = duckdb.connect("taxi_rides_ny.duckdb")
con.execute("CREATE SCHEMA IF NOT EXISTS prod")

for taxi_type in ["yellow", "green"]:
    for year in [2019, 2020]:
        for month in range(1, 13):
            file = f"{taxi_type}_tripdata_{year}-{month:02d}.csv.gz"
            url = f"{BASE_URL}/{taxi_type}/{file}"
            path = DATA_DIR / file

            if not path.exists():
                print(f"Downloading {file}")
                r = requests.get(url)
                r.raise_for_status()
                with open(path, "wb") as f:
                    f.write(r.content)

    print(f"Loading {taxi_type} data...")
    con.execute(f"""
        CREATE OR REPLACE TABLE prod.{taxi_type}_tripdata AS
        SELECT * FROM read_csv_auto('data/{taxi_type}_tripdata_*.csv.gz')
    """)

con.close()
print("Done loading raw tables.")
