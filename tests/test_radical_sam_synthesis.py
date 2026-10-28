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
PHASE3_SCOPE = ROOT / "projects" / "RADICAL_SAM" / "data" / "phase3_scope.yaml"


def _build():
    spec = importlib.util.spec_from_file_location("rsam_synthesis", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.build()


def test_committed_synthesis_is_current():
    """data/synthesis.yaml equals a fresh run (the --check contract).

    Compares parsed data, not bytes: the contract is that the committed figures
    match the reviews, and a PyYAML formatting change should not redden CI.
    """
    assert yaml.safe_load(DATA.read_text()) == _build(), (
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
    # The REMOVE breakdown accounts for every REMOVE row.
    assert sum(d["remove_breakdown"].values()) == d["actions_in_reviewed_genes"]["REMOVE"]


def test_phase3_scope_is_covered_and_conformant():
    """Every pre-existing review named in the Phase 3 scope is actually checked.

    The Phase 3 claim on the project page is that the treatment rule now holds
    across the reviews the project did not write, as well as the ones it did.
    That claim is only worth anything if the scope file is non-empty, resolves,
    and comes back clean, so assert all three rather than trusting the prose.
    """
    d = yaml.safe_load(DATA.read_text())
    p3 = d["phase3_rule_conformance"]
    scope = yaml.safe_load(PHASE3_SCOPE.read_text())["genes"]

    assert scope, "the Phase 3 scope file lists no genes"
    assert p3["genes_checked"] == len(scope)
    assert [g["gene"] for g in p3["genes"]] == list(scope)
    # Organism-qualified, so a multi-organism symbol cannot be checked by accident.
    assert all("/" in name for name in scope)
    # The pass is only finished when both scopes come back clean.
    assert p3["deviations"] == [], p3["deviations"]
    assert d["treatment_rule_deviations"] == [], d["treatment_rule_deviations"]
    # Phase 3 reviews stay out of the Phase 4 totals, which report what this
    # project reviewed from scratch. Compared organism-qualified, not by bare
    # symbol: lipA, bioB, moaA, hemN and pqqE are reviewed in several organisms,
    # and it is the review FILE that must not be counted twice.
    phase4 = {f"{v['organism']}/{k}" for k, v in d["genes"].items()}
    assert set(scope).isdisjoint(phase4), sorted(set(scope) & phase4)


def test_documented_rule_exceptions_are_live():
    """A documented exception that matches no row is stale, not a free pass.

    The exception file exists so that honouring the rule table's "keep GO:0046872
    if a separate metal ion is bound" branch never requires editing a test. An
    allowlist nobody checks rots, so assert every declared entry is actually in
    use.
    """
    d = yaml.safe_load(DATA.read_text())
    ex = d["documented_rule_exceptions"]
    assert ex["stale"] == [], ex["stale"]
    assert len(ex["used"]) == len(ex["declared"])


def test_rule_exception_suppresses_a_deviation():
    """The escape hatch works, checked on synthetic rows rather than on the corpus.

    Today no reviewed member binds a mononuclear metal beside its cluster, so the
    declared list is empty and the corpus cannot exercise this path. Drive
    rule_check() directly: the same row is a deviation without an exception and a
    documented exception with one.
    """
    spec = importlib.util.spec_from_file_location("rsam_synthesis", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    rows = [{
        "term": {"id": "GO:0046872", "label": "metal ion binding"},
        "evidence_type": "IDA",
        "review": {"action": "ACCEPT"},
    }]

    _, deviations, _, used = mod.rule_check("someGene", "SOMEORG", rows, True)
    assert len(deviations) == 1 and not used
    assert deviations[0]["term"] == "GO:0046872"

    exceptions = {("SOMEORG", "someGene", "GO:0046872"):
                  {"actions": {"ACCEPT"}, "reason": "binds a separate Zn site"}}
    _, deviations, _, used = mod.rule_check("someGene", "SOMEORG", rows, True,
                                           exceptions)
    assert deviations == []
    assert len(used) == 1
    assert used[0]["documented_exception"] == "binds a separate Zn site"
