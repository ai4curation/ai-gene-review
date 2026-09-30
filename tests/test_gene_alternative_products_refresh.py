"""Repair legacy wrapped VSP lists without replacing curated product metadata."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl import gene
from ai_gene_review.validation.goa_validator import GOAValidator


ROOT = next(p for p in Path(__file__).resolve().parents if (p / "pyproject.toml").exists())
BAG6 = ROOT / "genes/human/BAG6/BAG6-uniprot.txt"
SHORT = "VSP_015695, VSP_045910, VSP_045911,"
COMPLETE = "VSP_015695, VSP_045910, VSP_045911, VSP_045912, VSP_045913"


def test_bag6_cached_record_preserves_wrapped_sequence():
    """Use a committed real record, independent of the ATXN2 seed fixture."""
    products = gene._extract_alternative_products(BAG6.read_text(), "P46379")
    assert len(products) == 5
    assert next(p for p in products if p["id"] == "P46379-4")["sequence_note"] == COMPLETE


def test_fetch_repairs_existing_bag6_note_and_preserves_curated_fields(tmp_path, monkeypatch):
    """Run the actual existing-review fetch path with only external work mocked."""
    directory = tmp_path / "genes/human/BAG6"
    directory.mkdir(parents=True)
    review = directory / "BAG6-ai-review.yaml"
    raw = BAG6.read_text()
    goa = "GENE PRODUCT DB\tGENE PRODUCT ID\tGO TERM\n"
    (directory / "BAG6-uniprot.txt").write_text(raw)
    (directory / "BAG6-goa.tsv").write_text(goa)
    original = {
        "id": "P46379",
        "gene_symbol": "BAG6",
        "description": "Curated gene description.",
        "alternative_products": [
            {"id": "P46379-4", "name": "Curated name", "description": "Curated product description.", "sequence_note": SHORT},
            {"id": "P46379-2", "name": "2", "sequence_note": "Curated selection: VSP_015695"},
        ],
        "existing_annotations": [{"term": {"id": "GO:0005515", "label": "protein binding"}, "review": {"action": "UNDECIDED", "reason": "Retain judgment."}}],
    }
    review.write_text(yaml.safe_dump(original, sort_keys=False))
    monkeypatch.setattr(gene, "fetch_uniprot_data", lambda accession: raw)
    monkeypatch.setattr(gene, "fetch_goa_data", lambda accession: goa)
    monkeypatch.setattr(gene, "_extract_panther_family_id", lambda text: None)
    calls = []
    def seed(self, yaml_file, goa_file, fetch_titles=True):
        calls.append((yaml_file, goa_file, fetch_titles))
        return 0, None, 0, 0, 0
    monkeypatch.setattr(GOAValidator, "seed_missing_annotations", seed)
    result = gene.fetch_gene_data(("human", "BAG6"), base_path=tmp_path, fetch_titles=False)
    expected = deepcopy(original)
    expected["alternative_products"][0]["sequence_note"] = COMPLETE
    assert yaml.safe_load(review.read_text()) == expected
    assert result["alternative_product_sequences_repaired"] == 1
    first_bytes = review.read_bytes()
    second = gene.fetch_gene_data(("human", "BAG6"), base_path=tmp_path, fetch_titles=False)
    assert second["alternative_product_sequences_repaired"] == 0
    assert review.read_bytes() == first_bytes
    assert len(calls) == 2 and all(call[2] is False for call in calls)
    assert (directory / "BAG6-uniprot.txt").read_text() == raw
    assert (directory / "BAG6-goa.tsv").read_text() == goa


@pytest.mark.parametrize("old,new", [
    ("Curated: " + SHORT, COMPLETE),
    ("VSP_015695", COMPLETE),  # No dangling comma: not the legacy signature.
    (SHORT, "VSP_999999, VSP_045910, VSP_045911, VSP_045912"),
    (SHORT, "VSP_015695, VSP_045910"),
    (SHORT, SHORT),
    (SHORT, COMPLETE + ","),  # The new list must itself be complete.
    (SHORT, COMPLETE + "; curated explanation"),
    ("Displayed", COMPLETE),
    (None, COMPLETE),
])
def test_refresh_preserves_nonlegacy_or_nonextending_notes(old, new):
    existing = [{"id": "P46379-4", "sequence_note": old}]
    before = deepcopy(existing)
    assert gene._repair_truncated_product_sequences(existing, [{"id": "P46379-4", "sequence_note": new}]) == 0
    assert existing == before


@pytest.mark.parametrize("ambiguous_side", ["existing", "fresh"])
def test_refresh_requires_unique_matching_product_id(ambiguous_side):
    existing = [{"id": "P46379-4", "sequence_note": SHORT}]
    fresh = [{"id": "P46379-4", "sequence_note": COMPLETE}]
    if ambiguous_side == "existing":
        existing.append(deepcopy(existing[0]))
    else:
        fresh.append(deepcopy(fresh[0]))
    before = deepcopy(existing)
    assert gene._repair_truncated_product_sequences(existing, fresh) == 0
    assert existing == before


def test_refresh_does_not_replace_add_or_remove_product_records():
    existing = [{"id": "P46379-4", "name": "curated", "sequence_note": SHORT}, {"id": "P46379-99", "sequence_note": SHORT}]
    fresh = [{"id": "P46379-1"}, {"id": "P46379-4", "name": "4", "sequence_note": COMPLETE}]
    before = deepcopy(existing)
    assert gene._repair_truncated_product_sequences(existing, fresh) == 1
    before[0]["sequence_note"] = COMPLETE
    assert existing == before
    assert gene._repair_truncated_product_sequences(existing, fresh) == 0


@pytest.mark.parametrize("value", [None, {}, "curated explanation"])
def test_refresh_preserves_nonlist_existing_products(value):
    assert gene._repair_truncated_product_sequences(value, [{"id": "P46379-4", "sequence_note": COMPLETE}]) == 0
