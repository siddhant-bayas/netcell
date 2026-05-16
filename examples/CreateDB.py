import netcell

# Initialize a new database file
db = netcell.create("company_records.ncell")

# Create a sheet for employees
employees = db.create_sheet("employees")

# Add rows as dictionaries
employees.add_row({"id": 101, "name": "Alice", "dept": "Engineering", "salary": 95000})
employees.add_row({"id": 102, "name": "Bob", "dept": "Sales", "salary": 72000})
employees.add_row({"id": 103, "name": "Charlie", "dept": "Engineering", "salary": 110000})

# Save with Zstandard compression enabled
db.save(compress=True)