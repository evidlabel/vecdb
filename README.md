 # Chroma App
 
 A basic application to set up and query a local ChromaDB.
 
 ## Installation
 Use UV to install dependencies:
 ```sh
 uv pip install -r requirements.txt  # Or directly from pyproject.toml
 ```
 
 ## Usage
 Run the CLI:
 ```sh
 python -m chroma_app.cli init -d /path/to/db
 python -m chroma_app.cli query -d /path/to/db -q "sample query"
 ```
 
 ## Documentation
 For full docs, use MkDocs: `mkdocs serve` after installing MkDocs via UV.
