"""Week 4: End-to-end e-commerce sales analysis and visualization."""

from pathlib import Path
import matplotlib
matplotlib.use("Agg")  # Save charts without requiring a graphical display.
import matplotlib.pyplot as plt
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
CHART_DIR = BASE_DIR / "visualizations"
REPORT_DIR = BASE_DIR / "report"
REQUIRED_COLUMNS = {
    "Date", "Product", "Quantity", "Price",
    "Customer_ID", "Region", "Total_Sales"
}


def load_and_clean_data(file_path):
    """Load the CSV, validate its structure, and clean unusable records."""
    if not file_path.is_file():
        raise FileNotFoundError(f"Dataset was not found: {file_path}")

    data = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    original_rows = len(data)
    data = data.drop_duplicates().copy()

    # Convert values to suitable types; invalid conversions become missing.
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    for column in ["Quantity", "Price", "Total_Sales"]:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    # Remove rows that cannot contribute to the main sales analysis.
    data = data.dropna(
        subset=["Date", "Product", "Quantity", "Price", "Total_Sales"]
    ).copy()
    data["Region"] = data["Region"].fillna("Unknown").astype(str)
    data["Product"] = data["Product"].astype(str).str.strip()
    data = data[data["Product"] != ""]

    if data.empty:
        raise ValueError("The dataset has no valid rows after cleaning.")

    print(f"Rows before cleaning: {original_rows}")
    print(f"Rows after cleaning:  {len(data)}")
    print(f"Duplicate rows removed: {original_rows - len(data)}")
    return data


def analyze_data(data):
    """Calculate summary metrics and grouped sales totals."""
    product_sales = data.groupby("Product")["Total_Sales"].sum().sort_values(
        ascending=False
    )
    region_sales = data.groupby("Region")["Total_Sales"].sum().sort_values(
        ascending=False
    )
    monthly_sales = (
        data.assign(Month=data["Date"].dt.to_period("M").astype(str))
        .groupby("Month")["Total_Sales"].sum()
        .sort_index()
    )

    metrics = {
        "records": len(data),
        "total_sales": data["Total_Sales"].sum(),
        "average_sale": data["Total_Sales"].mean(),
        "highest_sale": data["Total_Sales"].max(),
        "lowest_sale": data["Total_Sales"].min(),
        "total_quantity": data["Quantity"].sum(),
        "date_start": data["Date"].min().date(),
        "date_end": data["Date"].max().date(),
    }
    return metrics, product_sales, region_sales, monthly_sales


def create_visualizations(product_sales, region_sales, monthly_sales):
    """Create and save a bar chart, line chart, and pie chart."""
    CHART_DIR.mkdir(parents=True, exist_ok=True)

    plt.figure(figsize=(9, 5))
    product_sales.plot(kind="bar", title="Total Sales by Product", rot=25)
    plt.xlabel("Product")
    plt.ylabel("Total sales")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "sales_by_product.png", dpi=150)
    plt.close()

    plt.figure(figsize=(9, 5))
    monthly_sales.plot(kind="line", marker="o", title="Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Total sales")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig(CHART_DIR / "monthly_sales_trend.png", dpi=150)
    plt.close()

    plt.figure(figsize=(7, 7))
    region_sales.plot(
        kind="pie", autopct="%1.1f%%", startangle=90,
        title="Share of Sales by Region"
    )
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "sales_by_region.png", dpi=150)
    plt.close()


def write_report(metrics, product_sales, region_sales, monthly_sales):
    """Write numerical results and data-driven insights to Markdown."""
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    best_product = product_sales.idxmax()
    best_region = region_sales.idxmax()
    best_month = monthly_sales.idxmax()
    low_month = monthly_sales.idxmin()

    product_table = "\n".join(
        f"| {name} | {value:,.2f} |" for name, value in product_sales.items()
    )
    region_table = "\n".join(
        f"| {name} | {value:,.2f} |" for name, value in region_sales.items()
    )

    report = f"""# E-commerce Sales Analysis Report

## 1. Project overview
This report analyzes the supplied sample sales dataset to understand product performance, regional contribution, and monthly revenue patterns.

## 2. Dataset summary
- Valid records analyzed: {metrics['records']}
- Date range: {metrics['date_start']} to {metrics['date_end']}
- Total quantity sold: {metrics['total_quantity']:,.0f}
- Products analyzed: {len(product_sales)}
- Regions analyzed: {len(region_sales)}

## 3. Key metrics
| Metric | Result |
|---|---:|
| Total revenue | {metrics['total_sales']:,.2f} |
| Average transaction value | {metrics['average_sale']:,.2f} |
| Highest transaction | {metrics['highest_sale']:,.2f} |
| Lowest transaction | {metrics['lowest_sale']:,.2f} |

## 4. Revenue by product
| Product | Total revenue |
|---|---:|
{product_table}

## 5. Revenue by region
| Region | Total revenue |
|---|---:|
{region_table}

## 6. Insights
- **Top product:** {best_product} generated the highest total revenue ({product_sales.iloc[0]:,.2f}).
- **Top region:** {best_region} contributed the most revenue ({region_sales.iloc[0]:,.2f}).
- **Strongest month:** {best_month} had the highest monthly revenue ({monthly_sales.max():,.2f}).
- **Lowest month:** {low_month} had the lowest monthly revenue ({monthly_sales.min():,.2f}).
- The product bar chart supports comparison of product revenue; the monthly line chart shows the direction of sales over time; the regional pie chart compares each region's share.

## 7. Visualizations
- [Sales by product](../visualizations/sales_by_product.png)
- [Monthly sales trend](../visualizations/monthly_sales_trend.png)
- [Sales share by region](../visualizations/sales_by_region.png)

## 8. Method and limitations
The program uses Pandas for CSV loading, cleaning, grouping, and summary calculations, and Matplotlib for chart creation. Invalid dates and numeric values are converted to missing values; records missing essential analysis fields are excluded; duplicate rows are removed. This is a practice dataset, so the findings describe only these sample records and cannot establish real-world business causes.
"""
    report_path = REPORT_DIR / "analysis_report.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report saved to: {report_path}")


def main():
    """Run the full load-clean-analyze-visualize-report pipeline."""
    try:
        data = load_and_clean_data(DATA_FILE)
        metrics, product_sales, region_sales, monthly_sales = analyze_data(data)
        print("\nKey metrics")
        print(f"Total revenue: {metrics['total_sales']:,.2f}")
        print(f"Average sale:  {metrics['average_sale']:,.2f}")
        print(f"Highest sale:  {metrics['highest_sale']:,.2f}")
        print(f"Lowest sale:   {metrics['lowest_sale']:,.2f}")
        create_visualizations(product_sales, region_sales, monthly_sales)
        write_report(metrics, product_sales, region_sales, monthly_sales)
        print("Charts saved in the visualizations folder.")
        print("Analysis completed successfully.")
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Analysis could not be completed: {error}")


if __name__ == "__main__":
    main()
