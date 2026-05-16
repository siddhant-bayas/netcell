# NetCell architecture

NetCell operates on a hierarchical columnar model designed for speed and portability.

### Data Layout

1. **Database:** The top-level container (maps to a single `.ncell` file).
2. **Sheet:** Equivalent to a Table. Contains multiple columns.
3. **ColumnVector:** A typed array of values (Integer, Float, String, or Object).
4. **String Pool:** A global dictionary per sheet that maps integers to strings, drastically reducing the footprint of repetitive text data.

### The .ncell File Format

Every NetCell file begins with a **fixed 24-byte binary header**:

| Offset | Size | Type | Description |
| --- | --- | --- | --- |
| 0 | 4 | Magic | The bytes `NCLL` |
| 4 | 4 | Version | Format version (Current: 2) |
| 8 | 4 | Count | Number of sheets in the file |
| 12 | 1 | Flags | Bit 0: Compression (1=Zstd, 0=None) |
| 13 | 3 | Padding | Reserved for future alignment |
| 16 | 8 | Reserved | Future use (64-bit) |

**Payload:** Following the header is the JSON-serialized data, optionally compressed using `zstandard`.

### Indexing Logic

* **HashIndex:** Created for all columns. Uses a dictionary mapping values to row IDs for instant `==` matches.
* **RangeIndex:** Maintains a sorted list of values for optimized `>` and `<` comparisons using binary search (`bisect`).
