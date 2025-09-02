"""Test the methods of the HTML package."""

# ruff: noqa: S101

import pytest

from md_html.elements import Content, H, P
from md_html.elements.html import HTML


class TestHTMLElements:
    """Test the methods of the HTML class."""

    @pytest.mark.parametrize(
        "title,sections,expects",
        [
            (
                "Markdown Document",
                [
                    Content(H, "# Hello World"),
                    Content(
                        P, "A paragraph with **bold**, *italic*, and `inline code`.\n"
                    ),
                    Content(
                        P,
                        "1. Ordered item\n2. Another item\n3. Final item with a [link](https://example.com/test)\n",
                    ),
                ],
                [
                    "<h1># Hello World</h1>",
                    "<p>A paragraph with **bold**, *italic*, and `inline code`.\n</p>",
                    "<p>1. Ordered item",
                    "<a href=\"https://example.com/test\">link</a>",
                ],
            ),
            (
                "Markdown Document",
                [
                    Content(P, """```json\n{"key": "value"}\n```\n"""),
                    Content(H, "## A section heading"),
                    Content(
                        P,
                        """- [ ] A checked list\n- [x] With some checked items
- [ ] And other items
    - with nested
    - items""",
                    ),
                ],
                [
                    "<p>```json\n{\"key\": \"value\"}\n```\n",
                    "<h2>## A section heading</h2>",
                    "<p>- [ ] A checked list",
                    "    - with nested",
                ],
            ),
        ],
    )
    def test_html_render_of_html_elements(self, title, sections, expects) -> None:
        """R-BICEP: Right."""
        test = HTML(title=title, sections=sections, atr=[])
        print(test.html)
        for expect in expects:
            assert expect in test.html

    @pytest.mark.parametrize(
        "title,sections,attr,expected",
        [
            (
                "Markdown Document",
                [],
                ["class='light'"],
                "<html lang='en_gb' dir='ltr' class='light'>",
            ),
        ],
    )
    def test_html_can_parse_custom_attr(self, title, sections, attr, expected) -> None:
        """R-BICEP: Right."""
        test = HTML(title=title, sections=sections, attr=attr)
        assert test.html.split("\n")[0] == expected
