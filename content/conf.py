"""Sphinx configuration for the SLURM training lesson."""

from __future__ import annotations

project = "HPC SLURM Job Workflows Minicourse"
author = "Polar Meteorology"
copyright = "2026, Polar Meteorology"
version = "0.1.0"
release = version

extensions = [
    "myst_parser",
    "sphinx_copybutton",
]

source_suffix = {
    ".md": "markdown",
}
master_doc = "index"

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "linkify",
    "substitution",
    "tasklist",
]

html_theme = "alabaster"
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

copybutton_prompt_text = r"\$ "
copybutton_prompt_is_regexp = True
