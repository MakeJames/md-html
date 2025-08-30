"""Parse Module."""

from md_html.exceptions import HTMLParseError
from md_html.utils import Elements


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


class P(HTMLBaseClass):
    """Paragraph Element.

    Takes markdown text and formats it as a paragraph.
    """

    kind = Elements.paragraph


class HTML(HTMLBaseClass):
    """The HTML class that declares the page."""

    kind = Elements.html
    attr = ["lang='en_gb'", "dir=ltr"]

    def __post_init__(
        self, title: str, sections: list[str], attr: list[str] | None = None, **kwargs
    ) -> None:
        """Create the HTML document.

        The HMTL class is a special html element class.
        This class wraps the markdown content and creates the html document.

        This post-init method.

        """
        self.content = "\n"
        self.head = Head(title=title)
        self.body = Body(sections=sections)
        self.content = "\n".join([self.head.html, self.body.html])
        self.content = self.content + "\n"
        if attr:
            self.attr.append(*attr)


class Head(HTMLBaseClass):
    """The Head element that declares the document meta-data."""

    kind = Elements.head

    def __post_init__(self, title: str, **kwargs) -> None:
        """Create the <head></head> content."""
        self.title = title
        self.content = (
            "\n"
            + "\n".join(
                [
                    self._charset,
                    self._viewport,
                    self._title,
                    self._description,
                    self._author,
                    self._style,
                ]
            )
            + "\n"
        )

    @property
    def _charset(self) -> str:
        return '<meta charset="utf-8">'

    @property
    def _viewport(self) -> str:
        return '<meta name="viewport" content="width=device-width, initial-scale=1">'

    @property
    def _description(self) -> str:
        return '<meta name="description" content="Generated from Markdown">'

    @property
    def _author(self) -> str:
        return '<meta name="author" content="md-html">'

    @property
    def _title(self) -> str:
        return f"<title>{self.title}</title>"

    @property
    def _style(self) -> str:
        return (
            """<style>
    body {
      max-width: 120ch;
      margin: 2rem auto;
      padding: 0 1rem;
      font-family: system-ui, sans-serif;
      line-height: 1.6;
      color: #222;
      background: #fff;
    }
    h1, h2, h3, h4, h5, h6 {
      line-height: 1.2;
      margin-top: 1.5em;
    }
    pre, code {
      font-family: monospace;
      background: #f5f5f5;
      padding: 0.2em 0.4em;
      border-radius: 3px;
    }
    pre {
      padding: 1em;
      overflow-x: auto;
    }
    blockquote {
      margin: 1em 0;
      padding-left: 1em;
      border-left: 0.25em solid #ccc;
      color: #555;
    }
    a {
      color: #0645ad;
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
  </style>
""".replace("  ", "")
            .replace("\n", " ")
            .rstrip()
        )


class Body(HTMLBaseClass):
    """Body of the HTML document."""

    kind = Elements.body

    def __post_init__(self, sections: list[str], **kwargs) -> None:
        """Instantiate the Body class."""
        self.content = "\n"
        for section in sections:
            self.content = "\n".join([self.content, P(content=section).html])
        self.content = self.content + "\n"
