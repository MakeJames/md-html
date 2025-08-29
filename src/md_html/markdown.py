"""Markdown module."""

from typing import Generator


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
