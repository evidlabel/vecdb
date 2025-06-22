"""Command-line interface for chroma_app."""

import click
from .core.db import get_client, query_collection, create_collection, bulk_add_documents
from .utils.file_utils import get_tex_files, snippetize_latex
import logging
from rich.logging import RichHandler
from rich.console import Console
from rich.table import Table
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """ChromaDB application CLI."""
    pass


@cli.command()
@click.option("--directory", "-d", required=True, help="Directory for ChromaDB")
@click.option("--collection", "-c", default="default", help="Collection name")
def init(directory, collection):
    """Initialize ChromaDB in the specified directory."""
    client = get_client(directory)
    create_collection(client, collection)
    click.echo(f"Collection '{collection}' created in {directory}")


@cli.command()
@click.option("--directory", "-d", required=True, help="Directory for ChromaDB")
@click.option("--collection", "-c", default="default", help="Collection name")
@click.option("--query-text", "-q", required=True, help="Query text")
@click.option("--top-n", "-n", default=5, help="Number of top results to return")
@click.option("--full", "-f", is_flag=True, help="Return full documents; otherwise, return key passages")
def query(directory, collection, query_text, top_n, full):
    """Run a query against the collection and display results in rich format."""
    client = get_client(directory)
    results = query_collection(client, collection, query_text, n_results=top_n)
    console = Console()
    if results and "ids" in results and "documents" in results and "distances" in results:
        ids = results["ids"][0]  # Extract top IDs
        documents = results["documents"][0]  # Extract top documents
        distances = results["distances"][0]
        table = Table(title="Top Query Results")
        table.add_column("Rank", style="cyan")
        table.add_column("ID", style="blue")
        table.add_column("Distance", style="magenta")
        table.add_column("Content", style="green")
        for i, (doc_id, doc, dist) in enumerate(zip(ids, documents, distances), 1):
            content = doc if full else (doc[:100] + "...")
            table.add_row(str(i), doc_id, f"{dist:.4f}", content)
        console.print(table)
    else:
        console.print("[yellow]No results found.[/yellow]")


@cli.command()
@click.option("--directory", "-d", required=True, help="Directory for ChromaDB")
@click.option("--collection", "-c", default="default", help="Collection name")
@click.option("--target-dir", "-t", required=True, help="Target directory to scan for .tex files")
def add(directory, collection, target_dir):
    """Add .tex files from the target directory to the collection in bulk as snippets."""
    client = get_client(directory)
    tex_files = get_tex_files(target_dir)
    logger.info(f"Found {len(tex_files)} .tex files in {target_dir}")
    documents = []
    ids = []
    for file_path in tex_files:
        snippets = snippetize_latex(file_path)
        for idx, snippet in enumerate(snippets, 1):
            documents.append(snippet)
            base_uuid = file_path.split(os.sep)[-2][:8]
            # note the uuid is in the dir name, not file
            snippet_id = f"{base_uuid}_{idx}"
            ids.append(snippet_id)
            logger.info(f"Adding snippet from {file_path} with ID: {snippet_id}")
    if documents:
        bulk_add_documents(client, collection, documents, ids)
    click.echo(f"Added {len(documents)} snippets to collection '{collection}'")
