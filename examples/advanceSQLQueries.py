import netcell

db = netcell.open("company_records.ncell")

# Use standard SQL to calculate departmental stats
query = """
    SELECT dept, COUNT(*) as count, AVG(salary) as avg_pay 
    FROM employees 
    GROUP BY dept 
    ORDER BY avg_pay DESC
"""

stats = db.sql(query)
for row in stats:
    print(f"Dept: {row['dept']} | Staff: {row['count']} | Avg Pay: ${row['avg_pay']:.2f}")