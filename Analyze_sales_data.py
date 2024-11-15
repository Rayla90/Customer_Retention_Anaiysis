import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv("customer_retention_sales_data.csv")

# Analyze the data: Retention rates
retention_counts = data["Retention"].value_counts()
retention_labels = ["Retained", "Not Retained"]

# Create a pie chart for retention
plt.figure(figsize=(6, 6))
plt.pie(
retention_counts,
labels=retention_labels,
autopct="%1.1f%%",
startangle=90,
colors=["green", "red"],
)
plt.title("Customer Retention Rates")
plt.savefig("retention_pie_chart.png")
print("Pie chart saved as 'retention_pie_chart.png'.")

# Analyze satisfaction vs. spending
plt.figure(figsize=(8, 5))
plt.scatter(data["Satisfaction"], data["MonthlySpending"], color="blue")
plt.title("Customer Satisfaction vs Monthly Spending")
plt.xlabel("Satisfaction (1-5)")
plt.ylabel("Monthly Spending ($)")
plt.savefig("satisfaction_vs_spending.png")
print("Scatter plot saved as 'satisfaction_vs_spending.png'.")
