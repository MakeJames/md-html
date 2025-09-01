"""Test the parser module."""

# ruff: noqa: S101 S301

import json

import pytest

from md_html.elements import HTML, HTMLBaseClass, P
from md_html.exceptions import HTMLParseError
from md_html.utils import Elements


class TestHTMLBaseClass:
    """Test the methods of the HTMLBaseClass."""

    @pytest.mark.parametrize(
        "content,expected",
        [
            (
                "Text <div>that contains a div</div>",
                "Text &lt;div&gt;that contains a div&lt;/div&gt;",
            ),
            (
                "Text <div>that also contains an &</div>",
                "Text &lt;div&gt;that also contains an &amp;&lt;/div&gt;",
            ),
            (
                "&&&&&",
                "&amp;&amp;&amp;&amp;&amp;",
            ),
            (
                "<<<<",
                "&lt;&lt;&lt;&lt;",
            ),
            (">>>>", "&gt;&gt;&gt;&gt;"),
        ],
    )
    def test_html_escaping_is_correct(self, content, expected) -> None:
        """R-BICEP: Right."""
        test_instance = HTMLBaseClass(content)
        test_instance.kind = Elements.paragraph
        assert test_instance.escape == expected
        assert test_instance.content == test_instance.escape

    @pytest.mark.parametrize(
        "content,expected",
        [
            ("<&lt;", "&lt;&lt;"),
            (">&gt;", "&gt;&gt;"),
            ("&amp;", "&amp;"),
            ("&&amp;", "&amp;&amp;"),
        ],
    )
    def test_html_escaping_boundary_conditions(self, content, expected) -> None:
        """R-BICEP: Boundary."""
        test_instance = HTMLBaseClass(content)
        test_instance.kind = Elements.paragraph
        assert test_instance.escape == expected
        assert test_instance.content == test_instance.escape

    @pytest.mark.parametrize(
        "content",
        [
            (500),
            (True),
            (False),
            (5.8),
        ],
    )
    def test_html_escaping_error_conditions(self, content) -> None:
        """R-BICEP: Error."""
        with pytest.raises(HTMLParseError):
            HTMLBaseClass(content)

    @pytest.mark.parametrize(
        "kind,content,expected",
        [
            (Elements.paragraph, "Hello World!", "<p>Hello World!</p>"),
            (Elements.paragraph, "Hello <div>", "<p>Hello &lt;div&gt;</p>"),
            (Elements.paragraph, "<p>", "<p>&lt;p&gt;</p>"),
        ],
    )
    def test_html_render_is_correct(self, kind, content, expected) -> None:
        """R-BICEP: Right."""
        test_instance = HTMLBaseClass(content)
        test_instance.kind = kind
        assert test_instance.html == expected

    @pytest.mark.parametrize(
        "kind,content,expected",
        [
            (Elements.paragraph, "    ", "<p>    </p>"),
            (Elements.paragraph, "\n", "<p>\n</p>"),
            (Elements.head, "", "<head></head>"),
        ],
    )
    def test_html_render_boundary_conditions(self, kind, content, expected) -> None:
        """R-BICEP: Boundary."""
        test_instance = HTMLBaseClass(content)
        test_instance.kind = kind
        assert test_instance.html == expected

    @pytest.mark.parametrize(
        "kind,attr,content,expected",
        [
            (
                Elements.html,
                ["lang='en_gb'", "dir='ltr'"],
                "",
                "<html lang='en_gb' dir='ltr'></html>",
            ),
            (Elements.paragraph, [""], "\n", "<p>\n</p>"),
            (Elements.paragraph, [], "\n", "<p>\n</p>"),
        ],
    )
    def test_html_render_attributes(self, kind, attr, content, expected) -> None:
        """R-BICEP: Boundary."""
        test_instance = HTMLBaseClass(content)
        test_instance.kind = kind
        test_instance.attr = attr
        assert test_instance.html == expected


class TestParagraphElements:
    """Test the methods of the Paragraph class."""

    @pytest.mark.parametrize(
        "content,expected",
        [
            ("Hello World!", "<p>Hello World!</p>"),
            ("Hello <div>", "<p>Hello &lt;div&gt;</p>"),
            ("<p>", "<p>&lt;p&gt;</p>"),
            ("**strong text**", "<p>**strong text**</p>"),
            ("*emphasis text*", "<p>*emphasis text*</p>"),
            (
                "**strong text with *emphasis***",
                "<p>**strong text with *emphasis***</p>",
            ),
            (
                "***strong text with emphasis***",
                "<p>***strong text with emphasis***</p>",
            ),
        ],
    )
    def test_html_render(self, content, expected) -> None:
        """R-BICEP: Right."""
        test = P(content)
        assert test.html == expected


class TestHTMLElements:
    """Test the methods of the HTML class."""

    @pytest.mark.parametrize(
        "title,file,attr",
        [
            ("Markdown Document", "table", []),
            ("Markdown Document", "inline-img", []),
            ("Markdown Document", "quantum-slopes", []),
            ("Markdown Document", "blockquote", []),
            ("Markdown Document", "perfectly-ripe-tomatoes", []),
            ("Markdown Document", "a-grand-day-out", []),
            ("Markdown Document", "a-tower-of-blocks", []),
        ],
    )
    def test_html_render_of_html_elements(
        self, title, file, attr, snapshot
    ) -> None:
        """R-BICEP: Right."""
        snapshot.snapshot_dir = "tests/snapshots/html"
        with open(f"./tests/data/sections/{file}.json", "rb") as _file:
            sections = json.load(_file)
        test = HTML(title=title, sections=sections, atr=attr)
        snapshot.assert_match(test.html, f"{file}.html")

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
