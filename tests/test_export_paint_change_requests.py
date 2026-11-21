"""Tests for the PAINT change-request exporter (family-review ``proposed_action`` rows)."""

import csv
import json
from pathlib import Path

import pytest
import yaml

from ai_gene_review.tools.export_paint_change_requests import (
    COLUMNS,
    collect,
    conflicts,
    main,
    render_report,
    write_outputs,
)

FAMILY_REVIEW = """
family_id: PANTHER:PTHR1
family_name: TEST FAMILY
node_assessments:
  - node_id: PANTHER:PTN10
    asserted_term: {id: "GO:0005518", label: collagen binding}
    node_taxon: {id: "NCBITaxon:6072", label: Eumetazoa}
    evidence: IBD
    paint_snapshot: '20170830'
    assessment: TOO_DEEP
    assessment_reason: >-
      Seeds are vertebrate only.
    proposed_action:
      paint_action: MOVE_IBD
      target_node_id: PANTHER:PTN20
    supported_by:
      - reference_id: PMID:20004161
        supporting_text: Trp52 is indispensable
  - node_id: PANTHER:PTN11
    asserted_term: {id: "GO:0004714", label: transmembrane receptor protein tyrosine kinase activity}
    evidence: IBD
    assessment: NEEDS_PRUNING
    assessment_reason: Dipteran members lost the catalytic residues.
    proposed_action:
      paint_action: ADD_IKR
      target_node_id: PANTHER:PTN30
  - node_id: PANTHER:PTN12
    asserted_term: {id: "GO:0005737", label: cytoplasm}
    evidence: IBD
    assessment: SOUND
"""


def _write(root: Path, family: str, text: str) -> Path:
    """Write a family review at its conventional path under ``root``."""
    path = root / "interpro" / "panther" / family / f"{family}-review.yaml"
    path.parent.mkdir(parents=True)
    path.write_text(text)
    return path


def test_collect_flattens_only_assessments_with_actions(tmp_path: Path) -> None:
    """Each proposed action becomes one row; a SOUND row with no action is skipped."""
    _write(tmp_path, "PTHR1", FAMILY_REVIEW)
    _write(tmp_path, "PTHR2", "family_id: PANTHER:PTHR2\nnode_assessments: []\n")
    rows = collect(tmp_path)
    assert [(r["node_id"], r["paint_action"]) for r in rows] == [
        ("PANTHER:PTN10", "MOVE_IBD"),
        ("PANTHER:PTN11", "ADD_IKR"),
    ]
    move = rows[0]
    assert set(move) == set(COLUMNS)
    assert move["family_id"] == "PANTHER:PTHR1"
    assert move["node_taxon"] == "Eumetazoa"
    assert move["target_node_id"] == "PANTHER:PTN20"
    assert move["request"] == (
        "Move the IBD of GO:0005518 (collagen binding) from PANTHER:PTN10 to PANTHER:PTN20")
    assert move["source_path"] == "interpro/panther/PTHR1/PTHR1-review.yaml"
    assert json.loads(move["supported_by"])[0]["reference_id"] == "PMID:20004161"
    assert rows[1]["request"].startswith("Add an IKR (loss) of GO:0004714")


def test_write_outputs_writes_tsv_and_one_report_per_family(tmp_path: Path) -> None:
    """The TSV has every row and each family gets its own Markdown report."""
    _write(tmp_path, "PTHR1", FAMILY_REVIEW)
    tsv = tmp_path / "out" / "requests.tsv"
    report_dir = tmp_path / "out" / "requests"
    write_outputs(tmp_path, tsv, report_dir)
    with tsv.open() as fh:
        written = list(csv.DictReader(fh, delimiter="\t"))
    assert len(written) == 2
    assert sorted(p.name for p in report_dir.iterdir()) == ["PTHR1.md"]
    report = (report_dir / "PTHR1.md").read_text()
    assert report.startswith("# PAINT change requests for PANTHER:PTHR1 (TEST FAMILY)")
    assert "- **Target node:** PANTHER:PTN30" in report
    assert "> Trp52 is indispensable" in report
    assert "Conflicting requests" not in report


