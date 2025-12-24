import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="123456789"
)

# Load data
query = "SELECT * FROM ecommerce_sales;"
df = pd.read_sql(query, conn)

# Basic cleaning
df = df[df['quantity'] > 0]
df['sales'] = df['quantity'] * df['unitprice']

# CREATE sales_by_country (THIS WAS MISSING)
sales_by_country = (
    df.groupby('country')['sales']
    .sum()
    .sort_values(ascending=False)
)

# Plot Top 10 Countries
top_countries = sales_by_country.head(10)

top_countries.plot(kind='bar', figsize=(10,5))
plt.title("Top 10 Countries by Sales")
plt.xlabel("Country")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

