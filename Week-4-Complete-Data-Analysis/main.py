"""Week 4: End-to-end sales data analysis with two visualizations."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "sales_data.csv"
CHART_DIR = BASE_DIR / "visualizations"
REPORT_DIR = BASE_DIR / "report"
REQUIRED_COLUMNS = {"Date", "Product", "Quantity", "Price", "Customer_ID", "Region", "Total_Sales"}

def load_and_clean_data(path):
    if not path.exists():
        raise FileNotFoundError(f"Dataset not found: {path}")
    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Dataset is missing columns: {sorted(missing)}")
    df = df.drop_duplicates().copy()
    df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
    for col in ["Quantity", "Price", "Total_Sales"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["Date", "Product", "Quantity", "Price", "Total_Sales"])
    df["Region"] = df["Region"].fillna("Unknown")
    return df

def create_visualizations(df):
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(9, 5))
    product_sales.plot(kind="bar", title="Total Sales by Product", ylabel="Sales")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "sales_by_product.png")
    plt.close()

    region_sales = df.groupby("Region")["Total_Sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(7, 7))
    region_sales.plot(kind="pie", autopct="%1.1f%%", title="Sales Share by Region")
    plt.ylabel("")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "sales_by_region.png")
    plt.close()
    return product_sales, region_sales

def write_report(df, product_sales, region_sales):
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    best_product = product_sales.idxmax()
    best_region = region_sales.idxmax()
    report = f"""# Complete Data Analysis Report

## Dataset overview
- Records after cleaning: {len(df)}
- Date range: {df['Date'].min().date()} to {df['Date'].max().date()}
- Products: {df['Product'].nunique()}
- Regions: {df['Region'].nunique()}

## Key metrics
- Total sales: {df['Total_Sales'].sum():,.2f}
- Average sale: {df['Total_Sales'].mean():,.2f}
- Highest sale: {df['Total_Sales'].max():,.2f}
- Lowest sale: {df['Total_Sales'].min():,.2f}

## Insights
- Best product by total sales: **{best_product}**.
- Highest-revenue region: **{best_region}**.
- Compare the two charts in the visualizations folder to identify product and regional patterns.

## Files generated
- `visualizations/sales_by_product.png`
- `visualizations/sales_by_region.png`

## Limitations
This is a generated practice dataset. Results describe only the sample records and should not be treated as real business performance.
"""
    (REPORT_DIR / "analysis_report.md").write_text(report, encoding="utf-8")
    print(report)

def main():
    try:
        data = load_and_clean_data(DATA_FILE)
        product_sales, region_sales = create_visualizations(data)
        write_report(data, product_sales, region_sales)
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Could not complete analysis: {error}")

if __name__ == "__main__":
    main()
