"""Handles requests to the interpreter."""

import argparse

from md_html.__version__ import version
from md_html.markdown import Markdown


def main(args, input=None) -> None:
    """Process user commands."""
    if args.file and args.file != "-":
        markdown = Markdown.open(args.file)
    else:
        markdown = Markdown(input)
    print(list(markdown.sections))


parser = argparse.ArgumentParser(
    prog="md-html",
    description="Take the simplicity of Markdown to the structure of HTML.",
)

parser.add_argument("file", help="Path to the input Markdown file also accepts stdin.")

parser.add_argument(
    "--version",
    action="version",
    version=f"%(prog)s {version}",
    help="Print the Version number and exit.",
)
