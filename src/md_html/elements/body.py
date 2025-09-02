"""The Body of the HTML document."""

from md_html.elements.base_element import Elements, HTMLBaseClass
from md_html.elements.content import Content


class Body(HTMLBaseClass):
    """Body of the HTML document."""

    kind = Elements.body

    def __post_init__(self, sections: list[Content], *args, **kwargs) -> None:
        """Instantiate the Body class."""
        for section in sections:
            self.content = "\n    ".join(
                [self.content, section.build(*args, **kwargs).html]
            )
        self.content = self.content + "\n  "
