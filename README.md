# Module 4 – Analytics Engineering with dbt

This repository contains my solution for **Module 4 – Analytics Engineering** from the Data Engineering Zoomcamp.

## 📌 Project Overview

In this project, I used:

- **dbt Core**
- **DuckDB**
- **Docker**
- NYC Taxi dataset (Green & Yellow taxis 2019–2020)

The goal is to transform raw trip data into analytics-ready models using modern ELT practices.

---

## 🏗 Architecture

Raw Data (CSV.gz)  
⬇  
DuckDB (prod schema)  
⬇  
dbt Staging Models  
⬇  
Intermediate Models  
⬇  
Fact & Dimension Models  
⬇  
Monthly Revenue Aggregation

---

## 📂 Project Structure

```

taxi_rides_ny/
│
├── models/
│   ├── staging/
│   ├── intermediate/
│   └── marts/
│
├── seeds/
├── macros/
├── dbt_project.yml
├── packages.yml
└── README.md

````

---

## ⚙️ Setup Instructions

### 1️⃣ Run Docker Container

```bash
docker run -it \
  -v $(pwd)/taxi_rides_ny:/app/taxi_rides_ny \
  -v $(pwd)/profiles:/root/.dbt \
  dbt-zoomcamp
````

---

### 2️⃣ Install Dependencies

```bash
dbt deps
```

---

### 3️⃣ Load Raw Taxi Data

Inside DuckDB:

```sql
CREATE SCHEMA IF NOT EXISTS prod;

CREATE OR REPLACE TABLE prod.green_tripdata AS
SELECT * FROM read_csv_auto('data/green_tripdata_*.csv.gz');

CREATE OR REPLACE TABLE prod.yellow_tripdata AS
SELECT * FROM read_csv_auto('data/yellow_tripdata_*.csv.gz');
```

---

### 4️⃣ Run dbt Models

```bash
dbt seed --target prod
dbt run --target prod
```

---

## 📊 Final Models Created

* `prod.stg_green_tripdata`
* `prod.stg_yellow_tripdata`
* `prod.int_trips`
* `prod.fct_trips`
* `prod.dim_zones`
* `prod.dim_vendors`
* `prod.fct_monthly_zone_revenue`

---

## 📈 Homework Results

### ✅ Q1

`dbt run --select int_trips_unioned` builds:

**int_trips_unioned**

---

### ✅ Q2

If payment_type = 6 appears:

**dbt fails the test with a non-zero exit code**

---

### ✅ Q3

Count of records in `fct_monthly_zone_revenue`:

**12,184**

---

### ✅ Q4

Highest Green taxi revenue zone in 2020:

**East Harlem North**

---

### ✅ Q5

Total Green taxi trips in October 2019:

**384,624**

---

### ✅ Q6
Count of records in `stg_fhv_tripdata` (2019, excluding NULL dispatching_base_num):

**43,244,693**

---

## 🧠 Key Learnings

* dbt model materialization strategies (view vs incremental)
* Surrogate key generation
* Data quality testing
* Model lineage and dependencies
* Handling large datasets in DuckDB
* Memory optimization for analytical workloads

---

## 🔗 Course Reference

Data Engineering Zoomcamp
[https://github.com/DataTalksClub/data-engineering-zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)

---

🚀 Built as part of my journey toward becoming a Data Engineer.
