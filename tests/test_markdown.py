"""Test the methods of the Markdown module."""

# ruff: noqa: S101, E501

import pytest

from md_html.markdown import Markdown


class TestMarkdown:
    """Test the methods of the Markdown class."""

    @pytest.mark.parametrize(
        "file, elements,",
        [
            ("basic", 5),
            ("code", 4),
            ("inline-img", 7),
            ("empty", 0),
            ("blockquote", 4),
            ("table", 3),
            ("lists-and-quotes", 4),
            ("quantum-slopes", 6),
            ("a-tower-of-blocks", 604),
            ("a-grand-day-out", 1759),
            ("perfectly-ripe-tomatoes", 629),
        ],
    )
    def test_given_markdwon_sections_splits_on_empty_lines(
        self, file, elements
    ) -> None:
        """R-BICEP: Right."""
        with open(f"./tests/data/{file}.md", "r") as md_file:
            content = md_file.read()
        test = Markdown(content)
        assert len(list(test.sections)) == elements