@pytest.mark.parametrize(
    "second_action,second_target,expect_conflict",
    [
        ("MOVE_IBD", "PANTHER:PTN20", False),   # the same request twice
        ("MOVE_IBD", "PANTHER:PTN21", True),    # moved to two different nodes
        ("REMOVE_IBD", None, True),             # moved and removed
    ],
)
def test_conflicting_requests_on_one_row_are_flagged(
        tmp_path: Path, second_action: str, second_target: str | None,
        expect_conflict: bool) -> None:
    """Two incompatible requests on the same PAINT row are reported and fail the export."""
    target = f"\n      target_node_id: {second_target}" if second_target else ""
    extra = f"""  - node_id: PANTHER:PTN10
    asserted_term: {{id: "GO:0005518", label: collagen binding}}
    evidence: IBD
    assessment: TOO_DEEP
    proposed_action:
      paint_action: {second_action}{target}
"""
    _write(tmp_path, "PTHR1", FAMILY_REVIEW.replace("  - node_id: PANTHER:PTN11", extra
                                                    + "  - node_id: PANTHER:PTN11"))
    rows = collect(tmp_path)
    found = conflicts(rows)
    assert bool(found) is expect_conflict
    report = render_report("PANTHER:PTHR1", rows)
    assert ("Conflicting requests" in report) is expect_conflict


def test_losses_below_one_ibd_do_not_conflict() -> None:
    """Several losses requested below the same IBD are independent requests."""
    base = {c: "" for c in COLUMNS}
    first = {**base, "family_id": "F", "node_id": "N", "term_id": "GO:1",
             "paint_action": "ADD_IKR", "target_node_id": "A"}
    assert conflicts([first, {**first, "paint_action": "ADD_IRD", "target_node_id": "B"}]) == []


def test_move_next_to_a_loss_on_one_row_conflicts() -> None:
    """A move and a loss on one PAINT row are two verdicts; the moved IBD may not sit above
    the loss target, which only the tree can tell, so the pair is flagged."""
    base = {c: "" for c in COLUMNS}
    loss = {**base, "family_id": "F", "node_id": "N", "term_id": "GO:1",
            "paint_action": "ADD_IKR", "target_node_id": "A"}
    found = conflicts([loss, {**loss, "paint_action": "MOVE_IBD", "target_node_id": "C"}])
    assert found == ["F: N GO:1 has conflicting requests: ADD_IKR to A; MOVE_IBD to C"]


def test_loss_below_a_removed_ibd_conflicts() -> None:
    """A loss requested below an IBD that another request removes cannot both be filed."""
    base = {c: "" for c in COLUMNS}
    loss = {**base, "family_id": "F", "node_id": "N", "term_id": "GO:1",
            "paint_action": "ADD_IRD", "target_node_id": "A"}
    found = conflicts([loss, {**loss, "paint_action": "REMOVE_IBD", "target_node_id": ""}])
    assert found == ["F: N GO:1 has conflicting requests: ADD_IRD to A; REMOVE_IBD"]


def test_main_exits_nonzero_on_conflict(tmp_path: Path, monkeypatch: pytest.MonkeyPatch,
                                        capsys: pytest.CaptureFixture[str]) -> None:
    """The command line reports each conflict and exits 1, so it cannot pass silently."""
    clash = FAMILY_REVIEW + """  - node_id: PANTHER:PTN10
    asserted_term: {id: "GO:0005518", label: collagen binding}
    evidence: IBD
    assessment: TOO_DEEP
    proposed_action:
      paint_action: REMOVE_IBD
"""
    _write(tmp_path, "PTHR1", clash)
    monkeypatch.setattr("sys.argv", ["prog", "--root", str(tmp_path),
                                     "--tsv", str(tmp_path / "r.tsv"),
                                     "--report-dir", str(tmp_path / "r")])
    with pytest.raises(SystemExit) as exc:
        main()
    assert exc.value.code == 1
    assert "CONFLICT: PANTHER:PTHR1: PANTHER:PTN10" in capsys.readouterr().out


REPO_ROOT = Path(__file__).resolve().parents[1]
TARGETED = {"MOVE_IBD", "ADD_IRD", "ADD_IKR", "MOVE_LOSS"}


def test_committed_family_reviews_export_cleanly() -> None:
    """Every committed proposed action exports to a well-formed request, without conflicts.

    Asserts invariants rather than particular rows, so later curation of a family review
    does not break this test.
    """
    schema = yaml.safe_load(
        (REPO_ROOT / "src/ai_gene_review/schema/family_review.yaml").read_text())
    actions = set(schema["enums"]["PaintActionEnum"]["permissible_values"])
    rows = collect(REPO_ROOT)
    assert rows, "no committed family review carries a proposed_action"
    for r in rows:
        assert r["family_id"].startswith("PANTHER:PTHR"), r
        assert r["node_id"] and r["term_id"], r
        assert r["paint_action"] in actions, r
        assert bool(r["target_node_id"]) is (r["paint_action"] in TARGETED), r
        assert r["request"] and not r["request"].startswith(r["paint_action"]), r
    assert conflicts(rows) == []
