"""Markdown to HTML Converter Command-Line Interface.

This module provides a command-line interface (CLI)
for converting Markdown (.md) files into styled HTML documents.

Usage:
    python -m md-html input.md [options]

Examples:
    python -m md-html README.md
    python -m md-html notes.md
    python -m md-html post.md

Options:

This module is intended to be run as a script via `python -m`, but may also be
imported and reused as a library component.

Author: MakeJames <james@makejames.com
License: MIT

"""

from md_html.handler import main

main()
