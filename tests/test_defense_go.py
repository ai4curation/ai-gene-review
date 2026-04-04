"""Tests for the extraction-ready defense-family to GO wrapper."""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_gene_review.defense_go import (
    DefenseFamilyPrediction,
    load_default_registry,
    load_registry,
    wrap_prediction,
)


def test_default_registry_exposes_stable_family_ids() -> None:
    """The built-in registry should load the expected stable family IDs."""
    registry = load_default_registry()
    family_ids = {family.id for family in registry.families}
    assert "DEFENSE_FAMILY:CRISPR_CAS" in family_ids
    assert "DEFENSE_FAMILY:RESTRICTION_MODIFICATION" in family_ids
    assert "DEFENSE_FAMILY:CBASS" in family_ids


def test_registry_resolves_aliases_and_labels() -> None:
    """Canonical labels and common aliases should resolve to the same family."""
    registry = load_default_registry()
    assert registry.resolve("CRISPR-Cas").id == "DEFENSE_FAMILY:CRISPR_CAS"
    assert registry.resolve("R-M").id == "DEFENSE_FAMILY:RESTRICTION_MODIFICATION"
    assert registry.resolve("restriction modification").id == "DEFENSE_FAMILY:RESTRICTION_MODIFICATION"


def test_wrap_prediction_returns_automatic_go_terms_for_supported_families() -> None:
    """Supported families should translate into automatic GO term suggestions."""
    wrapped = wrap_prediction(
        DefenseFamilyPrediction(
            family="CRISPR/Cas",
            confidence=0.94,
            source="plm-classifier",
        )
    )
    assert wrapped.family.id == "DEFENSE_FAMILY:CRISPR_CAS"
    assert wrapped.confidence == 0.94
    assert wrapped.source == "plm-classifier"
    assert [mapping.term.id for mapping in wrapped.automatic_terms] == ["GO:0099048"]
    assert not wrapped.review_only_terms


def test_wrap_prediction_preserves_unmapped_families_for_review() -> None:
    """Families without GO policy should still resolve cleanly for review."""
    wrapped = wrap_prediction("CBASS")
    assert wrapped.family.id == "DEFENSE_FAMILY:CBASS"
    assert not wrapped.automatic_terms
    assert any("No automatic GO mapping" in note for note in wrapped.review_notes)


def test_load_registry_rejects_cross_family_alias_collisions(tmp_path: Path) -> None:
    """Alias reuse across families should fail fast during registry load."""
    registry_path = tmp_path / "registry.yaml"
    registry_path.write_text(
        "\n".join(
            [
                'version: "1"',
                "families:",
                "  - id: DEFENSE_FAMILY:ONE",
                "    label: One",
                "    aliases: [shared]",
                "  - id: DEFENSE_FAMILY:TWO",
                "    label: Two",
                "    aliases: [shared]",
            ]
        ),
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="Duplicate defense-family alias"):
        load_registry(registry_path)
