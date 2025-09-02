"""The HTML module."""

from md_html.elements.base_element import Elements, HTMLBaseClass
from md_html.elements.body import Body
from md_html.elements.content import Content
from md_html.elements.head import Head


class HTML(HTMLBaseClass):
    """The HTML class that declares the page."""

    kind = Elements.html
    attr = ["lang='en_gb'", "dir='ltr'"]

    def __post_init__(
        self,
        title: str,
        sections: list[Content],
        attr: list[str] | None = None,
        **kwargs,
    ) -> None:
        """Create the HTML document.

        Arguments:
            title:
                The title of the document.
            sections:
                Content blocks.
            attr:
                Additional attributes that will be applied to the html element.
            **kwargs:
                Named attributes can be passed in at a parent level
                and reused in child elements.

        """
        self.head = Head(title=title, **kwargs)
        self.body = Body(sections=sections, **kwargs)
        self.content = "\n  ".join(["", self.head.html, self.body.html])
        self.content = self.content + "\n"
        if attr:
            self.attr.append(*attr)
