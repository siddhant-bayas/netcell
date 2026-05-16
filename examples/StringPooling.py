import netcell

db = netcell.create("catalog.ncell")
items = db.create_sheet("products")

for i in range(10000):
    items.add_row({
        "sku": f"SKU-{i}",
        "category": "Electronics", # Pooled
        "status": "In Stock"       # Pooled
    })

db.save() 