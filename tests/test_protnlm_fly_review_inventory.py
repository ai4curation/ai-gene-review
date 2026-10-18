"""Zero-output fly records require an explicit reviewed sidecar."""

import importlib.util
from pathlib import Path
from types import ModuleType
from typing import Any

import pytest


def inventory_module() -> ModuleType:
    """Load the project-specific coverage checker without running it."""
    path = Path("projects/PROTNLM_EVALUATION/fly-benchmark/review_inventory.py")
    spec = importlib.util.spec_from_file_location("fly_review_inventory", path)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize(
    "sidecar, expected",
    [
        ({}, False),
        ({"id": "TARGET", "status": "COMPLETE", "description": "No GO output."}, False),
        ({"id": "TARGET", "predictions": []}, False),
        ({"id": "TARGET", "status": "COMPLETE", "description": " ", "predictions": []}, False),
        ({"id": "OTHER", "status": "COMPLETE", "description": "No GO output.", "predictions": []}, False),
        ({"id": "TARGET", "status": "COMPLETE", "description": "No GO output.", "predictions": []}, True),
    ],
)
def test_zero_output_requires_identity_explicit_list_and_summary(
    sidecar: dict[str, Any], expected: bool,
) -> None:
    """Missing work must not be silently equated with an assessed omission."""
    assert inventory_module().go_sidecar_matches_source(sidecar, "TARGET", []) is expected


def test_empty_review_cannot_cover_an_emitted_go_prediction() -> None:
    """An empty sidecar cannot erase a source claim from the denominator."""
    sidecar = {"id": "TARGET", "status": "COMPLETE", "description": "No GO output.", "predictions": []}
    source = [{"id": "GO:0005214", "text": "F:structural constituent of chitin-based cuticle"}]
    assert not inventory_module().go_sidecar_matches_source(sidecar, "TARGET", source)


def test_existing_go_assessment_still_matches_source() -> None:
    """The coverage check preserves emitted terms and their valid assessments."""
    source = [{"id": "GO:0005214", "text": "F:structural constituent of chitin-based cuticle"}]
    sidecar = {"id": "TARGET", "predictions": [{
        "predicted_term": {"id": "GO:0005214", "label": "structural constituent of chitin-based cuticle"},
        "review": {"assessment": "LSP"},
    }]}
    assert inventory_module().go_sidecar_matches_source(sidecar, "TARGET", source)
