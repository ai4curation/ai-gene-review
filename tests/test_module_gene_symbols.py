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
    ("SLC25A4 / ANT1 (human)", "SLC25A4"),
    ("Acadvl / CG7461 (Drosophila)", "Acadvl"),
    ("Acaa / Yip2 / CG4600 (Drosophila)", "Acaa"),
    ("SLC25A4 / ANT1", "SLC25A4"),
    ("SepJ / FraG (alr2338), Nostoc sp. PCC 7120", "SepJ"),
    ("PSEPK MetXS / MetX", None),
    ("SLC25A4 / descriptive prose (human)", None),
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


def test_live_carrier_alias_preserves_symbol_predicates():
    from ai_gene_review.module_logic import compile_module_file

    circuit = compile_module_file(Path("modules/oxphos_adenine_nucleotide_phosphate_carriers.yaml"))
    atom = next(a for a in iter_atoms(circuit) if a.node_id == "slc25a4_activity")
    assert atom.gene_symbol == "SLC25A4"
    assert atom.gene_symbols == ("SLC25A4",)
    assert is_satisfied(atom, lambda a: "SLC25A4" in a.gene_symbols)


@pytest.mark.parametrize("participant,path", [
    ({"gene": {"preferred_term": "human ALDH2"}}, "module.annotons[0].participant.gene"),
    ({"complex": {"members": [{"family": {"representative_members": [
        {"preferred_term": "PSEPK AccB"}
    ]}}]}}, "module.annotons[0].participant.complex.members[0].family.representative_members[0]"),
])
def test_symbol_warning_paths_include_gene_and_nested_members(participant, path):
    from ai_gene_review.module_gene_symbols import symbol_label_warnings

    doc = {"module": {"annotons": [{"participant": participant}]}}
    warnings = symbol_label_warnings(doc)
    assert len(warnings) == 1
    assert f"SYMBOL_LABEL {path}:" in warnings[0]
