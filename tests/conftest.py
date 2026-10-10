"""Shared test configuration and fixtures.

Provides automatic VCR cassette recording/replay for integration tests, and
fails the run if any test writes into the committed publications/ or genes/.
"""

import builtins
import os
import subprocess
from pathlib import Path
from typing import Optional

import pytest
import vcr


CASSETTES_DIR = Path(__file__).parent / "cassettes"


REPO_ROOT = Path(__file__).resolve().parents[1]
WORKING_TREE_GENES = REPO_ROOT / "genes"
# Committed curated data that no test may write to; tests use tmp_path instead.
PROTECTED_TREES = ("publications", "genes")


def _protected_tree_status() -> Optional[str]:
    """Return git's porcelain status of the protected trees, or None without git.

    Untracked files are included, so a newly cached ``PMID_*.md`` counts too.
    """
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", "--untracked-files=all", "--", *PROTECTED_TREES],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
    except (OSError, subprocess.CalledProcessError):  # not a git checkout
        return None
    return result.stdout


def pytest_sessionstart(session):
    """Snapshot the protected trees before any test runs."""
    session.config._protected_tree_status = _protected_tree_status()


def pytest_sessionfinish(session, exitstatus):
    """Fail the run if any test changed committed publications/ or genes/ files."""
    before = getattr(session.config, "_protected_tree_status", None)
    if before is None:
        return
    after = _protected_tree_status()
    if after is None or after == before:
        return
    changed = sorted(set(after.splitlines()) - set(before.splitlines()))
    reporter = session.config.pluginmanager.get_plugin("terminalreporter")
    message = (
        "Tests modified the committed "
        + "/".join(PROTECTED_TREES)
        + " trees (write to tmp_path instead):\n  "
        + "\n  ".join(changed or ["(status changed for already-modified files)"])
    )
    if reporter is not None:
        reporter.write_line(message, red=True, bold=True)
    session.exitstatus = pytest.ExitCode.TESTS_FAILED


def pytest_addoption(parser):
    """Add --vcr-record CLI option."""
    parser.addoption(
        "--vcr-record",
        default="none",
        choices=["none", "new_episodes", "all"],
        help=(
            "VCR record mode: "
            "'none' replays existing cassettes (default), "
            "'new_episodes' records only new requests, "
            "'all' re-records everything"
        ),
    )


@pytest.fixture(autouse=True)
def _vcr_cassette(request):
    """Auto-apply VCR cassette to @pytest.mark.integration tests.

    Non-integration tests are unaffected (fixture is a no-op).
    Cassettes are stored at tests/cassettes/<module>/<test_node_name>.yaml.
    Parametrized tests get unique cassettes via pytest's node name.
    """
    marker = request.node.get_closest_marker("integration")
    if marker is None:
        yield
        return

    # Allow tests to opt out of VCR (e.g. oaklib downloads multi-GB databases)
    if request.node.get_closest_marker("vcr_skip"):
        yield
        return

    record_mode = request.config.getoption("--vcr-record")

    # Build cassette path from test module and node name
    module_name = request.node.module.__name__.rsplit(".", 1)[-1]
    # node name includes parametrize suffixes, e.g. test_foo[param1-param2]
    test_name = request.node.name
    cassette_dir = CASSETTES_DIR / module_name
    cassette_dir.mkdir(parents=True, exist_ok=True)
    cassette_path = str(cassette_dir / f"{test_name}.yaml")

    my_vcr = vcr.VCR(
        record_mode=record_mode,
        cassette_library_dir=str(cassette_dir),
        decode_compressed_response=True,
        match_on=["method", "uri", "body"],
        filter_headers=["Authorization", "X-API-Key", "Cookie"],
    )

    with my_vcr.use_cassette(cassette_path):
        yield


@pytest.fixture
def forbid_working_tree_genes(monkeypatch):
    """Fail if the code under test reads anything under the working-tree ``genes/``.

    Benchmark generators must read gene inputs at the declared review snapshot
    commit, so an ordinary curation edit to a gene review cannot stale them.
    """

    def check(path) -> None:
        if Path(os.path.abspath(os.fspath(path))).is_relative_to(WORKING_TREE_GENES):
            raise AssertionError(f"working-tree gene file consulted: {path}")

    def guarded_method(name: str):
        original = getattr(Path, name)

        def wrapper(self, *args, **kwargs):
            check(self)
            return original(self, *args, **kwargs)

        return wrapper

    for name in ("open", "read_text", "read_bytes", "exists", "is_file", "iterdir"):
        monkeypatch.setattr(Path, name, guarded_method(name))

    def guarded_search(name: str):
        # ``REPO_ROOT.glob("genes/...")`` starts outside genes/, so check every match too.
        original = getattr(Path, name)

        def wrapper(self, *args, **kwargs):
            check(self)
            for match in original(self, *args, **kwargs):
                check(match)
                yield match

        return wrapper

    for name in ("glob", "rglob"):
        monkeypatch.setattr(Path, name, guarded_search(name))

    def guarded_listing(original):
        def wrapper(path="."):
            if isinstance(path, (str, os.PathLike)):
                check(path)
            return original(path)

        return wrapper

    monkeypatch.setattr(os, "scandir", guarded_listing(os.scandir))
    monkeypatch.setattr(os, "listdir", guarded_listing(os.listdir))

    original_open = builtins.open

    def guarded_open(file, *args, **kwargs):
        if isinstance(file, (str, os.PathLike)):
            check(file)
        return original_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", guarded_open)
