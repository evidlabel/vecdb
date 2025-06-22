"""Utilities for generating embeddings."""

import sentence_transformers

model = sentence_transformers.SentenceTransformer('all-MiniLM-L6-v2')  # Load a pre-trained model

def generate_embedding(text: str):
    """Generate an embedding for the given text using the model."""
    return model.encode(text).tolist()  # Convert to list for compatibility
