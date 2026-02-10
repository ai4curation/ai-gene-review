"""Shared test configuration and fixtures.

Provides automatic VCR cassette recording/replay for integration tests.
"""

from pathlib import Path

import pytest
import vcr


CASSETTES_DIR = Path(__file__).parent / "cassettes"


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
