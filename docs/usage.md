# Usage Guide for VecDB

This guide provides detailed instructions on how to use the VecDB CLI to manage your ChromaDB database. All commands are executed via the `vecdb` entry point after installation.

## Command Overview
VecDB offers three primary commands for interacting with your database: `init`, `add`, and `query`. Each command supports both long and short forms for options (e.g., `--directory` or `-d`).

### Initialize a Database (`init`)
The `init` command sets up a new ChromaDB database in the specified directory.

```bash
vecdb init --directory /path/to/db --collection mycollection
# or using short options
vecdb init -d /path/to/db -c mycollection
```

- `--directory` / `-d`: (Required) The directory where the ChromaDB database will be stored.
- `--collection` / `-c`: (Optional) The name of the collection to create (defaults to "default").

### Add Documents (`add`)
The `add` command scans a target directory for `.tex` files and adds their contents as snippets to the specified collection.
```bash
vecdb add --directory /path/to/db --collection mycollection --target-dir /path/to/tex/files
# or using short options
vecdb add -d /path/to/db -c mycollection -t /path/to/tex/files
```

- `--directory` / `-d`: (Required) The directory of the ChromaDB database.
- `--collection` / `-c`: (Optional) The name of the collection to add documents to (defaults to "default").
- `--target-dir` / `-t`: (Required) The directory to scan for `.tex` files.

### Query the Database (`query`)
The `query` command searches the specified collection for documents matching the query text, returning the top results in a formatted table.
```bash
vecdb query --directory /path/to/db --collection mycollection --query-text "search query" --top-n 5 --full
# or using short options
vecdb query -d /path/to/db -c mycollection -q "search query" -n 5 -f
```

- `--directory` / `-d`: (Required) The directory of the ChromaDB database.
- `--collection` / `-c`: (Optional) The name of the collection to query (defaults to "default").
- `--query-text` / `-q`: (Required) The text to search for in the collection.
- `--top-n` / `-n`: (Optional) The number of top results to return (defaults to 5).
- `--full` / `-f`: (Optional) Flag to return full document content instead of truncated snippets.

## Viewing Documentation Locally
VecDB includes MkDocs for generating documentation. After installation, you can serve the documentation locally with:
```bash
mkdocs serve
```
This will host the documentation at `http://127.0.0.1:8000/` by default, allowing you to browse through detailed guides and module references.
