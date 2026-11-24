"""Tests for the RGD triage's module index (projects/RGD_PATHWAY_ONTOLOGY/scripts).

``load_modules`` reads GO and UniProtKB ids from structured ``term.id`` fields only
(ai4curation/ai-gene-review#6006) and follows node-level ``module_ref`` links.
"""

import importlib.util
from pathlib import Path

import yaml

SCRIPT = (
    Path(__file__).resolve().parents[1]
    / "projects"
    / "RGD_PATHWAY_ONTOLOGY"
    / "scripts"
    / "analyze_rgd_pathways.py"
)


def _load_script():
    spec = importlib.util.spec_from_file_location("analyze_rgd_pathways", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _gene(acc: str) -> dict:
    return {
        "participant": {
            "selector_type": "GENE_PRODUCT",
            "gene_product": {"term": {"id": f"UniProtKB:{acc}", "label": acc}},
        }
    }


def _write(path: Path, doc: dict) -> None:
    path.write_text(yaml.safe_dump(doc, sort_keys=False))


def test_structured_ids_only_and_node_refs(tmp_path):
    analyze = _load_script()
    mods = tmp_path / "modules"
    mods.mkdir()
    # B has two steps; A references only B's second step.
    _write(
        mods / "b.yaml",
        {
            "id": "MODULE:b",
            "title": "B",
            "module": {
                "id": "b",
                "parts": [
                    {"node": {"id": "step1", "annotons": [_gene("P00001")]}},
                    {"node": {"id": "step2", "annotons": [_gene("P00002")]}},
                ],
            },
        },
    )
    # C is a separate whole module; a bare-slug reference must not pull it in.
    _write(
        mods / "c.yaml",
        {"id": "MODULE:c", "title": "C",
         "module": {"id": "c", "annotons": [_gene("P00003")]}},
    )
    _write(
        mods / "a.yaml",
        {
            "id": "MODULE:a",
            "title": "A",
            # Ids named only in prose must not count.
            "notes": "Unrelated to UniProtKB:P99999 and GO:0099999.",
            "evidence": [{"source_id": "PW:0000001"}],
            "module": {
                "id": "a",
                "concepts": [{"term": {"id": "GO:0000001", "label": "x"}}],
                "annotons": [_gene("P00004")],
                "parts": [
                    {"node": {"id": "ref_b", "module_ref": "b#step2"}},
                    {"node": {"id": "ref_c", "module_ref": "c"}},
                ],
            },
        },
    )
    up2sym = {"P00001": "G1", "P00002": "G2", "P00003": "G3",
              "P00004": "G4", "P99999": "G9"}

    by_id = {m["id"]: m for m in analyze.load_modules(mods, up2sym)}

    assert by_id["a"]["symbols"] == {"G4", "G2"}
    assert by_id["a"]["go"] == {"GO:0000001"}
    assert by_id["a"]["pw"] == {"PW:0000001"}
    assert by_id["b"]["symbols"] == {"G1", "G2"}


def test_reference_cycle_terminates(tmp_path):
    analyze = _load_script()
    mods = tmp_path / "modules"
    mods.mkdir()
    for name, other in (("x", "y"), ("y", "x")):
        _write(
            mods / f"{name}.yaml",
            {"id": f"MODULE:{name}", "title": name,
             "module": {"id": name, "parts": [
                 {"node": {"id": "n", "annotons": [_gene("P0000" + ("1" if name == "x" else "2"))]}},
                 {"node": {"id": "r", "module_ref": f"{other}#n"}}]}},
        )
    by_id = {m["id"]: m for m in analyze.load_modules(mods, {"P00001": "X", "P00002": "Y"})}
    assert by_id["x"]["symbols"] == {"X", "Y"}
    assert by_id["y"]["symbols"] == {"X", "Y"}


def test_unresolved_node_ref_adds_nothing(tmp_path, capsys):
    analyze = _load_script()
    mods = tmp_path / "modules"
    mods.mkdir()
    _write(
        mods / "big.yaml",
        {"id": "MODULE:big", "title": "Big",
         "module": {"id": "big", "annotons": [_gene("P00005"), _gene("P00006")]}},
    )
    _write(
        mods / "a.yaml",
        {"id": "MODULE:a", "title": "A",
         "module": {"id": "a", "annotons": [_gene("P00004")],
                    "parts": [{"node": {"id": "r", "module_ref": "big#no_such_node"}}]}},
    )
    by_id = {m["id"]: m for m in analyze.load_modules(
        mods, {"P00004": "G4", "P00005": "G5", "P00006": "G6"})}
    assert by_id["a"]["symbols"] == {"G4"}
    assert "unresolved module_ref big#no_such_node" in capsys.readouterr().err
