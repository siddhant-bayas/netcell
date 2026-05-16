## 🚀 Quickstart Guide

Get up and running with NetCell in under 60 seconds.

### 1. Create and Save Data

```python
import netcell

# Initialize a new database
db = netcell.create("inventory.ncell")
products = db.create_sheet("products")

# Add data
products.add_row({"id": 1, "name": "Laptop", "price": 1200.50, "category": "Electronics"})
products.add_row({"id": 2, "name": "Desk Chair", "price": 250.00, "category": "Furniture"})

# Save to disk with compression
db.save(compress=True)

```

### 2. Querying Data (Programmatic)

```python
from netcell import open as open_nc

db = open_nc("inventory.ncell")
sheet = db.sheet("products")

# Fluent Query Builder
results = sheet.where("price", ">", 500).select("name", "price").execute()

for row in results.rows:
    print(f"Item: {row['name']} | Price: {row['price']}")

```

### 3. Querying Data (SQL)

```python
# Use the full power of SQLite on your columnar file
results = db.sql("SELECT category, AVG(price) FROM products GROUP BY category")
print(results)

```