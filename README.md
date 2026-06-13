# Bluestock Mutual Fund Analytics Platform

## Project Overview

The Bluestock Mutual Fund Analytics Platform is an end-to-end data engineering, analytics, and business intelligence project developed to analyze the Indian mutual fund industry. The platform integrates data ingestion, ETL processing, financial performance analysis, risk analytics, and interactive dashboard reporting into a unified workflow.

The project processes multiple mutual fund datasets covering scheme information, historical NAV data, AUM statistics, SIP inflows, folio growth, portfolio holdings, investor transactions, benchmark indices, and scheme performance metrics.

The objective is to provide meaningful insights for investors, analysts, and fund managers through data-driven decision making.

---

## Project Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Store cleaned data in a structured SQLite database.
* Perform Exploratory Data Analysis (EDA).
* Calculate mutual fund performance metrics.
* Conduct advanced risk analytics.
* Build an interactive Power BI dashboard.
* Generate investor-oriented recommendations.
* Produce comprehensive project documentation.

---

## Technology Stack

| Component               | Technology                |
| ----------------------- | ------------------------- |
| Programming Language    | Python                    |
| Data Processing         | Pandas, NumPy             |
| Visualization           | Matplotlib, Plotly        |
| Database                | SQLite                    |
| Dashboard               | Power BI                  |
| Version Control         | Git & GitHub              |
| Development Environment | VS Code, Jupyter Notebook |

---

## Project Architecture

Raw Data (CSV Files)
↓
Data Ingestion
↓
ETL Pipeline
↓
Processed Datasets
↓
SQLite Database
↓
Analytics & Performance Metrics
↓
Power BI Dashboard
↓
Business Insights & Recommendations

---

## Repository Structure

```text
capstone_project/
│
├── dashboard/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── database/
│
├── notebooks/
│
├── reports/
│   ├── Figures/
│   ├── Metrics/
│   ├── Final_Report.pdf
│   └── Bluestock_MF_Presentation.pptx
│
├── scripts/
│
├── sql/
│
├── README.md
├── requirements.txt
├── data_dictionary.md
└── run_pipeline.py
```

---

## Datasets Used

The project utilizes ten datasets:

1. Fund Master Dataset
2. NAV History Dataset
3. AUM by Fund House Dataset
4. Monthly SIP Inflows Dataset
5. Category Inflows Dataset
6. Industry Folio Count Dataset
7. Scheme Performance Dataset
8. Investor Transactions Dataset
9. Portfolio Holdings Dataset
10. Benchmark Indices Dataset

These datasets collectively represent scheme information, investor activity, fund performance, portfolio composition, and industry growth trends.

---

## ETL Pipeline

The ETL pipeline performs the following operations:

### Data Extraction

* Read raw CSV datasets
* Validate schema consistency

### Data Transformation

* Missing value handling
* Duplicate removal
* Date standardization
* Numeric validation
* Data quality checks
* Feature engineering

### Data Loading

* Export cleaned datasets
* Load processed data into SQLite database

---

## Performance Metrics

The project calculates multiple financial performance metrics:

### Return Metrics

* Daily Return
* CAGR (1-Year, 3-Year, 5-Year)

### Risk Metrics

* Volatility
* Sharpe Ratio
* Sortino Ratio
* Maximum Drawdown

### Benchmark Metrics

* Alpha
* Beta
* Tracking Error

### Advanced Risk Analytics

* Value at Risk (VaR)
* Conditional Value at Risk (CVaR)
* Rolling Sharpe Ratio

---

## Exploratory Data Analysis

EDA was conducted to understand:

* Industry AUM growth trends
* SIP inflow patterns
* Investor folio growth
* Sector allocation
* Portfolio concentration
* Benchmark performance
* Investor demographics
* Category-wise fund flows

Key visualizations are available in the reports/Figures directory.

---

## Advanced Analytics

Additional analytical modules include:

### Fund Recommendation Engine

Provides mutual fund recommendations based on investor risk profiles:

* Conservative
* Moderate
* Aggressive

### Portfolio Analytics

* Sector concentration analysis
* Diversification assessment

### Benchmark Analysis

* Fund vs Benchmark comparison
* Performance attribution

---

## Power BI Dashboard

The interactive dashboard consists of four analytical pages:

### Industry Overview

* Total AUM
* SIP Inflows
* Folio Growth
* Industry Trends

### Fund Performance

* Return Analysis
* CAGR Comparison
* Sharpe Ratio Analysis

### Investor Analytics

* Demographic Distribution
* Transaction Analysis
* Investment Patterns

### SIP & Market Trends

* SIP Growth
* Benchmark Performance
* Market Insights

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sagilisunandhaReddy/capstone_project.git
```

Navigate to project directory:

```bash
cd capstone_project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

Run the ETL pipeline:

```bash
python run_pipeline.py
```

Open Jupyter notebooks for analysis:

```bash
jupyter notebook
```

Open the Power BI dashboard:

```text
dashboard/bluestock_mf_dashboard.pbix
```

---

## Project Deliverables

* Final_Report.pdf
* Bluestock_MF_Presentation.pptx
* Power BI Dashboard
* SQLite Database
* Python ETL Pipeline
* Analytics Reports
* GitHub Repository

---

## Key Findings

* Mutual fund industry AUM demonstrated sustained growth.
* SIP participation increased consistently over time.
* Risk-adjusted returns varied significantly across schemes.
* Financial Services emerged as a dominant portfolio sector.
* Benchmark tracking quality differed across funds.
* Investor participation expanded across demographic segments.

---

## Future Enhancements

* Machine Learning based return forecasting.
* Portfolio optimization models.
* Real-time NAV integration.
* Automated dashboard refresh.
* Cloud database deployment.
* Advanced recommendation algorithms.

---

## Author

Sunanda Reddy

Bluestock Mutual Fund Analytics Capstone Project

2026

