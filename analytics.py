import pandas as pd

# ---------------------------------------------------------
# Load and prepare the dataset
# ---------------------------------------------------------

def load_data(filepath="data/sales.csv"):
    """
    Loads the sales dataset, cleans it, and prepares it for analysis.
    """
    try:
        df = pd.read_csv(filepath)

        # Convert dates
        df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")

        # Drop rows with invalid dates
        df = df.dropna(subset=["OrderDate"])

        # Fill missing numeric values
        numeric_cols = ["Sales", "Profit", "Quantity"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = df[col].fillna(0)

        # Fill missing text values
        text_cols = ["Product", "Category", "CustomerSegment", "Region"]
        for col in text_cols:
            if col in df.columns:
                df[col] = df[col].fillna("Unknown")

        # Create Month column for trend charts
        df["Month"] = df["OrderDate"].dt.to_period("M").astype(str)

        return df

    except FileNotFoundError:
        print("ERROR: sales.csv not found in /data folder.")
        return None


# ---------------------------------------------------------
# Summary Metrics
# ---------------------------------------------------------

def total_sales(df):
    return df["Sales"].sum()

def total_profit(df):
    return df["Profit"].sum()

def total_orders(df):
    return len(df)

def average_order_value(df):
    if len(df) == 0:
        return 0
    return df["Sales"].sum() / len(df)

def best_category(df):
    category_totals = df.groupby("Category")["Sales"].sum()
    return category_totals.idxmax(), category_totals.max()

def best_product(df):
    product_totals = df.groupby("Product")["Sales"].sum()
    return product_totals.idxmax(), product_totals.max()


# ---------------------------------------------------------
# Monthly Sales Trend
# ---------------------------------------------------------

def monthly_sales(df):
    """
    Returns a DataFrame grouped by Month with total Sales.
    """
    return df.groupby("Month")["Sales"].sum().reset_index()


# ---------------------------------------------------------
# Category Performance
# ---------------------------------------------------------

def category_performance(df):
    """
    Returns total Sales and Profit grouped by Category.
    """
    return df.groupby("Category")[["Sales", "Profit"]].sum().reset_index()


# ---------------------------------------------------------
# Top Products
# ---------------------------------------------------------

def top_products(df, n=10):
    """
    Returns the top N products by Sales.
    """
    return df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(n).reset_index()


# ---------------------------------------------------------
# Customer Segment Analysis
# ---------------------------------------------------------

def customer_segments(df):
    """
    Returns total Sales grouped by Customer Segment.
    """
    return df.groupby("CustomerSegment")["Sales"].sum().reset_index()
