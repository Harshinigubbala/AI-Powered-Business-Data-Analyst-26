

from pathlib import Path
import pandas as pd

# Dataset location
DATA_PATH = Path("data/raw/Online Retail.xlsx")


def load_data(path=DATA_PATH):
    """Load, validate, clean, and prepare UCI Online Retail data."""

    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {path}. "
            "Download Online Retail.xlsx from the UCI repository "
            "and save it inside data/raw/."
        )

    # Load dataset
    df = pd.read_excel(path)

    # Validate required columns
    required = {
        "InvoiceNo",
        "StockCode",
        "Description",
        "Quantity",
        "InvoiceDate",
        "UnitPrice",
        "Country"
    }

    missing = required - set(df.columns)

    if missing:
        raise ValueError(
            f"Dataset is missing required columns: {sorted(missing)}"
        )

    # Convert identifiers into strings
    df["InvoiceNo"] = df["InvoiceNo"].astype(str).str.strip()
    df["StockCode"] = df["StockCode"].astype(str).str.strip()

    # Convert dates and numeric columns
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"], errors="coerce"
    )

    df["Quantity"] = pd.to_numeric(
        df["Quantity"], errors="coerce"
    )

    df["UnitPrice"] = pd.to_numeric(
        df["UnitPrice"], errors="coerce"
    )

    # Clean text columns
    df["Country"] = df["Country"].astype("string").str.strip()

    df["Description"] = (
        df["Description"]
        .fillna("Unknown product")
        .astype(str)
        .str.strip()
    )

    # Remove rows with missing required analysis values
    df = df.dropna(
        subset=[
            "InvoiceDate",
            "Quantity",
            "UnitPrice",
            "Country"
        ]
    )

    # Remove cancelled invoices and invalid sales rows
    df = df[
        ~df["InvoiceNo"].str.upper().str.startswith("C")
        & (df["Quantity"] > 0)
        & (df["UnitPrice"] > 0)
        & (df["Country"] != "")
    ].copy()

    # Calculate sales
    df["Sales"] = df["Quantity"] * df["UnitPrice"]

    # Extract date information
    df["Year"] = df["InvoiceDate"].dt.year
    df["Month"] = df["InvoiceDate"].dt.month

    df["Year-Month"] = (
        df["InvoiceDate"]
        .dt.to_period("M")
        .astype(str)
    )

    return df


def get_business_summary(df):
    """Calculate overall business performance metrics."""

    return {
        "Total Sales (£)": float(round(df["Sales"].sum(), 2)),
        "Total Quantity": int(df["Quantity"].sum()),
        "Total Invoices": int(df["InvoiceNo"].nunique()),
        "Countries": int(df["Country"].nunique())
    }


def get_product_analysis(df):
    """Analyze sales and quantity by product."""

    return (
        df.groupby("Description", dropna=False)
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Invoice_Count=("InvoiceNo", "nunique")
        )
        .reset_index()
        .sort_values(
            "Total_Sales",
            ascending=False
        )
    )


def get_country_analysis(df):
    """Analyze business performance by country."""

    return (
        df.groupby("Country")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Invoice_Count=("InvoiceNo", "nunique")
        )
        .reset_index()
        .sort_values(
            "Total_Sales",
            ascending=False
        )
    )


def get_monthly_analysis(df):
    """Analyze monthly sales performance."""

    return (
        df.groupby("Year-Month")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Invoice_Count=("InvoiceNo", "nunique")
        )
        .reset_index()
        .sort_values("Year-Month")
    )


def get_yearly_analysis(df):
    """Analyze yearly sales performance."""

    return (
        df.groupby("Year")
        .agg(
            Total_Sales=("Sales", "sum"),
            Total_Quantity=("Quantity", "sum"),
            Invoice_Count=("InvoiceNo", "nunique")
        )
        .reset_index()
        .sort_values("Year")
    )


if __name__ == "__main__":

    data = load_data()

    print("UCI ONLINE RETAIL DATA ANALYSIS")
    print("-" * 40)

    print("Prepared rows:", len(data))

    print("\nBusiness Summary:")
    print(get_business_summary(data))

    print("\nTop 10 Countries by Sales:")
    print(
        get_country_analysis(data)
        .head(10)
        .round(2)
        .to_string(index=False)
    )

    print("\nTop 10 Products by Sales:")
    print(
        get_product_analysis(data)
        .head(10)
        .round(2)
        .to_string(index=False)
    )

    print("\nMonthly Sales Analysis:")
    print(
        get_monthly_analysis(data)
        .round(2)
        .to_string(index=False)
    )

    print("\nYearly Sales Analysis:")
    print(
        get_yearly_analysis(data)
        .round(2)
        .to_string(index=False)
    )
