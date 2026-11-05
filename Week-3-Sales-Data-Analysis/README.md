# Week 3: Introduction to Data Analysis — Working with Real Data

**Level:** Intermediate  
**Assignment deadline:** November 12, 2026

## Project overview
Use Python and pandas to explore, clean, and analyse a sales dataset. Calculate useful metrics, identify the best-selling product, and present findings in a clear report.

## Theory concepts
- Data analysis: inspecting and interpreting data to answer questions.
- Pandas: a Python library with spreadsheet-like tools for rows and columns.
- CSV files: load tabular data with pandas read_csv().
- Data exploration: inspect first rows, shape, columns, and data types.
- Data cleaning: handle missing or invalid values and remove duplicates.
- Statistics: calculate mean, maximum, minimum, and totals.

## Dataset
The supplied sales_data.csv contains 100 rows and 7 columns: Date, Product, Quantity, Price, Customer_ID, Region, and Total_Sales. The brief mentions five columns, but the uploaded dataset has seven. All seven original columns are retained to preserve the supplied data.

## Repository structure
Week-3-Sales-Data-Analysis/
- README.md
- sales_analysis.py
- sales_data.csv
- analysis_report.md
- requirements.txt
- test_cases.txt

## Setup instructions
1. Install Python 3.10 or newer.
2. Open this folder in VS Code or Command Prompt.
3. Install pandas: py -m pip install -r requirements.txt
4. Run the program: py sales_analysis.py
5. Open analysis_report.md to read the generated report.

## Five-day work plan
| Day | Work |
|---|---|
| Day 1 | Install pandas, create the Python file, and load the CSV |
| Day 2 | Explore rows, columns, shape, and data types |
| Day 3 | Check missing values, handle invalid values, and remove duplicates |
| Day 4 | Calculate revenue, statistics, and the best-selling product |
| Day 5 | Generate the report, review findings, and capture screenshots |

## Analysis process
1. Read the CSV file using pandas.
2. Display the first five rows and dataset dimensions.
3. Inspect column names, data types, and missing-value counts.
4. Remove duplicate rows.
5. Convert numeric columns and handle invalid or missing values.
6. Calculate missing Total_Sales using Quantity multiplied by Price where possible.
7. Calculate total revenue, average sale, highest sale, and lowest sale.
8. Group sales by product and identify the product with the highest revenue.
9. Save results and findings to analysis_report.md.

## Technical details
- Library: pandas
- Input: CSV file
- Main data structure: pandas DataFrame
- Cleaning: duplicate removal, numeric conversion, and missing-value handling
- Analysis: sum(), mean(), max(), min(), and groupby()
- Output: formatted Markdown report

## Screenshots and testing evidence
Run the program on your computer and capture genuine screenshots showing:
- the terminal running sales_analysis.py
- the first rows and dataset information
- the final metrics and best-selling product
- the generated analysis_report.md

Save screenshots in a screenshots/ folder if required by your submission portal. No execution screenshots are included because they must come from your own computer.

## Quality checklist
- [x] Project overview and objectives
- [x] Setup instructions
- [x] Organised code and comments
- [x] Dataset included
- [x] Missing-value and duplicate handling
- [x] At least three metrics
- [x] Formatted report
- [x] Test cases and validation guidance
- [ ] Add your own execution screenshots after running the program

## Submission files
Submit sales_analysis.py, sales_data.csv, analysis_report.md, and requirements.txt. Include this README and test cases as supporting documentation.
