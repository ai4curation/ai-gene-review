"""Tests for rule enrichment functionality."""

import json
import tempfile
from pathlib import Path

import pytest

from ai_gene_review.etl.rule_enrichment import (
    EnrichedLabel,
    EnrichmentCache,
    LabelEnricher,
    enrich_rule_json,
)


def test_enriched_label():
    """Test EnrichedLabel creation."""
    label = EnrichedLabel(
        original_id="GO:0036435",
        curie="GO:0036435",
        label="lipoprotein particle receptor activity"
    )
    assert label.original_id == "GO:0036435"
    assert label.curie == "GO:0036435"
    assert label.label == "lipoprotein particle receptor activity"


def test_enrichment_cache_save_load():
    """Test cache save and load."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_file = Path(tmpdir) / "labels.json"

        # Create and populate cache
        cache = EnrichmentCache()
        cache.go_labels = {"GO:0006915": "apoptotic process"}
        cache.interpro_labels = {"IPR000001": "Kringle"}
        cache.cache_file = cache_file
        cache.save()

        # Verify file was created
        assert cache_file.exists()

        # Load into new cache
        cache2 = EnrichmentCache()
        cache2.load(cache_file)

        assert cache2.go_labels == {"GO:0006915": "apoptotic process"}
        assert cache2.interpro_labels == {"IPR000001": "Kringle"}


def test_normalize_taxon():
    """Test taxon normalization to CURIE format."""
    enricher = LabelEnricher()

    # With cv_id
    result = enricher.normalize_taxon("Fungi", "4751")
    assert result.curie == "NCBITaxon:4751"
    assert result.label == "Fungi"
    assert result.original_id == "Fungi"

    # Without cv_id
    result = enricher.normalize_taxon("Unknown", None)
    assert result.curie == "Unknown"
    assert result.label == "Unknown"


def test_enrich_condition_value_taxon():
    """Test enriching a taxon condition value."""
    enricher = LabelEnricher()

    result = enricher.enrich_condition_value("taxon", "Bacteria", "2")
    assert result.curie == "NCBITaxon:2"
    assert result.label == "Bacteria"
    assert result.source == "ncbi_taxonomy"


def test_enrich_condition_value_interpro():
    """Test enriching an InterPro condition value."""
    enricher = LabelEnricher()

    result = enricher.enrich_condition_value("InterPro id", "IPR000001", None)
    assert result.curie == "InterPro:IPR000001"
    # Label may or may not be fetched depending on network


def test_enrich_condition_value_funfam():
    """Test enriching a FunFam condition value."""
    enricher = LabelEnricher()

    result = enricher.enrich_condition_value("FunFam id", "1.10.510.10:FF:000100", None)
    assert result.curie == "CATH.FunFam:1.10.510.10:FF:000100"


def test_enrich_go_annotation():
    """Test enriching a GO annotation."""
    enricher = LabelEnricher()

    result = enricher.enrich_go_annotation("GO:0006915")
    assert result.curie == "GO:0006915"
    # Label may or may not be fetched depending on network


def test_enrich_rule_json_taxon():
    """Test enriching rule JSON with taxon."""
    rule = {
        "mainRule": {
            "conditionSets": [{
                "conditions": [{
                    "type": "taxon",
                    "conditionValues": [{"value": "Fungi", "cvId": "4751"}]
                }]
            }],
            "annotations": []
        }
    }

    enriched = enrich_rule_json(rule)

    cv = enriched["mainRule"]["conditionSets"][0]["conditions"][0]["conditionValues"][0]
    assert cv["curie"] == "NCBITaxon:4751"
    assert cv["label"] == "Fungi"
    assert cv["value"] == "Fungi"  # Original preserved
    assert cv["cvId"] == "4751"  # Original preserved


def test_enrich_rule_json_preserves_original():
    """Test that enrichment doesn't modify original dict."""
    rule = {
        "mainRule": {
            "conditionSets": [{
                "conditions": [{
                    "type": "taxon",
                    "conditionValues": [{"value": "Fungi", "cvId": "4751"}]
                }]
            }],
            "annotations": []
        }
    }

    # Make a copy of original for comparison
    original_json = json.dumps(rule)

    enrich_rule_json(rule)

    # Original should be unchanged
    assert json.dumps(rule) == original_json


def test_enrichment_cache_with_enricher():
    """Test that enricher uses cache correctly."""
    with tempfile.TemporaryDirectory() as tmpdir:
        cache_dir = Path(tmpdir)

        # Pre-populate cache
        cache_file = cache_dir / "_labels.json"
        cache_data = {
            "go_labels": {"GO:0006915": "apoptotic process"},
            "interpro_labels": {},
            "funfam_labels": {}
        }
        cache_file.write_text(json.dumps(cache_data))

        # Create enricher with cache
        enricher = LabelEnricher(cache_dir=cache_dir)

        # Should get cached value without API call
        label = enricher.get_go_label("GO:0006915")
        assert label == "apoptotic process"


@pytest.mark.integration
def test_get_go_label_quickgo():
    """Test fetching GO label from QuickGO API."""
    enricher = LabelEnricher()

    label = enricher.get_go_label("GO:0006915")
    assert label is not None
    assert "apoptotic" in label.lower()


@pytest.mark.integration
def test_get_go_labels_batch_quickgo():
    """Test batch fetching GO labels from QuickGO API."""
    enricher = LabelEnricher()

    labels = enricher.get_go_labels_batch(["GO:0006915", "GO:0005737", "GO:0008150"])
    assert len(labels) >= 1
    # At least one should be fetched
    assert any(v for v in labels.values())


@pytest.mark.integration
def test_get_interpro_label():
    """Test fetching InterPro label from API."""
    enricher = LabelEnricher()

    label = enricher.get_interpro_label("IPR000001")
    assert label is not None
    assert "Kringle" in label


@pytest.mark.integration
def test_get_funfam_label():
    """Test fetching FunFam label from CATH API."""
    enricher = LabelEnricher()

    # Use a known FunFam ID
    label = enricher.get_funfam_label("1.10.510.10:FF:000100")
    # May return None if API changes, but should not error
    assert label is None or isinstance(label, str)


@pytest.mark.integration
def test_enrich_full_rule():
    """Test enriching a complete rule JSON."""
    rule = {
        "uniRuleId": "TEST001",
        "mainRule": {
            "conditionSets": [{
                "conditions": [
                    {
                        "type": "taxon",
                        "conditionValues": [{"value": "Fungi", "cvId": "4751"}]
                    },
                    {
                        "type": "InterPro id",
                        "conditionValues": [{"value": "IPR000001"}]
                    }
                ]
            }],
            "annotations": [
                {
                    "dbReference": {
                        "database": "GO",
                        "id": "GO:0006915"
                    }
                }
            ]
        }
    }

    enricher = LabelEnricher()
    enriched = enrich_rule_json(rule, enricher)

    # Check taxon enrichment
    taxon_cv = enriched["mainRule"]["conditionSets"][0]["conditions"][0]["conditionValues"][0]
    assert taxon_cv["curie"] == "NCBITaxon:4751"

    # Check InterPro enrichment
    interpro_cv = enriched["mainRule"]["conditionSets"][0]["conditions"][1]["conditionValues"][0]
    assert interpro_cv["curie"] == "InterPro:IPR000001"

    # Check GO enrichment (label may or may not be present depending on API)
    go_ref = enriched["mainRule"]["annotations"][0]["dbReference"]
    assert "label" in go_ref  # Key should be present even if None
