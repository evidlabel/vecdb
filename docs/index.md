# VecDB Documentation

Welcome to the official documentation for **VecDB**, a command-line interface (CLI) application for managing and querying a local ChromaDB database. This tool is designed for efficient vectorized search and storage of documents using modern Python libraries like NumPy and Sentence Transformers.

## Overview

VecDB allows users to initialize a ChromaDB database, add documents in bulk (especially LaTeX files), and query the database for relevant content. It is built with modularity and ease of use in mind, leveraging the power of vector embeddings for semantic search.

## Installation

We recommend using `uv` for dependency management and installation. To install VecDB, run:
```bash
uv pip install .
```
Alternatively, you can use pip if uv is not available:
```bash
pip install .
```

## Quick Start
To get started with VecDB, follow these steps:

1. Initialize a database:
   ```bash
   vecdb init --directory /path/to/db --collection mycollection
   ```
2. Add documents (e.g., LaTeX files) to the collection:
   ```bash
   vecdb add --directory /path/to/db --collection mycollection --target-dir /path/to/tex/files
   ```
3. Query the collection:
   ```bash
   vecdb query --directory /path/to/db --collection mycollection --query-text "search query" --top-n 5
   ```

Navigate through the documentation for detailed usage instructions and module descriptions.
