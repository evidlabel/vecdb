 # Chroma App Documentation
 
 ## Overview
 This project provides a command-line interface for interacting with ChromaDB, including initialization, querying, and adding documents. It uses NumPy for vectorization and is built with modularity in mind.
 
 ## Installation
 Prefer using `uv` for installation:
 ```
 uv pip install -e .
 ```
 
 ## Usage
 - Initialize: `chrdb init -d /path/to/db -c mycollection`
 - Query: `chrdb query -d /path/to/db -c mycollection -q "search text" -n 5`
 - Add documents: `chrdb add -d /path/to/db -c mycollection -t /path/to/tex/files`
 
 ## Modules
 - **cli.py**: Handles command-line interactions.
 - **core/db.py**: Manages ChromaDB operations with vectorized embeddings.
 - **utils/file_utils.py**: Provides utilities for file handling.
