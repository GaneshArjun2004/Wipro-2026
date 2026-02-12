import pandas as pd
import numpy as np
import os

CSV_FILE = "sales.csv"

# =================================================
# STEP 0: CREATE CSV IF MISSING OR EMPTY
# =================================================
def create_csv():
    print("Creating sales.csv with sample data...")

    data = {
        "Date": ["01-01-2025", "02-01-2025", "03-01-2025", "04-01-2025"],
        "Product": ["A", "B", "A", "C"],
        "Quantity": [10, 20, 15, 25],
        "Price": [50, 30, 40, 20]
    }

    df = pd.DataFrame(data)
    df.to_csv(CSV_FILE, index=False)
    print("sales.csv created successfully\n")


# Create file if not exists or empty
if not os.path.exists(CSV_FILE) or os.path.getsize(CSV_FILE) == 0:
    create_csv()


# =================================================
# STEP 1: LOAD CSV INTO PANDAS DATAFRAME
# =================================================
try:
    df = pd.read_csv(CSV_FILE)
    print("CSV loaded successfully\n")

except Exception as e:
    print("Error loading CSV:", e)
    exit()

print("Initial Data:")
print(df)


# =================================================
# STEP 2: ADD TOTAL COLUMN
# =================================================
df["Total"] = df["Quantity"] * df["Price"]
print("\n'Total' column added")


# =================================================
# STEP 3: NUMPY CALCULATIONS
# =================================================
daily_sales = df["Total"].values

total_sales = np.sum(daily_sales)
avg_daily_sales = np.mean(daily_sales)
std_dev_sales = np.std(daily_sales)

print("\nSales Analysis:")
print("Total Sales:", total_sales)
print("Average Daily Sales:", avg_daily_sales)
print("Standard Deviation:", std_dev_sales)


# =================================================
# STEP 4: BEST-SELLING PRODUCT
# =================================================
product_sales = df.groupby("Product")["Quantity"].sum()
best_product = product_sales.idxmax()

print("\nBest-selling product:", best_product)


# =================================================
# FINAL OUTPUT
# =================================================
print("\nFinal Data with Total Column:")
print(df)
