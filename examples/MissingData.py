import netcell

db = netcell.create("sensor_data.ncell")
logs = db.create_sheet("readings")

# Some readings might have missing (None) values
logs.add_row({"timestamp": "2023-01-01 10:00", "temp": 22.5, "humidity": 45})
logs.add_row({"timestamp": "2023-01-01 10:05", "temp": None, "humidity": 46}) 
logs.add_row({"timestamp": "2023-01-01 10:10", "temp": 23.1, "humidity": None})

db.save()

# SQL queries will correctly treat None as NULL
null_check = db.sql("SELECT * FROM readings WHERE temp IS NULL")
print(f"Missing temperatures found: {len(null_check)}")