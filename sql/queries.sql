-- 1. Top 5 funds by NAV
SELECT amfi_code, MAX(nav) as max_nav
FROM fact_nav
GROUP BY amfi_code
ORDER BY max_nav DESC
LIMIT 5;

-- 2. Average NAV per month
SELECT amfi_code, strftime('%Y-%m', date) as month, AVG(nav)
FROM fact_nav
GROUP BY amfi_code, month;

-- 3. SIP YoY growth
SELECT amfi_code, SUM(amount)
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY amfi_code;

-- 4. Transactions by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 5. Expense ratio < 1%
SELECT amfi_code
FROM fact_performance
WHERE expense_ratio < 1;

-- 6. Highest AUM funds
SELECT amfi_code, MAX(aum)
FROM fact_aum
GROUP BY amfi_code;

-- 7. Monthly transaction volume
SELECT strftime('%Y-%m', date), SUM(amount)
FROM fact_transactions
GROUP BY strftime('%Y-%m', date);

-- 8. Top performing funds (1Y return)
SELECT amfi_code, return_1y
FROM fact_performance
ORDER BY return_1y DESC
LIMIT 5;

-- 9. Risk check (high expense ratio)
SELECT amfi_code
FROM fact_performance
WHERE expense_ratio > 2;

-- 10. NAV volatility proxy
SELECT amfi_code, MAX(nav) - MIN(nav) as volatility
FROM fact_nav
GROUP BY amfi_code;