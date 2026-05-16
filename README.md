### Overview

NetCell is designed for scenarios where you need more structure than a JSON file but less overhead than a full SQL server. By storing data in **columns** rather than rows, it excels at analytical queries and high compression ratios.

### Documentation

* **[Quickstart Guide](./docs/quickstart.md)**: Get up and running in under 60 seconds.
* **[API Reference](./docs/api.md)**: Detailed documentation of classes, methods, and functions.
* **[Architecture](/docs/architecture.md)**: Understanding the `.ncell` file format and columnar engine.

---
### Key Features

* **Columnar Storage:** Efficient memory usage and faster queries on specific fields.
* **String Pooling:** Reduces file size by storing unique strings only once.
* **Automatic Indexing:** Built-in Hash and Range indexes for $O(1)$ and $O(\log n)$ lookups.
* **SQL Bridge:** Query your local NetCell files using standard SQLite syntax.
* **Zstandard Compression:** High-ratio compression for disk-space efficiency.
* **Excel Integration:** Direct conversion from `.xlsx` to `.ncell`.
To update your documentation with instructions for using the `setup.bat` file to install NetCell globally along with its dependencies, you can use the following section. This emphasizes the convenience of the "one-click" setup you've created.

---

###  Easy Installation (Windows)

If you have downloaded the **`setup.bat`** file, follow these steps to install NetCell and all its features  globally on your system:

1. **Run as Administrator**: Right-click `setup.bat` and select **"Run as Administrator"**. This ensures the script has permission to move NetCell into your Python library folder.

2. **Automatic Setup**: The script will automatically:
* Locate your Python `site-packages` directory.
* Download the latest `netcell.py` directly into your global library.
* Install `zstandard` for high-ratio data compression.
* Install `openpyxl` to enable `.xlsx` to `.ncell` conversion.

####  Verification

Once the setup is complete, you can verify the installation from any directory by running:

```python
import netcell
print("NetCell version:", netcell.NCELL_VERSION)

```

This works everywhere on your PC because the setup script places NetCell in your global environment.

---

### Manual Installation

If you prefer to handle the installation manually or are on a non-Windows system, use the commands below:

**Windows (cmd):**

```bat
certutil -urlcache -split -f "https://raw.githubusercontent.com/siddhant-bayas/netcell/refs/heads/main/netcell.py" "netcell.py"

```

**PowerShell:**

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/siddhant-bayas/netcell/refs/heads/main/netcell.py' -OutFile 'netcell.py'

```

**Linux/macOS:**

```bash
curl -o netcell.py https://raw.githubusercontent.com/siddhant-bayas/netcell/refs/heads/main/netcell.py
```