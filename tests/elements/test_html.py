"""Test the methods of the HTML package."""

# ruff: noqa: S101

import json

import pytest

from md_html.elements.html import HTML


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
    def test_html_render_of_html_elements(self, title, file, attr, snapshot) -> None:
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
