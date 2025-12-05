import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create charts folder
os.makedirs("charts", exist_ok=True)

# Load dataset
df = pd.read_csv("data/sales.csv")
df['date'] = pd.to_datetime(df['date'])
df['revenue'] = df['quantity'] * df['price']
# KPIs
total_revenue = df['revenue'].sum()
avg_order_value = df['revenue'].mean()
top_region = df.groupby('region')['revenue'].sum().idxmax()

print("Total Revenue:", total_revenue)
print("Average Order Value:", avg_order_value)
print("Top Performing Region:", top_region)

# Monthly sales trend

df['month'] = df['date'].dt.to_period('M')

monthly_sales = df.groupby('month')['revenue'].sum()

plt.figure(figsize=(7,4))
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Revenue Trend")
plt.ylabel("Revenue")
plt.savefig("charts/monthly_sales.png")
plt.close()

# Top Products

top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)

plt.figure(figsize=(7,4))
sns.barplot(x=top_products.index, y=top_products.values)
plt.title("Top Products by Revenue")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.savefig("charts/top_products.png")
plt.close()

# Region Revenue

region_rev = df.groupby('region')['revenue'].sum()

plt.figure(figsize=(6,6))
plt.pie(region_rev, labels=region_rev.index, autopct="%1.1f%%")
plt.title("Revenue Share by Region")
plt.savefig("charts/region_revenue.png")
plt.close()

print("\nCharts saved in the 'charts' folder.")
print("Analysis complete!")
