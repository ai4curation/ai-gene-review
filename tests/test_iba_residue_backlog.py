"""The residue-evidence backlog that ``projects/IBA_REVIEW/tree_evidence.py --residue-backlog`` lists.

The script is a project tool, not a package module, so it is loaded by path.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType
from typing import Any

import yaml

SCRIPT = Path(__file__).parent.parent / "projects" / "IBA_REVIEW" / "tree_evidence.py"


def _load() -> ModuleType:
    spec = importlib.util.spec_from_file_location("iba_tree_evidence_analysis", SCRIPT)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules["iba_tree_evidence_analysis"] = module
    spec.loader.exec_module(module)
    return module


analysis = _load()

LOSS = {"root_cause": "PROPAGATION_BAD", "failure_modes": ["PSEUDO_OR_SUBACTIVITY_LOSS"]}


def row(term: str, action: str, **propagation: Any) -> dict[str, Any]:
    return {
        "term": {"id": term, "label": f"label of {term}"},
        "evidence_type": "IEA",
        "review": {"action": action, "propagation_review": {**LOSS, **propagation}},
    }


def write_review(root: Path, gene: str, rows: list[dict[str, Any]]) -> Path:
    folder = root / "genes" / "human" / gene
    folder.mkdir(parents=True)
    (folder / f"{gene}-ai-review.yaml").write_text(yaml.safe_dump({"existing_annotations": rows}), encoding="utf-8")
    return folder


def test_the_backlog_is_the_overruled_rows_without_a_residue_claim(tmp_path: Path) -> None:
    write_review(tmp_path, "AAA", [
        row("GO:0000001", "REMOVE"),
        row("GO:0000002", "REMOVE", residue_claims=[{"claim_type": "LOST"}]),
        row("GO:0000003", "MARK_AS_OVER_ANNOTATED", residue_claims_not_applicable="a missing domain, not a residue"),
        row("GO:0000004", "KEEP_AS_NON_CORE"),
    ])
    write_review(tmp_path, "BBB", [{"term": {"id": "GO:0000005"}, "evidence_type": "IEA", "review": {"action": "REMOVE"}}])

    backlog = analysis.residue_backlog(tmp_path)

    assert backlog["rows"] == [{
        "gene": "human/AAA", "term": "GO:0000001", "label": "label of GO:0000001", "evidence_type": "IEA",
        "action": "REMOVE", "has_extract": False, "curated_sites_in_extract": 0,
    }]
    assert backlog["counts"] == {
        "reviews_read": 2,
        "rows_with_the_failure_mode": 4,
        "reviews_with_the_failure_mode": 1,
        "rows_with_residue_claims": 1,
        "rows_with_residue_claims_not_applicable": 1,
        "rows_not_asked_because_not_overruled": 1,
        "rows_without_a_claim": 1,
        "reviews_without_a_claim": 1,
        "rows_whose_extract_has_curated_sites": 0,
    }


def test_curated_sites_are_counted_from_the_extract(tmp_path: Path) -> None:
    folder = write_review(tmp_path, "AAA", [row("GO:0000001", "REMOVE")])
    extract = folder / "AAA-phylo.yaml"
    assert analysis.curated_sites(extract) == 0
    extract.write_text(
        yaml.safe_dump({"trees": [{"family": "PTHR1", "residue_sites": [{"site": "a"}, {"site": "b"}]}, {"family": "PTHR2"}]}),
        encoding="utf-8",
    )
    assert analysis.curated_sites(extract) == 2
    listed = analysis.residue_backlog(tmp_path)["rows"][0]
    assert (listed["has_extract"], listed["curated_sites_in_extract"]) == (True, 2)
