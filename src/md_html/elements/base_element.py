"""Parse Module."""

from enum import StrEnum

from md_html.exceptions import HTMLParseError


class Elements(StrEnum):
    """HTML elements lookup."""

    paragraph = "p"
    head = "head"
    html = "html"
    body = "body"


class HTMLBaseClass:
    """Base Class for HTML Element definitions."""

    kind: Elements
    attr: list[str] = [""]

    def __init__(self, content: str = "", **kwargs) -> None:
        """Instantiate the class."""
        if isinstance(content, str) is False:
            raise HTMLParseError(
                f"Text is not of type str. Input is of type {content.__class__}."
            )
        self.content: str = content
        self.__post_init__(**kwargs)

    def __post_init__(self, **kwargs) -> None:
        """Post init method called after __init__ can be over-typed."""
        self.content = self.escape

    def __pre_render__(self) -> None:
        """Empty method that is called before html."""
        self._add_space_to_first_attr()

    def _add_space_to_first_attr(self) -> None:
        if len(self.attr) == 0:
            return

        first_attr = self.attr[0]

        if first_attr == "":
            return

        self.attr[0] = " " + first_attr if first_attr[0] != " " else first_attr

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
            self.content.replace("&amp;", "&")
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
        return f"<{self.kind}{' '.join(self.attr)}>{self.content}</{self.kind}>"
