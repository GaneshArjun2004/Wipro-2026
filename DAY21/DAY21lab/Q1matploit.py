import matplotlib.pyplot as plt
import seaborn as sns

# Dataset
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# Create figure with two subplots
plt.figure(figsize=(12, 5))

# -------------------------------
# 1️⃣ Line Chart using Matplotlib
# -------------------------------
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend (Matplotlib)")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

# -------------------------------
# 2️⃣ Bar Plot using Seaborn
# -------------------------------
plt.subplot(1, 2, 2)
sns.barplot(x=months, y=sales)
plt.title("Monthly Sales Distribution (Seaborn)")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)

# Adjust layout
plt.tight_layout()

# Save the figure
plt.savefig("monthly_sales_report.png")

# Display the plots
plt.show()