"""Pytest configuration and fixtures."""

# ruff: noqa: S603

import shutil
import subprocess
import sys

import pytest


@pytest.fixture
def run_cli():
    """Run the md-html CLI safely in a test case.

    Usage:
        def test_case(run_cli) -> None:
            result = run_cli(["--help"])
            assert result.returncode == 0
    """

    def _run_cli(
        args: list[str] | None = None,
        input_data: str | None = None,
        use_script: bool = True,
    ):
        if args is None:
            args = []
        if not all(isinstance(a, str) for a in args):
            raise pytest.UsageError("All CLI arguments must be strings")

        if use_script:
            exe = shutil.which("md-html")
            if exe is None:
                raise pytest.UsageError("md-html script not found in PATH")
            cmd = [exe]
        else:
            cmd = [sys.executable, "-m", "md_html"]

        result = subprocess.run(
            cmd + args,
            input=input_data,
            capture_output=True,
            text=True,
        )
        return result

    return _run_cli
