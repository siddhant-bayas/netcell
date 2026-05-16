### Overview

NetCell is designed for scenarios where you need more structure than a JSON file but less overhead than a full SQL server. By storing data in **columns** rather than rows, it excels at analytical queries and high compression ratios.

### Key Features

* **Columnar Storage:** Efficient memory usage and faster queries on specific fields.
* **String Pooling:** Reduces file size by storing unique strings only once.
* **Automatic Indexing:** Built-in Hash and Range indexes for $O(1)$ and $O(\log n)$ lookups.
* **SQL Bridge:** Query your local NetCell files using standard SQLite syntax.
* **Zstandard Compression:** High-ratio compression for disk-space efficiency.
* **Excel Integration:** Direct conversion from `.xlsx` to `.ncell`.

### Installation

Choose the command for your operating system to download the core script:

**Windows (cmd):**

```bat
certutil -urlcache -split -f "https://raw.githubusercontent.com/sidddhant-bayas/netcell/main/netcell.py" "netcell.py"

```

**PowerShell:**

```powershell
Invoke-WebRequest 'https://raw.githubusercontent.com/sidddhant-bayas/netcell/main/netcell.py' -OutFile 'netcell.py'

```

**Linux/macOS:**

```bash
curl -o netcell.py https://raw.githubusercontent.com/sidddhant-bayas/netcell/main/netcell.py

```