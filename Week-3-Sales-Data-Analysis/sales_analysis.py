"""Week 3: Clean and analyse a sales CSV using pandas."""
from pathlib import Path
import pandas as pd

DATA_FILE = Path(__file__).with_name("sales_data.csv")
REPORT_FILE = Path(__file__).with_name("analysis_report.md")

def main():
    df = pd.read_csv(DATA_FILE)
    print("Original shape:", df.shape)
    print("\nColumns:", list(df.columns))
    print("\nData types:\n", df.dtypes)

    df = df.drop_duplicates().copy()
    numeric_columns = ["Quantity", "Price", "Total_Sales"]
    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df[numeric_columns] = df[numeric_columns].fillna(0)
    df["Product"] = df["Product"].fillna("Unknown")
    df["Region"] = df["Region"].fillna("Unknown")

    if "Total_Sales" not in df.columns:
        df["Total_Sales"] = df["Quantity"] * df["Price"]

    total_revenue = df["Total_Sales"].sum()
    average_sale = df["Total_Sales"].mean()
    highest_sale = df["Total_Sales"].max()
    lowest_sale = df["Total_Sales"].min()
    product_revenue = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False)
    best_product = product_revenue.index[0] if not product_revenue.empty else "N/A"

    report = (
        "# Sales Analysis Report\n\n"
        f"- Cleaned records: {len(df)}\n"
        f"- Total revenue: {total_revenue:,.2f}\n"
        f"- Average sale: {average_sale:,.2f}\n"
        f"- Highest sale: {highest_sale:,.2f}\n"
        f"- Lowest sale: {lowest_sale:,.2f}\n"
        f"- Best product by revenue: {best_product}\n\n"
        "## Revenue by Product\n\n"
        + product_revenue.to_string()
        + "\n"
    )
    REPORT_FILE.write_text(report, encoding="utf-8")
    print(report)
    print(f"Report saved to {REPORT_FILE.name}")

if __name__ == "__main__":
    main()
