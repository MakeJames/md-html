"""Heading html element."""

from md_html.elements.base_element import Elements, HTMLBaseClass


class H(HTMLBaseClass):
    """The heading element."""

    kind = Elements.heading

    def __post_init__(self, **kwargs) -> None:
        """Set additional parameters for Heading elements."""
        self.prefix = self.content.split(" ", 1)[0]
        self.level = self._calculate_level()

    def _is_valid_heading(self) -> bool:
        h1 = 1
        h6 = 6
        return h1 <= len(self.prefix) <= h6 and all(ch == "#" for ch in self.prefix)

    def _calculate_level(self) -> int | None:
        if self._is_valid_heading() is False:
            self.kind = Elements.paragraph
            return None
        return len(self.prefix)

    @property
    def tag(self) -> str:
        """The heading tag as h1 -> h6."""
        if self.level:
            return f"{self.kind}{self.level}"
        return self.kind

