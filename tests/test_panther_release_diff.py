"""Tests for the PANTHER release-diff dry-run report (no network)."""

from pathlib import Path

import pytest
import yaml

from ai_gene_review.etl.panther_release_diff import (
    Anchor,
    build_report,
    cited_ids,
    collect_anchors,
    propose_remap,
)

MODULE = {
    "id": "example_module",
    "parts": [
        {
            "family": {
                "preferred_term": "STAT transcription factors",
                "term": {"id": "PANTHER:PTHR11801:SF43", "label": "SIGNAL TRANSDUCER"},
                "representative_members": [
                    {"preferred_term": "STAT1", "term": {"id": "UniProtKB:P42224"}},
                    {"preferred_term": "STAT3", "term": {"id": "UniProtKB:P40763"}},
                ],
            }
        },
        {
            "family": {
                "preferred_term": "No members, so not an anchor",
                "term": {"id": "PANTHER:PTHR10000"},
            }
        },
    ],
}

FAMILY_REVIEW = {
    "family_id": "PANTHER:PTHR10133",
    "subfamilies": [
        {
            "subfamily_id": "PANTHER:PTHR10133:SF27",
            "label": "DNA POLYMERASE NU",
            "representative_members": [{"id": "UniProtKB:Q7Z5Q5"}],
        }
    ],
}


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repository with one module and one family review."""
    (tmp_path / "modules").mkdir()
    (tmp_path / "modules" / "example.yaml").write_text(yaml.safe_dump(MODULE))
    review_dir = tmp_path / "interpro" / "panther" / "PTHR10133"
    review_dir.mkdir(parents=True)
    (review_dir / "PTHR10133-review.yaml").write_text(yaml.safe_dump(FAMILY_REVIEW))
    return tmp_path


def test_collect_anchors_reads_modules_and_family_reviews(repo: Path) -> None:
    anchors = collect_anchors(repo)
    assert [(a.file, a.declared, a.members) for a in anchors] == [
        ("modules/example.yaml", ("PTHR11801:SF43",), ("P40763", "P42224")),
        ("interpro/panther/PTHR10133/PTHR10133-review.yaml", ("PTHR10133:SF27",), ("Q7Z5Q5",)),
    ]


def test_build_report_end_to_end(repo: Path) -> None:
    files = sorted(repo.glob("modules/*.yaml")) + sorted(repo.glob("interpro/panther/*/*-review.yaml"))
    current_names = {
        "PTHR11801:SF43": "SIGNAL TRANSDUCER",
        "PTHR10000": "SOME FAMILY",
        "PTHR10133:SF27": "DNA POLYMERASE NU",
        "PTHR10133": "DNA POLYMERASE",
    }
    target_names = {
        "PTHR11801:SF43": "SIGNAL TRANSDUCER",
        "PTHR10133:SF27": "HELICASE AND POLYMERASE-CONTAINING PROTEIN TEBICHI",
        "PTHR10133:SF30": "DNA POLYMERASE NU",
        "PTHR10133": "DNA POLYMERASE",
    }
    current_index = {"P42224": "PTHR11801:SF43", "P40763": "PTHR11801:SF43", "Q7Z5Q5": "PTHR10133:SF27"}
    target_index = {"P42224": "PTHR11801:SF43", "P40763": "PTHR11801:SF43", "Q7Z5Q5": "PTHR10133:SF30"}

    report = build_report(
        "19.0",
        "20.0",
        cited_ids(files, repo),
        current_names,
        target_names,
        collect_anchors(repo),
        current_index,
        target_index,
    )

    # The names share "POLYMERASE", so label_drift calls this rename partial, not divergent.
    assert report["summary"]["ids"] == {"gone": 1, "renamed_partial": 1, "unchanged": 2}
    assert report["summary"]["anchor_remaps"] == {"remap": 1, "unchanged": 1}
    statuses = {entry["id"]: (entry["status"], entry.get("drift")) for entry in report["ids"]}
    assert statuses == {
        "PANTHER:PTHR10000": ("gone", None),
        "PANTHER:PTHR10133:SF27": ("renamed", "partial"),
    }
    (remapped,) = report["anchors"]
    assert remapped["declared"] == ["PANTHER:PTHR10133:SF27"]
    assert remapped["proposed"] == "PANTHER:PTHR10133:SF30"
    assert remapped["members_20.0"] == {"Q7Z5Q5": "PTHR10133:SF30"}
    # The report is plain data that round-trips through YAML.
    assert yaml.safe_load(yaml.safe_dump(report)) == report


@pytest.mark.parametrize(
    ("declared", "target", "status", "proposed"),
    [
        (("PTHR1",), {"P1": "PTHR1:SF3", "P2": "PTHR1:SF4"}, "unchanged", None),
        (("PTHR1",), {"P1": "PTHR2:SF3", "P2": "PTHR2:SF4"}, "remap", "PTHR2"),
        (("PTHR1",), {"P1": "PTHR1:SF3", "P2": "PTHR2:SF4"}, "split", None),
        (("PTHR1:SF3",), {"P1": "PTHR1:SF3"}, "unchanged", None),
        (("PTHR1:SF3",), {"P1": "PTHR1:SF7"}, "remap", "PTHR1:SF7"),
        (("PTHR1", "PTHR2"), {"P1": "PTHR1:SF3"}, "multiple_declared", None),
        (("PTHR1",), {}, "unresolved", None),
    ],
)
def test_propose_remap(declared, target, status, proposed) -> None:
    current = {"P1": "PTHR1:SF3"}
    remap = propose_remap(Anchor("f", "$", declared, ("P1", "P2")), current, target)
    assert (remap.status, remap.proposed) == (status, proposed)
