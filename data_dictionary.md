# Data Dictionary - Bluestock MF Capstone

## nav_history_clean.csv
- amfi_code: Unique fund identifier
- date: NAV date (datetime)
- nav: Net Asset Value of fund

## investor_transactions_clean.csv
- investor_id: Unique investor ID
- amfi_code: Fund identifier
- transaction_type: SIP / LUMPSUM / REDEMPTION
- amount: Transaction amount (> 0)
- kyc_status: YES/NO

## scheme_performance_clean.csv
- return_1y: 1 year return %
- return_3y: 3 year return %
- return_5y: 5 year return %
- expense_ratio: Fund expense ratio (%)

## Sources
- MFAPI
- Internal simulated investor dataset