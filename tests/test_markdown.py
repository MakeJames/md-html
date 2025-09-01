"""Test the methods of the Markdown module."""

# ruff: noqa: S101, E501

import json

import pytest

from md_html.markdown import Markdown


class TestMarkdown:
    """Test the methods of the Markdown class."""

    @pytest.mark.parametrize(
        "file",
        [
            ("basic"),
            ("code"),
            ("inline-img"),
            ("empty"),
            ("blockquote"),
            ("table"),
            ("lists-and-quotes"),
            ("quantum-slopes"),
            ("a-tower-of-blocks"),
            ("a-grand-day-out"),
            ("perfectly-ripe-tomatoes"),
        ],
    )
    def test_given_markdwon_sections_splits_on_empty_lines(
        self, file, snapshot
    ) -> None:
        """R-BICEP: Right."""
        snapshot.snapshot_dir = "tests/snapshots/markdown/sections/"
        with open(f"./tests/data/{file}.md", "r") as md_file:
            content = md_file.read()
        test = Markdown(content)
        test_sections = json.dumps(list(test.sections))
        snapshot.assert_match(test_sections, f"{file}.json")
