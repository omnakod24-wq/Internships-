# Week 3 — Sales Data Analysis Report

## Project overview
This report analyses the supplied 100-row sales dataset using Python and pandas.

## Dataset overview
- Rows: **100**
- Columns: **7**
- Columns: Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales
- Missing values in the supplied file: **0**
- Duplicate rows in the supplied file: **0**

## Key metrics
- **Total revenue:** ₹12,365,048.00
- **Average sale:** ₹123,650.48
- **Highest sale:** ₹373,932.00
- **Lowest sale:** ₹6,540.00
- **Best-selling product by revenue:** Laptop
- **Best-selling product by units sold:** Laptop

## Sales by product

| Product | Total Revenue (₹) | Records |
|---|---:|---:|
| Laptop | 3,889,210.00 | 24 |
| Tablet | 2,884,340.00 | 26 |
| Phone | 2,859,394.00 | 20 |
| Headphones | 1,384,033.00 | 15 |
| Monitor | 1,348,071.00 | 15 |

## Findings
1. Laptop has the highest total revenue in the supplied dataset.
2. Laptop is also the leading product by total units sold.
3. Tablet has the largest number of records (26), but not the highest revenue.
4. The dataset contains records from January 1, 2024 to April 9, 2024.

## Data cleaning
The supplied CSV currently has no missing values and no duplicate rows. The Python script still includes checks to remove duplicates, convert data types, fill suitable text fields, and calculate missing Total_Sales values using Quantity multiplied by Price.

## Conclusion
Pandas can load, explore, clean, group, and summarize sales records efficiently. The results above describe only this supplied practice dataset.
