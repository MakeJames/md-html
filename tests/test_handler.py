"""Test the methods of the handler."""

# ruff: noqa: S101

import pytest

from md_html.handler import main, parser


class TestHandler:
    """Test the instantiation of the cli."""

    def test_when_called_with_no_args_then_help_text(self, capsys) -> None:
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            parser.parse_args([])
        assert e.value.code != 0
        captured = capsys.readouterr()
        assert "usage" in captured.err

    def test_help_flag(self, capsys):
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            parser.parse_args(["--help"])
        assert e.value.code == 0
        captured = capsys.readouterr()
        assert "usage" in captured.out

    def test_version_flag(self, capsys):
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            parser.parse_args(["--version"])
        assert e.value.code == 0
        captured = capsys.readouterr()
        assert "md-html" in captured.out.lower()

    def test_basic_file_to_file(self, tmp_path):
        """R-BICEP: Right."""
        md_file = tmp_path / "input.md"
        md_file.write_text("# Hello\n\nThis is a test.")
        args = parser.parse_args([str(md_file)])
        assert args.file == str(md_file)


class TestCLI:
    """Test the output and processing through the cli."""

    def run_cli(self, args, input_data=None) -> None:
        """Run CLI with subprocess and return result."""
        main(parser.parse_args([*args]), input_data)

    def test_help_flag(self, capsys):
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            self.run_cli(["--help"])
        assert e.value.code == 0
        captured = capsys.readouterr()
        assert "usage" in captured.out.lower()

    def test_no_args_prints_usage(self, capsys):
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            self.run_cli([])
        assert e.value.code != 0
        captured = capsys.readouterr()
        assert "usage" in captured.err.lower()

    def test_version_flag(self, capsys):
        """R-BICEP: Right."""
        with pytest.raises(SystemExit) as e:
            self.run_cli(["--version"])
        assert e.value.code == 0
        captured = capsys.readouterr()
        assert "md-html" in captured.out.lower()

    def test_basic_file_to_file(self, tmp_path):
        """R-BICEP: Right."""
        md_file = tmp_path / "input.md"
        md_file.write_text("# Hello\n\nThis is a test.")
        self.run_cli([str(md_file)])

    def test_stdin_to_stdout(self):
        """R-BICEP: Right."""
        md_text = "# Heading\n\nParagraph"
        self.run_cli(["-"], input_data=md_text)

    def test_file_not_found(self, tmp_path):
        """R-BICEP: Boundary."""
        missing = tmp_path / "does_not_exist.md"
        with pytest.raises(FileNotFoundError):
            self.run_cli([str(missing)])
