import matplotlib.pyplot as plt

# ---------------------------------------------------------
# Monthly Sales Trend Chart
# ---------------------------------------------------------

def chart_monthly_sales(df):
    monthly = df.groupby("Month")["Sales"].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["Month"], monthly["Sales"], marker="o", color="blue")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Category Performance Chart
# ---------------------------------------------------------

def chart_category_performance(df):
    category = df.groupby("Category")["Sales"].sum().reset_index()

    plt.figure(figsize=(10, 5))
    plt.bar(category["Category"], category["Sales"], color="green")
    plt.title("Category Performance")
    plt.xlabel("Category")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Top Products Chart
# ---------------------------------------------------------

def chart_top_products(df, n=10):
    top = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(n).reset_index()

    plt.figure(figsize=(10, 5))
    plt.bar(top["Product"], top["Sales"], color="purple")
    plt.title(f"Top {n} Products by Sales")
    plt.xlabel("Product")
    plt.ylabel("Sales")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Customer Segment Chart
# ---------------------------------------------------------

def chart_customer_segments(df):
    segments = df.groupby("CustomerSegment")["Sales"].sum().reset_index()

    plt.figure(figsize=(8, 8))
    plt.pie(segments["Sales"], labels=segments["CustomerSegment"], autopct="%1.1f%%")
    plt.title("Customer Segment Sales Distribution")
    plt.tight_layout()
    plt.show()


# ---------------------------------------------------------
# Profit Forecast Chart (Simple Linear Trend)
# ---------------------------------------------------------

def chart_profit_forecast(df):
    monthly = df.groupby("Month")["Profit"].sum().reset_index()

    # Convert Month to numeric index for regression
    monthly["Index"] = range(len(monthly))

    # Simple linear regression
    x = monthly["Index"]
    y = monthly["Profit"]

    slope = (y.iloc[-1] - y.iloc[0]) / (x.iloc[-1] - x.iloc[0])
    intercept = y.iloc[0]

    forecast = intercept + slope * x

    plt.figure(figsize=(10, 5))
    plt.plot(monthly["Month"], monthly["Profit"], marker="o", label="Actual Profit")
    plt.plot(monthly["Month"], forecast, linestyle="--", color="red", label="Forecast Trend")
    plt.title("Profit Forecast")
    plt.xlabel("Month")
    plt.ylabel("Profit")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
