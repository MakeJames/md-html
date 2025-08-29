"""Markdown module."""

from pathlib import Path
from typing import Generator, Self


class Markdown:
    """Markdown class."""

    def __init__(self, content: str) -> None:
        """Instantiate the class.

        Attributes:
            content -- the content of a markdown file.

        """
        self.content = content

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
                yield self.content[start:index]
                start = index + 2
        if len(self.content[start:]) > 0:
            yield self.content[start:]

    @classmethod
    def open(cls, file: str) -> Self:
        """Open and create an instance of the Markdown class.

        Options:
            file -- a pathlib ready file path string.

        """
        md_file = Path(file)
        content = ""

        with open(md_file, "r", encoding="utf-8") as f:
            content = f.read()

        return cls(content)
