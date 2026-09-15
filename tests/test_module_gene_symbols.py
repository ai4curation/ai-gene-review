"""Shared symbol extraction and validation rules."""
from pathlib import Path

import pytest
import yaml

from ai_gene_review.module_logic import abduce, compile_module, is_satisfied, iter_atoms
from ai_gene_review.validation.module_validator import validate_module_file


@pytest.mark.parametrize("label,symbol", [
    ("MetXS (PSEPK)", "MetXS"),
    ("PCK1 (cytosolic PEPCK)", "PCK1"),
    ("B", "B"),
    ("PSEPK AccB", None),
    ("Mycobacterium tuberculosis MetX", None),
    ("human ALDH2", None),
    ("E. coli MetB", None),
    ("Arabidopsis thaliana LACS9", None),
    ("an arbitrary descriptive label", None),
    ("", None),
])
def test_family_only_symbol_rule_and_accession_fallback(tmp_path: Path, label, symbol):
    doc = {"module": {"id": "family_only", "annotons": [{
        "id": "activity",
        "participant": {"selector_type": "FAMILY", "family": {
            "representative_members": [{
                "preferred_term": label,
                "term": {"id": "UniProtKB:Q88CT3"},
            }]
        }}
    }]}}
    circuit = compile_module(doc)
    atom = next(iter_atoms(circuit))
    assert atom.gene_symbol == symbol
    assert atom.gene_symbols == ((symbol,) if symbol else ())
    assert atom.uniprots == ("Q88CT3",)
    assert is_satisfied(circuit, lambda candidate: "Q88CT3" in candidate.uniprots)
    result = abduce(circuit, lambda _: False, asserted_active=True)
    assert result.gap_candidates == {"activity": [symbol] if symbol else []}
    path = tmp_path / "module.yaml"
    path.write_text(yaml.safe_dump(doc))
    warnings = validate_module_file(path).warnings
    symbol_warnings = [w for w in warnings if "SYMBOL_LABEL" in w]
    assert bool(symbol_warnings) == (symbol is None)
    if symbol_warnings:
        assert "representative_members[0]" in symbol_warnings[0]
        assert "symbol-first" in symbol_warnings[0]
