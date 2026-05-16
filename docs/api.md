##  API Reference

### Core Functions

* `create(path: str) -> NetCell`: Initializes a new database instance at the specified path.
* `open(path: str) -> NetCell`: Loads an existing `.ncell` file into memory.
* `convert_excel_to_netcell(excel_path, output_path)`: Utility to migrate `.xlsx` data to NetCell.

### Class: `NetCell`

The primary interface for database management.

* `create_sheet(name: str) -> Sheet`: Adds a new table.
* `sheet(name: str) -> Sheet`: Retrieves a sheet by name.
* `sql(query: str) -> List[Dict]`: Executes a SQL query by temporarily bridging data to an in-memory SQLite instance.
* `save(compress: bool)`: Serializes and writes the DB to the file system.

### Class: `Sheet`

Where the data lives.

* `add_row(row: Dict[str, Any])`: Appends a row. Note: Columns are dynamically inferred from the dictionary keys.
* `where(column, operator, value)`: Returns a `QueryBuilder` for filtering.

### Class: `QueryBuilder`

Provides a chainable interface for data retrieval.

* `.select(*columns)`: Defines which fields to return.
* `.limit(n)` / `.offset(n)`: Standard pagination tools.
* `.execute() -> QueryResult`: Processes the filters and returns the data.

---

**Note:** The `zstandard` and `openpyxl` modules are optional. If they are not installed, NetCell will function without compression and Excel conversion capabilities, respectively.

### One final tip:

> When using `db.sql()`, NetCell handles the heavy lifting of converting columnar data into a relational format for SQLite. This is powerful but can be memory-intensive for extremely large datasets. For simple filters, the `.where()` method is significantly faster!