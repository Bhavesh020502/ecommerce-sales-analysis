import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="ecommerce",
    user="postgres",
    password="123456789"
)

print("Connected to database successfully")

# Load data
query = "SELECT * FROM ecommerce_sales;"
df = pd.read_sql(query, conn)

print(df.head())
print("Shape:", df.shape)



