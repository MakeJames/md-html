"""Paragraph elements."""

from md_html.elements.base_element import Elements, HTMLBaseClass


class P(HTMLBaseClass):
    """Paragraph Element.

    Takes markdown text and formats it as a paragraph.
    """

    kind = Elements.paragraph
