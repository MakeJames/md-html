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
        "args,return_code,stdouterr,use_script",
        [
            (["--help"], SUCCESS, "usage", True),
            ([], MISSUSE_OF_SHELL, "usage", True),
            (["--version"], SUCCESS, f"md-html {version}", True),
            (["-"], ERROR, "No such file or directory", True),
            (["--help"], SUCCESS, "usage", False),
            ([], MISSUSE_OF_SHELL, "usage", False),
            (["--version"], SUCCESS, f"md-html {version}", False),
            (["-"], ERROR, "No such file or directory", False),
        ],
    )
    def test_cli_interface(
        self,
        run_cli,
        args,
        return_code,
        stdouterr,
        use_script,
    ):
        """R-BICEP: Right."""
        result = run_cli(args, input_data=None, use_script=use_script)
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

    @pytest.mark.parametrize(
        "file",
        [
            ("basic"),
            ("blockquote"),
            ("code"),
            ("empty"),
            ("inline-img"),
            ("mixed-content"),
            ("table"),
            ("a-tower-of-blocks"),
            ("a-grand-day-out"),
            ("perfectly-ripe-tomatoes"),
        ],
    )
    def test_read_file_to_stdout_snapshot(self, file, snapshot, run_cli) -> None:
        """R-BICEP: Right."""
        snapshot.snapshot_dir = "tests/snapshots/cli"
        result = run_cli(args=[f"./tests/data/{file}.md"])
        snapshot.assert_match(result.stdout, f"test_read_file_to_stdout_{file}.html")

    @pytest.mark.parametrize(
        "file,return_code,expect",
        [
            ("basic", 0, None),
            ("blockquote", 0, None),
            ("code", 0, None),
            ("empty", 2, "usage"),
            ("inline-img", 0, None),
            ("mixed-content", 0, None),
            ("table", 0, None),
            ("a-tower-of-blocks", 0, None),
            ("a-grand-day-out", 0, None),
            ("perfectly-ripe-tomatoes", 0, None),
        ],
    )
    def test_stdin_to_stdout_snapshot(
        self, file, return_code, expect, snapshot, run_cli
    ) -> None:
        """R-BICEP: Right."""
        snapshot.snapshot_dir = "tests/snapshots/cli"
        with open(f"./tests/data/{file}.md", "r") as _file:
            data = _file.read()
        result = run_cli(args=[], input_data=data)
        assert result.returncode == return_code
        if expect:
            assert expect in (result.stderr + result.stdout)
        else:
            snapshot.assert_match(
                result.stdout, f"test_read_file_to_stdout_{file}.html"
            )
