import pandas as pd
from analytics import (
    load_data,
    total_sales,
    total_profit,
    total_orders,
    average_order_value,
    best_category,
    best_product,
    monthly_sales,
    category_performance,
    top_products,
    customer_segments
)
from charts import (
    chart_monthly_sales,
    chart_category_performance,
    chart_top_products,
    chart_customer_segments,
    chart_profit_forecast
)

# ---------------------------------------------------------
# Dashboard Menu
# ---------------------------------------------------------

def show_summary(df):
    print("\n========== SUMMARY METRICS ==========")
    print(f"Total Sales: ${total_sales(df):,.2f}")
    print(f"Total Profit: ${total_profit(df):,.2f}")
    print(f"Total Orders: {total_orders(df):,}")
    print(f"Average Order Value: ${average_order_value(df):,.2f}")

    category, cat_sales = best_category(df)
    print(f"Best Category: {category} (${cat_sales:,.2f})")

    product, prod_sales = best_product(df)
    print(f"Best Product: {product} (${prod_sales:,.2f})")
    print("=====================================\n")


def main():
    df = load_data()

    if df is None:
        print("Dataset could not be loaded.")
        return

    while True:
        print("\n========== SALES DASHBOARD ==========")
        print("1. View Summary Metrics")
        print("2. Monthly Sales Trend")
        print("3. Category Performance")
        print("4. Top 10 Products")
        print("5. Customer Segment Analysis")
        print("6. Profit Forecast")
        print("7. Exit")
        print("=====================================")

        choice = input("Choose an option: ")

        if choice == "1":
            show_summary(df)

        elif choice == "2":
            chart_monthly_sales(df)

        elif choice == "3":
            chart_category_performance(df)

        elif choice == "4":
            chart_top_products(df)

        elif choice == "5":
            chart_customer_segments(df)

        elif choice == "6":
            chart_profit_forecast(df)

        elif choice == "7":
            print("Exiting dashboard...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
