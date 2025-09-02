"""Test the methods of heading package."""

# ruff: noqa: S101

import pytest

from md_html.elements.heading import H


class TestHeading:
    """Test the methods of the H class."""

    @pytest.mark.parametrize(
        "content,valid,level,expected",
        [
            ("# Hello World", True, 1, "<h1># Hello World</h1>"),
            ("## Heading 2", True, 2, "<h2>## Heading 2</h2>"),
            ("### Heading 3", True, 3, "<h3>### Heading 3</h3>"),
            ("#### Heading 4", True, 4, "<h4>#### Heading 4</h4>"),
            ("##### Heading 5", True, 5, "<h5>##### Heading 5</h5>"),
            ("###### Heading 6", True, 6, "<h6>###### Heading 6</h6>"),
            ("##  ## valid", True, 2, "<h2>##  ## valid</h2>"),
            ("  ## Not a valid", False, None, "<p>  ## Not a valid</p>"),
            ("##    valid", True, 2, "<h2>##    valid</h2>"),
            ("####### Heading 7", False, None, "<p>####### Heading 7</p>"),
        ]
    )
    def test_heading_rendered_correctly(self, content, valid, level,
                                        expected) -> None:
        """R-BICEP: Right."""
        test = H(content)
        assert test.html == expected
        assert test._calculate_level() == level == test.level
        assert test._is_valid_heading() is valid
