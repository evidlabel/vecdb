 # vecdb app
 
 A cli app to set up and query a local chromadb database.
 
 ## Installation
 Use UV to install dependencies:
 ```sh
 uv pip install . 
 ```
 
 ## Usage
 Run the CLI:
 ```sh
 vecdb init -d /path/to/db
 vecdb add -d /path/to/db -t /path/to/db
 vecdb query -d /path/to/db -q "sample query"
 ```
 
 ## Documentation
 For full docs, use MkDocs: `mkdocs serve` after installing MkDocs via UV.
