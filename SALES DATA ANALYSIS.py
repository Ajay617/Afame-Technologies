#SALES DATA ANALYSIS

import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('ECOMM DATA.xlsx')

total_sales = df['Sales'].sum()

print('Total Sales:', total_sales)

# Convert 'Order Date' to datetime format

df['Order Date'] = pd.to_datetime(df['Order Date'])

#Group by month and calulate total sales

monthly_sales = df.resample('ME', on='Order Date')['Sales'].sum()

#Plotting sales trends over time

plt.figure(figsize=(10,6))
sns.lineplot(data=monthly_sales)
plt.xlabel('Month')
plt.ylabel('Sales')
plt.title('Sales Trends Over Time')
plt.show()

# Group by 'Product Name' and calculate total sales
product_sales = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False)

# Display top N best-selling products
N = 5
top_products = product_sales.head(N)
print('Top', N, 'Best-Selling Products:')
print(top_products)

# Bar chart for best-selling products
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar')
plt.xlabel('Product Name')
plt.ylabel('Total Sales')
plt.title('Top Best-Selling Products')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()





