"""Module for ChromaDB operations."""

import chromadb
from ..utils.embeddings import generate_embedding  # Import embedding utility
from chromadb.config import Settings


def get_client(persist_directory: str):
    """Get a ChromaDB client for the given directory."""
    return chromadb.PersistentClient(
        path=persist_directory, settings=Settings(anonymized_telemetry=False)
    )


def create_collection(client, collection_name: str = "default"):
    """Create a new collection in the client."""
    return client.create_collection(collection_name)


def add_document(client, collection_name: str, document: str, id: str = "id1"):
    """Add a single document to the collection with a generated embedding."""
    embedding = generate_embedding(document)
    collection = client.get_collection(collection_name)
    collection.add(documents=[document], embeddings=[embedding], ids=[id])


def bulk_add_documents(
    client, collection_name: str, documents: list[str], ids: list[str]
):
    """Add multiple documents to the collection in bulk with generated embeddings."""
    collection = client.get_collection(collection_name)
    batch_size = 5000  # Adjust based on ChromaDB limits
    for i in range(0, len(documents), batch_size):
        batch_docs = documents[i : i + batch_size]
        batch_ids = ids[i : i + batch_size]
        batch_embeddings = [generate_embedding(doc) for doc in batch_docs]
        collection.add(documents=batch_docs, embeddings=batch_embeddings, ids=batch_ids)


def query_collection(client, collection_name: str, query_text: str, n_results: int = 1):
    """Query the collection using a generated embedding for the query text."""
    embedding = generate_embedding(query_text)  # Use real embedding for query
    collection = client.get_collection(collection_name)
    return collection.query(query_embeddings=[embedding], n_results=n_results)
