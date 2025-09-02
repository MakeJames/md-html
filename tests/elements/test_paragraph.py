"""Test the methods and classes of the Paragraph package."""

# ruff: noqa: S101

import pytest

from md_html.elements.paragraph import P


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
