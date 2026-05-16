from netcell import open as open_nc

# Open an existing database
db = open_nc("company_records.ncell")
employees = db.sheet("employees")

# Chain filters: Find high-earning Engineers
results = (employees.where("salary", ">", 90000)
                    .where("dept", "==", "Engineering")
                    .select("name", "salary")
                    .limit(5)
                    .execute())

for row in results.rows:
    print(f"High Earner: {row['name']} (${row['salary']})")