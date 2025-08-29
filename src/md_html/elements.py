"""Parse Module."""

from md_html.exceptions import HTMLParseError
from md_html.utils import Elements


class HTMLBaseClass:
    """Base Class for HTML Element definitions."""

    kind: Elements

    def __init__(self, text: str) -> None:
        """Instantiate the class."""
        if isinstance(text, str) is False:
            raise HTMLParseError(
                f"Text is not of type str. Input is of type {text.__class__}."
            )
        self.text: str = text
        self.__post_init__()

    def __post_init__(self) -> None:
        """Post init method called after __init__ can be over-typed."""
        self.text = self.escape

    def __pre_render__(self) -> None:
        """Empty method that is called before html."""
        ...

    @property
    def escape(self) -> str:
        """Escape html characters in the input string.

        This avoids issues where strings of text contain html elements.
        Specifically, this replaces:
            - `<` with `&lt;`
            - `>` with `&gt;`
            - `&` with `&amp;`
        """
        return (
            self.text.replace("&amp;", "&")
            .replace("&lt;", "<")
            .replace("&gt;", ">")
            .replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )

    @property
    def html(self) -> str:
        """Returns the html of the element."""
        self.__pre_render__()
        return f"<{self.kind}>{self.text}</{self.kind}>"


class P(HTMLBaseClass):
    """Paragraph Element.

    Takes markdown text and formats it as a paragraph.
    """

    kind = Elements.paragraph
