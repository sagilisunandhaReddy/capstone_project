-- 1. Top 5 Funds by AUM

SELECT scheme_name,aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV Per Month

SELECT
strftime('%Y-%m',date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 3. SIP YoY Growth

SELECT
month,
yoy_growth_pct
FROM monthly_sip_inflows;

-- 4. Transactions by State

SELECT
state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- 5. Funds with Expense Ratio Below 1%

SELECT
scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Average Return by Category

SELECT
category,
AVG(return_5yr_pct)
FROM fact_performance
GROUP BY category;

-- 7. Average Sharpe Ratio by Risk Grade

SELECT
risk_grade,
AVG(sharpe_ratio)
FROM fact_performance
GROUP BY risk_grade;

-- 8. Investments by City Tier

SELECT
city_tier,
SUM(amount_inr)
FROM fact_transactions
GROUP BY city_tier;

-- 9. Investments by Gender

SELECT
gender,
SUM(amount_inr)
FROM fact_transactions
GROUP BY gender;

-- 10. Top Performing Funds (5Y Return)

SELECT
scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
