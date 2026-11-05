"""Week 3: Sales Data Analysis using Python and pandas.

Loads the sales CSV, explores and cleans the data, calculates metrics,
and writes a formatted Markdown report.
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "sales_data.csv"
REPORT_FILE = BASE_DIR / "analysis_report.md"

REQUIRED_COLUMNS = {
    "Date", "Product", "Quantity", "Price",
    "Customer_ID", "Region", "Total_Sales"
}


def load_data(file_path):
    """Read the CSV and check that all required columns are present."""
    if not file_path.exists():
        raise FileNotFoundError(f"Dataset not found: {file_path}")

    data = pd.read_csv(file_path)
    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(
            "CSV is missing required columns: "
            + ", ".join(sorted(missing_columns))
        )
    return data


def explore_data(data):
    """Display first rows, dimensions, data types, and missing values."""
    print("\n--- First 5 Rows ---")
    print(data.head())
    print("\n--- Dataset Shape ---")
    print(f"Rows: {data.shape[0]}, Columns: {data.shape[1]}")
    print("\n--- Column Names ---")
    print(data.columns.tolist())
    print("\n--- Data Types and Non-null Counts ---")
    data.info()
    print("\n--- Missing Values Before Cleaning ---")
    print(data.isnull().sum())


def clean_data(data):
    """Remove duplicates and handle missing or invalid values."""
    cleaned = data.copy()
    starting_rows = len(cleaned)

    # Remove exact duplicate records.
    cleaned = cleaned.drop_duplicates()

    # Convert date and numeric columns to appropriate data types.
    cleaned["Date"] = pd.to_datetime(cleaned["Date"], errors="coerce")
    for column in ["Quantity", "Price", "Total_Sales"]:
        cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    # Replace missing descriptive values with a clear label.
    cleaned["Product"] = cleaned["Product"].fillna("Unknown")
    cleaned["Region"] = cleaned["Region"].fillna("Unknown")
    cleaned["Customer_ID"] = cleaned["Customer_ID"].fillna("Unknown")

    # Rows without a valid date, quantity, or price cannot be analysed.
    cleaned = cleaned.dropna(subset=["Date", "Quantity", "Price"])

    # Calculate missing sales values from quantity multiplied by price.
    missing_sales = cleaned["Total_Sales"].isna()
    cleaned.loc[missing_sales, "Total_Sales"] = (
        cleaned.loc[missing_sales, "Quantity"]
        * cleaned.loc[missing_sales, "Price"]
    )

    # Remove impossible negative quantities, prices, or sales.
    cleaned = cleaned[
        (cleaned["Quantity"] >= 0)
        & (cleaned["Price"] >= 0)
        & (cleaned["Total_Sales"] >= 0)
    ].copy()

    print("\n--- Cleaning Summary ---")
    print(f"Rows before cleaning: {starting_rows}")
    print(f"Rows after cleaning: {len(cleaned)}")
    print("\n--- Missing Values After Cleaning ---")
    print(cleaned.isnull().sum())
    return cleaned


def analyse_sales(data):
    """Calculate key metrics and summarize sales by product."""
    total_revenue = data["Total_Sales"].sum()
    average_sale = data["Total_Sales"].mean()
    highest_sale = data["Total_Sales"].max()
    lowest_sale = data["Total_Sales"].min()

    product_summary = (
        data.groupby("Product")
        .agg(
            Total_Revenue=("Total_Sales", "sum"),
            Units_Sold=("Quantity", "sum"),
            Number_of_Records=("Product", "count"),
        )
        .sort_values("Total_Revenue", ascending=False)
    )

    best_product = (
        product_summary.index[0] if not product_summary.empty else "N/A"
    )

    return {
        "total_revenue": total_revenue,
        "average_sale": average_sale,
        "highest_sale": highest_sale,
        "lowest_sale": lowest_sale,
        "product_summary": product_summary,
        "best_product": best_product,
    }


def create_report(data, metrics):
    """Create and save a formatted Markdown report."""
    summary = metrics["product_summary"]
    lines = [
        "# Week 3 — Sales Data Analysis Report",
        "",
        "## Project overview",
        "This report analyses the supplied sales dataset using Python and pandas.",
        "",
        "## Dataset overview",
        f"- Rows after cleaning: **{len(data)}**",
        f"- Columns: **{data.shape[1]}**",
        f"- Products analysed: **{data['Product'].nunique()}**",
        f"- Regions analysed: **{data['Region'].nunique()}**",
        f"- Duplicate rows remaining: **{data.duplicated().sum()}**",
        "",
        "## Key metrics",
        f"- Total revenue: **₹{metrics['total_revenue']:,.2f}**",
        f"- Average sale: **₹{metrics['average_sale']:,.2f}**",
        f"- Highest sale: **₹{metrics['highest_sale']:,.2f}**",
        f"- Lowest sale: **₹{metrics['lowest_sale']:,.2f}**",
        f"- Best-selling product by revenue: **{metrics['best_product']}**",
        "",
        "## Sales by product",
        "| Product | Total Revenue (₹) | Units Sold | Records |",
        "|---|---:|---:|---:|",
    ]

    for product, row in summary.iterrows():
        lines.append(
            f"| {product} | {row['Total_Revenue']:,.2f} "
            f"| {row['Units_Sold']:,.0f} "
            f"| {row['Number_of_Records']:,.0f} |"
        )

    lines.extend([
        "",
        "## Findings",
        f"- **{metrics['best_product']}** generated the highest total revenue.",
        "- The product table compares revenue and units sold for each product.",
        "- The summary metrics describe overall sales in the supplied dataset.",
        "",
        "## Data cleaning",
        "The script checks missing values, converts date and numeric fields, "
        "removes duplicate rows, and calculates missing Total_Sales values "
        "from Quantity multiplied by Price where possible.",
        "",
        "## Conclusion",
        "Pandas makes it easier to load, clean, group, and summarize sales data. "
        "These results describe only the supplied practice dataset.",
        "",
    ])

    REPORT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print("\n" + "\n".join(lines))
    print(f"\nReport saved to: {REPORT_FILE}")


def main():
    """Run the complete data analysis workflow."""
    try:
        sales_data = load_data(DATA_FILE)
        explore_data(sales_data)
        cleaned_data = clean_data(sales_data)

        if cleaned_data.empty:
            raise ValueError("No valid records remain after data cleaning.")

        metrics = analyse_sales(cleaned_data)
        create_report(cleaned_data, metrics)
    except (FileNotFoundError, ValueError, pd.errors.ParserError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
