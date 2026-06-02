# 📊 Mutual Fund Data Pipeline - Day 1

## Objective
To build a data ingestion pipeline for mutual fund NAV data using MFAPI.

## Data Source
- MFAPI (https://api.mfapi.in)

## Schemes Used
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip

## Process
- Fetched NAV data using API
- Parsed JSON response
- Converted into structured DataFrame
- Stored raw data in CSV format

## Output
- `data/raw/all_funds_nav.csv`

## Status
✔ Data ingestion completed successfully  
✔ API integration working  
✔ Dataset ready for further analysis
