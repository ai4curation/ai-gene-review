"""The committed RADICAL_SAM synthesis data must match a fresh run.

The Phase 4 project page cites figures from
projects/RADICAL_SAM/data/synthesis.yaml. Without this test the file can drift
from the reviews it is derived from, which is exactly the failure the page's
"computed, not recalled" claim is supposed to rule out.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "projects" / "RADICAL_SAM" / "rsam_synthesis.py"
DATA = ROOT / "projects" / "RADICAL_SAM" / "data" / "synthesis.yaml"


def _build():
    spec = importlib.util.spec_from_file_location("rsam_synthesis", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.build()


def test_committed_synthesis_is_current():
    """data/synthesis.yaml equals a fresh run (the --check contract)."""
    fresh = yaml.safe_dump(_build(), sort_keys=False, allow_unicode=True)
    assert DATA.read_text() == fresh, (
        "projects/RADICAL_SAM/data/synthesis.yaml is stale; re-run "
        "`uv run python projects/RADICAL_SAM/rsam_synthesis.py`"
    )


def test_internal_consistency():
    """Totals the project page quotes must add up within the data itself."""
    d = yaml.safe_load(DATA.read_text())

    reviewed = {k: v for k, v in d["genes"].items() if v["reviewed"]}
    assert d["totals"]["reviewed"] == len(reviewed)
    assert d["totals"]["annotation_rows_in_reviewed_genes"] == sum(
        v["n_rows"] for v in reviewed.values()
    )
    # The action table is the reviewed rows, exactly.
    assert sum(d["actions_in_reviewed_genes"].values()) == \
        d["totals"]["annotation_rows_in_reviewed_genes"]
    # No PENDING survives the reviewed filter.
    assert "PENDING" not in d["actions_in_reviewed_genes"]
    # IBA root causes partition the argued rows.
    assert sum(d["iba_root_causes"].values()) == len(
        d["ibas_whose_node_placement_was_argued"]
    )
    # The SAM buckets partition the reviewed genes, with unreviewed held separate.
    sam = d["sam_binding"]
    assert len(sam["new_rows_absent_from_goa"]) + len(sam["already_in_goa"]) + \
        len(sam["absent_catalysis_not_established"]) == len(reviewed)
    assert set(sam["not_reviewed_so_not_classified"]).isdisjoint(reviewed)
