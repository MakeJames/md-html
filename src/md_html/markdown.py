"""Markdown module."""

import re
import sys
from pathlib import Path
from typing import Generator, Self

from md_html.elements import Content, H, P
from md_html.exceptions import MDParseError


class Markdown:
    """Markdown class."""

    def __init__(self, content: str) -> None:
        """Instantiate the class.

        Attributes:
            content -- the content of a markdown file.

        """
        self.content = content

    def element(self, content: str) -> Content:
        """First guess element calculation."""
        first_char = content[0] if content != "" else ""
        match first_char:
            case "#":
                return Content(H, content)
            case _:
                return Content(P, content)

    @property
    def sections(self) -> Generator:
        """Splits the markdown content into parse-ready blocks.

        The best practice for paragraph spacing is to use a blank line
        to denote separate blocks of text.

        Yields strings of markdown content.

        """
        start = 0
        for index, char in enumerate(self.content):
            next_index = index + 1 if index + 1 < len(self.content) else index
            if char == "\n" and self.content[next_index] == "\n":
                yield self.element(self.content[start:index])
                start = index + 2
        if len(self.content[start:]) > 0:
            yield self.element(self.content[start:])

    @classmethod
    def from_stdin(cls, **kwargs) -> Self:
        """Generate a markdown instance from stdin."""
        if sys.stdin.isatty():
            raise MDParseError("No Markdown content supplied to the cli.")
        content = sys.stdin.read()
        if content == "":
            raise MDParseError("No Markdown content supplied to the cli.")
        return cls(content=content, **kwargs)

    @classmethod
    def from_file(cls, file: str, **kwargs) -> Self:
        """Generate a markdown instance from a file."""
        md_file = Path(file)
        content = ""

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        return cls(content, **kwargs)

    @classmethod
    def from_args(cls, file: str | None, **kwargs) -> Self:
        """Open and create an instance of the Markdown class.

        Options:
            file -- a pathlib ready file path string.

        """
        if file:
            return cls.from_file(file, **kwargs)
        return cls.from_stdin(**kwargs)
