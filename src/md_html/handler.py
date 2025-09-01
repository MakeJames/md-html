"""Handles requests to the interpreter."""

import argparse
import sys

from md_html.__version__ import version
from md_html.elements import HTML
from md_html.exceptions import MDParseError
from md_html.markdown import Markdown

parser = argparse.ArgumentParser(
    prog="md-html",
    description="Take the simplicity of Markdown to the structure of HTML.",
    usage="""Markdown to HTML Converter Command-Line Interface.

This module provides a command-line interface (CLI)
for converting Markdown (.md) files into styled HTML documents.

Usage:
    md-html input.md [options]
    cat input.md | md-html

Examples:
    md-html README.md
    md-html notes.md
    md-html post.md

Options:

This module is can be run as a command line tool, but you can also import
classes as a library component.

For more information please check out the README at
https://github.com/MakeJames/md-html/blob/main/README.md

Author: MakeJames <james@makejames.com>
License: MIT <https://github.com/MakeJames/md-html/blob/main/LICENCE

""",
)

parser.add_argument(
    "file",
    nargs="?",
    help="Path to the input Markdown file also accepts stdin.",
)

parser.add_argument(
    "--version",
    action="version",
    version=f"%(prog)s {version}",
    help="Print the Version number and exit.",
)

def usage() -> None:
    """Print usage documentation and exit."""
    parser.print_usage()
    sys.exit(2)


def main() -> None:
    """Process user commands."""
    args = parser.parse_args()

    try:
        markdown = Markdown.from_args(file=args.file)
    except MDParseError as e:
        print(f"Failed to Parse Markdown: {e.message}\n")
        usage()
        sys.exit(2)

    print(HTML(title="Markdown Document", sections=markdown.sections).html)
