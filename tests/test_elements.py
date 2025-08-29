"""Test the parser module."""

# ruff: noqa: S101

import pytest

from md_html.elements import HTMLBaseClass, P
from md_html.exceptions import HTMLParseError
from md_html.utils import Elements


class TestHTMLBaseClass:
    """Test the methods of the HTMLBaseClass."""

    @pytest.mark.parametrize(
        "text,expected",
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
    def test_html_escaping_is_correct(self, text, expected) -> None:
        """R-BICEP: Right."""
        test_instance = HTMLBaseClass(text)
        test_instance.kind = Elements.paragraph
        assert test_instance.escape == expected
        assert test_instance.text == test_instance.escape

    @pytest.mark.parametrize(
        "text,expected",
        [
            ("<&lt;", "&lt;&lt;"),
            (">&gt;", "&gt;&gt;"),
            ("&amp;", "&amp;"),
            ("&&amp;", "&amp;&amp;"),
        ],
    )
    def test_html_escaping_boundary_conditions(self, text, expected) -> None:
        """R-BICEP: Boundary."""
        test_instance = HTMLBaseClass(text)
        test_instance.kind = Elements.paragraph
        assert test_instance.escape == expected
        assert test_instance.text == test_instance.escape

    @pytest.mark.parametrize(
        "text",
        [
            (500),
            (True),
            (False),
            (5.8),
        ],
    )
    def test_html_escaping_error_conditions(self, text) -> None:
        """R-BICEP: Error."""
        with pytest.raises(HTMLParseError):
            HTMLBaseClass(text)

    @pytest.mark.parametrize(
        "kind,text,expected",
        [
            (Elements.paragraph, "Hello World!", "<p>Hello World!</p>"),
            (Elements.paragraph, "Hello <div>", "<p>Hello &lt;div&gt;</p>"),
            (Elements.paragraph, "<p>", "<p>&lt;p&gt;</p>"),
        ],
    )
    def test_html_render_is_correct(self, kind, text, expected) -> None:
        """R-BICEP: Right."""
        test_instance = HTMLBaseClass(text)
        test_instance.kind = kind
        assert test_instance.html == expected

    @pytest.mark.parametrize(
        "kind,text,expected",
        [
            (Elements.paragraph, "    ", "<p>    </p>"),
            (Elements.paragraph, "\n", "<p>\n</p>"),
        ],
    )
    def test_html_render_boundary_conditions(self, kind, text, expected) -> None:
        """R-BICEP: Boundary."""
        test_instance = HTMLBaseClass(text)
        test_instance.kind = kind
        assert test_instance.html == expected


class TestParagraphElements:
    """Test the methods of the Paragraph class."""

    @pytest.mark.parametrize(
        "text,expected",
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
    def test_html_render(self, text, expected) -> None:
        """R-BICEP: Right."""
        test = P(text)
        assert test.html == expected
