"""Parse Module."""

import re

from enum import StrEnum

from md_html.exceptions import HTMLParseError


class Elements(StrEnum):
    """HTML elements lookup."""

    body = "body"
    head = "head"
    heading = "h"
    html = "html"
    link = "a"
    paragraph = "p"


class HTMLBaseClass:
    """Base Class for HTML Element definitions.

    Attributes:
        attr
            A list of element attributes. These are rendered in the opening element tag.
        kind
            The class Element. References the Elements string Enum.
        html
            A class property returns the html fragment.
        tag
            The html tag that will be rendered in the html fragment.

    Raises:
        HTMLParseError
            If it is unable to process the html.

    """

    kind: Elements
    attr: list[str] = [""]
    _link_pattern = re.compile(r'(?<!\!)\[([^\]]*)\]\((\S+)(?:\s+"([^"]*)")?\)')

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
        self._replace_links()

    def _add_space_to_first_attr(self) -> None:
        if len(self.attr) == 0:
            return

        first_attr = self.attr[0]

        if first_attr == "":
            return

        self.attr[0] = " " + first_attr if first_attr[0] != " " else first_attr

    def _replace_links(self) -> None:
        def repl(match):
            link_text = match.group(1)
            href = match.group(2)
            return f"<a href=\"{href}\">{link_text}</a>"
        self.content = self._link_pattern.sub(repl, self.content)

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
        return f"<{self.tag}{' '.join(self.attr)}>{self.content}</{self.tag}>"

    @property
    def tag(self) -> str:
        """Returns the element tag.

        By default this returns the class.kind attribute.
        This method can be over-typed for custom logic,
        such as heading elements.
        """
        return self.kind
