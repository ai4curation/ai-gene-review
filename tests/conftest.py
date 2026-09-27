"""Shared test configuration and fixtures.

Provides automatic VCR cassette recording/replay for integration tests.
"""

import builtins
import os
from pathlib import Path

import pytest
import vcr


CASSETTES_DIR = Path(__file__).parent / "cassettes"
WORKING_TREE_GENES = Path(__file__).resolve().parents[1] / "genes"


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

    for name in ("open", "read_text", "read_bytes", "exists", "is_file", "glob", "iterdir"):
        monkeypatch.setattr(Path, name, guarded_method(name))

    original_open = builtins.open

    def guarded_open(file, *args, **kwargs):
        if isinstance(file, (str, os.PathLike)):
            check(file)
        return original_open(file, *args, **kwargs)

    monkeypatch.setattr(builtins, "open", guarded_open)
