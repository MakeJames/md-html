"""The Head element."""

from md_html.elements.base_element import Elements, HTMLBaseClass


class Head(HTMLBaseClass):
    """The Head element that declares the document meta-data."""

    kind = Elements.head

    def __post_init__(self, title: str, **kwargs) -> None:
        """Create the <head></head> content."""
        self.title = title
        self.content = "\n    ".join(
            [
                self.content,
                self._charset,
                self._viewport,
                self._title,
                self._description,
                self._author,
                self._style,
            ]
        )
        self.content = self.content + "\n  "

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
