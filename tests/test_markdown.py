"""Test the methods of the Markdown module."""

# ruff: noqa: S101, E501

import pytest

from md_html.markdown import Markdown
from tests.utils.template_blocks import Block1, Block2, Block3, Block4


class TestMarkdown:
    """Test the methods of the Markdown class."""

    @pytest.mark.parametrize(
        "content,expected",
        [
            (Block1.md, Block1.sections),
            (Block2.md, Block2.sections),
            (Block3.md, Block3.sections),
            (Block4.md, Block4.sections),
        ],
    )
    def test_given_markdwon_sections_splits_on_empty_lines(
        self, content, expected
    ) -> None:
        """R-BICEP: Right."""
        test = Markdown(content)
        test_sections = list(test.sections)
        assert test_sections == expected
