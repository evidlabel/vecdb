"""Utilities for file operations."""

import os
import glob


def get_tex_files(directory: str) -> list[str]:
    """Return a list of .tex files in the given directory."""
    return glob.glob(os.path.join(directory, "**", "label.tex"), recursive=True)


def snippetize_latex(file_path: str) -> list[str]:
    """Extract paragraphs from the body of a LaTeX file."""
    with open(file_path, "r") as f:
        content = f.read()
    start_tag = "\\begin{document}"
    end_tag = "\\end{document}"
    if start_tag in content and end_tag in content:
        start_idx = content.find(start_tag) + len(start_tag)
        end_idx = content.find(end_tag, start_idx)
        body = content[start_idx:end_idx].strip()
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        return paragraphs
    return []
