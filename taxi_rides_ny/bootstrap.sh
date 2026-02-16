#!/bin/bash

echo "Installing dependencies..."
dbt deps

echo "Loading raw data..."
python load_raw.py

echo "Building dbt models..."
dbt build --target prod

echo "DONE."
