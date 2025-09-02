"""The Body of the HTML document."""

from md_html.elements.base_element import Elements, HTMLBaseClass
from md_html.elements.paragraph import P


class Body(HTMLBaseClass):
    """Body of the HTML document."""

    kind = Elements.body

    def __post_init__(self, sections: list[str], **kwargs) -> None:
        """Instantiate the Body class."""
        for section in sections:
            self.content = "\n    ".join(
                [self.content, P(content=section, **kwargs).html]
            )
        self.content = self.content + "\n  "
