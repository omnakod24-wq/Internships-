# Week 4 — Data Visualization & Complete Data Analysis

**Project:** E-commerce Sales Analysis  
**Tools:** Python, Pandas, Matplotlib

## Project overview
This project demonstrates a complete data analysis workflow: loading a CSV file, validating and cleaning records, calculating sales metrics, creating charts, and explaining the results in a written report.

### Objectives
- Explore a dataset with Pandas.
- Handle missing values, invalid values, and duplicate rows.
- Calculate total, average, highest, and lowest sales.
- Compare revenue by product and region.
- Study monthly sales trends.
- Present findings using clear charts and written insights.

## Dataset
The supplied CSV contains **100 rows and 7 columns**: Date, Product, Quantity, Price, Customer_ID, Region, and Total_Sales. The assignment brief mentions 5 columns; this project accurately documents the actual supplied file.

## Folder structure
```text
Week-4-Complete-Data-Analysis/
├── README.md
├── main.py
├── requirements.txt
├── test_cases.txt
├── data/
│   └── sales_data.csv
├── visualizations/
│   └── (generated PNG charts)
├── report/
│   └── analysis_report.md
└── screenshots/
    └── (add your genuine screenshots here)
```

## Setup and run
1. Install Python 3.10 or later.
2. Open a terminal in this project directory.
3. Install the required libraries:

```bash
py -m pip install -r requirements.txt
```

4. Run the project:

```bash
py main.py
```

The script uses paths relative to its own location, so you do not need to edit the CSV path.

## Charts created
- **Bar chart:** total sales revenue by product.
- **Line chart:** monthly sales revenue over time.
- **Pie chart:** share of total sales by region.

All charts include titles and clear labels and are saved as PNG files in visualizations/.

## Technical workflow
1. **Load:** Pandas reads the CSV dataset.
2. **Validate:** the program checks that all required columns exist.
3. **Clean:** it converts dates and numeric values, removes duplicate records, fills missing region labels, and excludes rows missing essential analysis fields.
4. **Analyze:** groupby operations calculate product, region, and monthly sales; summary metrics are calculated.
5. **Visualize:** Matplotlib creates and saves three chart types.
6. **Report:** a Markdown report is generated with metrics, insights, and chart references.

The code is divided into functions for readability and includes error handling for missing files, malformed CSV files, missing columns, and datasets with no valid rows.

## How to interpret the charts
- Taller bars represent products with higher total revenue.
- The line chart shows whether monthly revenue rises or falls over the available period.
- Larger pie slices represent regions contributing a larger share of total revenue.

## Testing evidence
See test_cases.txt for validation checks. After running the script, confirm that all three PNG files and the Markdown report have been created. Add your actual terminal and chart screenshots to a screenshots/ folder before submission.

## Seven-day plan
| Day | Work |
|---|---|
| 1–2 | Select the e-commerce topic, inspect the CSV, prepare folders |
| 3 | Load, validate, clean, and explore the dataset |
| 4 | Calculate summary metrics and identify patterns |
| 5 | Create bar, line, and pie charts |
| 6 | Generate the report and write insights |
| 7 | Test the project, fix errors, and capture screenshots |

## Learning resources
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/tutorials/
- Python: https://docs.python.org/3/

**Note:** This is a practice dataset. Findings describe only the supplied sample and should not be treated as real business performance.
