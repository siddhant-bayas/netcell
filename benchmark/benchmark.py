import os
import time
import csv
import json
import sqlite3
import random
import string
import netcell as nc

NUM_ROWS = 500000

def generate_dummy_data(num_rows):
    print(f"Generating {num_rows:,} rows of test data...")
    data = []
    for i in range(num_rows):
        data.append({
            "id": i,
            "name": ''.join(random.choices(string.ascii_letters, k=8)),
            "age": random.randint(18, 80),
            "score": round(random.uniform(0, 100), 2),
            "department": random.choice(["Engineering", "Sales", "Marketing", "HR", "IT"])
        })
    return data

def format_size(size_bytes):
    return f"{size_bytes / (1024 * 1024):.2f} MB"

def run_benchmark():
    data = generate_dummy_data(NUM_ROWS)
    results = {}

    # ---------------------------------------------------------
    # 1. NetCell Benchmark
    # ---------------------------------------------------------
    print("\nRunning NetCell benchmark...")
    start = time.time()
    db = nc.create("bench.ncell")
    sheet = db.create_sheet("data")
    print("Saving to:", db.path.resolve())
    for row in data:
        sheet.add_row(row)
    db.save(compress=True)
    nc_write_time = time.time() - start
    nc_size = os.path.getsize("bench.ncell")

    start = time.time()
    db = nc.open("bench.ncell")
    nc_read_time = time.time() - start

    # Test NetCell SQL Query Engine (consistent across all)
    start = time.time()
    db.sql("SELECT * FROM data WHERE age > 30")
    nc_query_time = time.time() - start

    results['NetCell'] = {
        'Size': nc_size, 'Write (s)': nc_write_time, 
        'Read (s)': nc_read_time, 'Query (s)': nc_query_time
    }

    # ---------------------------------------------------------
    # 2. CSV Benchmark
    # ---------------------------------------------------------
    print("Running CSV benchmark...")
    start = time.time()
    with open("bench.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    csv_write_time = time.time() - start
    csv_size = os.path.getsize("bench.csv")

    start = time.time()
    csv_data = []
    with open("bench.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['age'] = int(row['age'])
            row['score'] = float(row['score'])
            csv_data.append(row)
    csv_read_time = time.time() - start

    start = time.time()
    _ = [r for r in csv_data if r['age'] > 30]
    csv_query_time = time.time() - start

    results['CSV'] = {
        'Size': csv_size, 'Write (s)': csv_write_time, 
        'Read (s)': csv_read_time, 'Query (s)': csv_query_time
    }

    # ---------------------------------------------------------
    # 3. JSON Benchmark
    # ---------------------------------------------------------
    print("Running JSON benchmark...")
    start = time.time()
    with open("bench.json", "w") as f:
        json.dump(data, f)
    json_write_time = time.time() - start
    json_size = os.path.getsize("bench.json")

    start = time.time()
    with open("bench.json", "r") as f:
        json_data = json.load(f)
    json_read_time = time.time() - start

    start = time.time()
    _ = [r for r in json_data if r['age'] > 30]
    json_query_time = time.time() - start

    results['JSON'] = {
        'Size': json_size, 'Write (s)': json_write_time, 
        'Read (s)': json_read_time, 'Query (s)': json_query_time
    }

    # ---------------------------------------------------------
    # 4. SQLite (Disk) Benchmark
    # ---------------------------------------------------------
    print("Running SQLite (Disk) benchmark...")
    if os.path.exists("bench.db"):
        os.remove("bench.db")
    start = time.time()
    conn = sqlite3.connect("bench.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE data (id INTEGER, name TEXT, age INTEGER, score REAL, department TEXT)")
    cursor.executemany("INSERT INTO data VALUES (:id, :name, :age, :score, :department)", data)
    conn.commit()
    sqlite_write_time = time.time() - start
    sqlite_size = os.path.getsize("bench.db")
    conn.close()

    start = time.time()
    conn = sqlite3.connect("bench.db")
    cursor = conn.cursor()
    # Read time in SQLite is just connection, so we do a full fetch to be fair to memory models
    cursor.execute("SELECT * FROM data")
    _ = cursor.fetchall()
    sqlite_read_time = time.time() - start

    start = time.time()
    cursor.execute("SELECT * FROM data WHERE age > 30")
    _ = cursor.fetchall()
    sqlite_query_time = time.time() - start
    conn.close()

    results['SQLite (Disk)'] = {
        'Size': sqlite_size, 'Write (s)': sqlite_write_time, 
        'Read (s)': sqlite_read_time, 'Query (s)': sqlite_query_time
    }

    # ---------------------------------------------------------
    # Print Results
    # ---------------------------------------------------------
    print("\n" + "="*70)
    print(f" BENCHMARK RESULTS ({NUM_ROWS:,} Rows) ")
    print("="*70)
    print(f"{'Format':<15} | {'File Size':<10} | {'Write':<10} | {'Read/Load':<10} | {'Query Time':<10}")
    print("-" * 70)
    
    for fmt, stats in results.items():
        print(f"{fmt:<15} | {format_size(stats['Size']):<10} | {stats['Write (s)']:<8.3f} s | {stats['Read (s)']:<8.3f} s | {stats['Query (s)']:<8.4f} s")
    
    print("="*70)

    # Cleanup
    for f in ["bench.ncell","bench.csv", "bench.json", "bench.db"]:
        if os.path.exists(f):
            os.remove(f)

if __name__ == "__main__":
    run_benchmark()