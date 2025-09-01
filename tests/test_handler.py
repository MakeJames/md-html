"""Test the methods of the handler."""

# ruff: noqa: S101

import pytest

from md_html.__version__ import version
from md_html.handler import parser


class TestHandler:
    """Test the instantiation of the cli."""

    def test_when_called_with_no_args_then_file_is_none(self) -> None:
        """R-BICEP: Right."""
        args = parser.parse_args([])
        assert args.file is None

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

    SUCCESS = 0
    ERROR = 1
    MISSUSE_OF_SHELL = 2

    @pytest.mark.parametrize(
        "args,return_code,stdouterr",
        [
            (["--help"], SUCCESS, "usage"),
            ([], MISSUSE_OF_SHELL, "usage"),
            (["--version"], SUCCESS, f"md-html {version}"),
            (["-"], ERROR, "No such file or directory"),

        ]
    )
    def test_cli_interface(self, run_cli, args, return_code, stdouterr):
        """R-BICEP: Right."""
        result = run_cli(args, input_data=None, use_script=True)
        assert result.returncode == return_code
        assert stdouterr in (result.stdout + result.stderr)

    def test_basic_file_to_file(self, tmp_path, run_cli):
        """R-BICEP: Right."""
        md_file = tmp_path / "input.md"
        md_file.write_text("# Hello\n\nThis is a test.")
        result = run_cli([str(md_file)])
        assert result.returncode == 0
        assert "<html lang='en_gb' dir='ltr'>" in result.stdout

    def test_file_not_found(self, tmp_path, run_cli):
        """R-BICEP: Boundary."""
        missing = tmp_path / "does_not_exist.md"
        result = run_cli([str(missing)])
        assert result.returncode == 1
        assert "No such file or directory" in result.stderr
