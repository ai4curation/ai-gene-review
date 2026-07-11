"""Offline tests for the generic module genome-scan tool and module detection."""
from pathlib import Path

import pytest

from ai_gene_review.module_scan import Component, extract_components, _acc_from_name
from ai_gene_review.render_modules import is_module_document


@pytest.mark.parametrize("name,expected", [
    ("tr|B2J2S4|B2J2S4_NOSP7", "B2J2S4"),
    ("sp|P46079|Y2393_NOSS1", "P46079"),
    ("A0ACD7RWW5", "A0ACD7RWW5"),
    ("plainname", "plainname"),
])
def test_acc_from_name(name, expected):
    assert _acc_from_name(name) == expected


def test_extract_components_family_and_exemplars():
    module = {
        "module": {
            "parts": [
                {"node": {"annotons": [
                    {"label": "FraD anchor", "participant": {
                        "selector_type": "FAMILY",
                        "family": {
                            "term": {"id": "InterPro:IPR020360", "label": "FraD family"},
                            "representative_members": [
                                {"term": {"id": "UniProtKB:P46079", "label": "FraD"}},
                            ],
                        }}},
                    {"label": "SepN plug", "participant": {
                        "selector_type": "FAMILY",
                        "family": {  # no family term -> exemplar only
                            "representative_members": [
                                {"term": {"id": "UniProtKB:A0ACD7RWW5", "label": "SepN"}},
                            ]}}},
                ]}},
            ],
        }
    }
    comps = extract_components(module)
    by_label = {c.label: c for c in comps}
    assert set(by_label) == {"FraD anchor", "SepN plug"}
    frad = by_label["FraD anchor"]
    assert frad.family_terms == ["InterPro:IPR020360"]
    assert frad.exemplars == ["P46079"]
    assert frad.interpro_terms == ["IPR020360"]
    sepn = by_label["SepN plug"]
    assert sepn.family_terms == []          # no family model
    assert sepn.exemplars == ["A0ACD7RWW5"]
    assert sepn.interpro_terms == []


def test_extract_components_gene_product_and_complex_units():
    module = {"module": {"annotons": [
        {"label": "single", "participant": {
            "selector_type": "GENE_PRODUCT",
            "gene_product": {"term": {"id": "UniProtKB:Q99999", "label": "x"}}}},
        {"label": "complex", "participant": {
            "selector_type": "PROTEIN_COMPLEX",
            "protein_complex": {"active_units": [
                {"participant": {"gene_product": {"term": {"id": "UniProtKB:P11111"}}}},
                {"participant": {"gene_product": {"term": {"id": "UniProtKB:P22222"}}}},
            ]}}},
    ]}}
    comps = {c.label: c for c in extract_components(module)}
    assert comps["single"].exemplars == ["Q99999"]
    assert comps["complex"].exemplars == ["P11111", "P22222"]


def test_extract_components_skips_ungrounded():
    module = {"module": {"annotons": [
        {"label": "abstract", "participant": {"selector_type": "ANY_WITH_FUNCTION"}},
    ]}}
    assert extract_components(module) == []


def test_is_module_document(tmp_path: Path):
    real = tmp_path / "m.yaml"
    real.write_text("id: MODULE:x\ntitle: X\nmodule:\n  id: x\n")
    assert is_module_document(real) is True

    not_module = tmp_path / "config.yaml"
    not_module.write_text("name: not-a-module\nfoo:\n  module: nested-key-not-top\n")
    assert is_module_document(not_module) is False

    nested = tmp_path / "n.yaml"
    nested.write_text("outer:\n  module:\n    id: x\n")  # 'module' only as nested key
    assert is_module_document(nested) is False
