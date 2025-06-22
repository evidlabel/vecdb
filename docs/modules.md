 
# Modules Overview

VecDB is organized into modular components, each with a specific responsibility. This structure enhances maintainability and allows for easy extension. Below is an overview of the key modules in the `src/vecdb` directory.

## `cli.py`

**Purpose**: Provides the command-line interface (CLI) for interacting with VecDB.

- Defines the main entry point for the application using the `click` library.
- Implements commands like `init`, `add`, and `query` with support for short and long option formats (e.g., `-d` and `--directory`).
- Uses `rich` for formatted console output, including tables for query results.

## `core/db.py`

**Purpose**: Manages core ChromaDB operations.

- Handles client initialization, collection creation, and document management.
- Supports bulk document addition with vectorized embeddings for efficiency.
- Provides querying functionality using embeddings for semantic search.
- Utilizes NumPy indirectly through the embedding generation process for vector operations.

## `utils/embeddings.py`

**Purpose**: Generates vector embeddings for documents and queries.

- Uses the `sentence-transformers` library with a pre-trained model (`all-MiniLM-L6-v2`) for creating meaningful embeddings.
- Converts text input into vector representations suitable for ChromaDB storage and querying.

## `utils/file_utils.py`

**Purpose**: Handles file operations and content extraction.

- Scans directories for `.tex` files using glob patterns.
- Extracts snippets from LaTeX files by parsing document body content between `\begin{document}` and `\end{document}`.
- Splits content into manageable paragraphs or snippets for storage in ChromaDB.

## Design Philosophy
VecDB follows a modular design where each file has a single responsibility. This approach ensures that changes to one part of the system (e.g., embedding generation) do not inadvertently affect unrelated components (e.g., CLI output formatting). The use of modern tools like `uv` for dependency management and `mkdocs-material` for documentation further enhances the developer experience.
