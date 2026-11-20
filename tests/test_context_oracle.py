"""Tests for the proteome oracle behind MODULE_CONTEXT conditions."""

from __future__ import annotations

from pathlib import Path

import pytest

from ai_gene_review.context_oracle import (
    Completeness,
    ProteomeInfo,
    check_detector,
    evaluate_cached,
    evaluate_module,
    load_cache,
    load_detector,
    summarise,
)
from ai_gene_review.module_logic import compile_module_file

REPO_ROOT = Path(__file__).resolve().parents[1]
DETECTOR_PATH = REPO_ROOT / "rules/curated/context/ubiquitin_transfer_relay.yaml"


@pytest.fixture(scope="module")
def detector():
    det = load_detector(DETECTOR_PATH)
    det.module_path = REPO_ROOT / det.module_path
    return det


@pytest.fixture(scope="module")
def circuit(detector):
    return compile_module_file(detector.module_path)


def test_detector_covers_every_module_step(detector, circuit) -> None:
    assert check_detector(detector, circuit) == []


def presence(present: set[str], detector) -> dict[str, bool]:
    return {s: s in present for s in detector.signatures}


EUKARYOTE_LIKE = {"IPR045886", "IPR000608", "IPR001841", "IPR000626"}


@pytest.mark.parametrize(
    ("present", "complete", "expected"),
    [
        (EUKARYOTE_LIKE, True, True),
        (EUKARYOTE_LIKE, False, True),
        # SAMP-type archaeon: ThiF-fold E1 only, no UBC E2, no ubiquitin
        ({"IPR045886"}, True, False),
        ({"IPR045886"}, False, None),
        # every enzyme but no modifier (the detector's extra step)
        (EUKARYOTE_LIKE - {"IPR000626"}, True, False),
    ],
)
def test_evaluate_module(detector, circuit, present, complete, expected) -> None:
    assert evaluate_module(detector, presence(present, detector), complete, circuit) is expected


@pytest.mark.parametrize(
    ("ptype", "busco", "level", "complete"),
    [
        ("Reference proteome", 99, "full", True),
        ("Reference proteome", 89, "full", False),
        ("Reference proteome", 99, "partial", False),
        ("Other proteome", 99, "full", False),
        ("Reference proteome", None, "full", False),
    ],
)
def test_completeness(ptype, busco, level, complete) -> None:
    info = ProteomeInfo("UP1", "x", 1, ptype, busco, level)
    assert info.is_complete(Completeness()) is complete


CACHE = load_cache(DETECTOR_PATH)


@pytest.mark.parametrize(
    ("upid", "expected"),
    [
        ("UP000005640", True),   # Homo sapiens
        ("UP000002311", True),   # Saccharomyces cerevisiae
        ("UP000008243", False),  # Haloferax volcanii: SAMP system, no ubiquitin
        ("UP000000242", False),  # Metallosphaera sedula
    ],
)
def test_cached_proteomes_match_known_biology(detector, circuit, upid, expected) -> None:
    """Organisms with a textbook answer, using the committed cache (no network)."""
    assert evaluate_cached(detector, CACHE[upid], circuit) is expected


@pytest.mark.parametrize("upid", sorted(CACHE))
def test_cached_verdicts_are_consistent(detector, circuit, upid) -> None:
    """False is only ever reported for a complete proteome."""
    entry = CACHE[upid]
    verdict = evaluate_cached(detector, entry, circuit)
    if verdict is False:
        assert ProteomeInfo(**entry["proteome"]).is_complete(detector.completeness)


ARCHAEAL_RUN = [
    u for u, e in CACHE.items()
    if "CR-0003" in e.get("rule_matches", {}) and e["proteome"]["taxon_id"] not in (9606, 559292, 83332)
]


def test_bulk_archaeal_run_is_complete_and_adds_up(detector, circuit) -> None:
    """The cached archaeal run covers every proteome and its totals reconcile."""
    assert len(ARCHAEAL_RUN) >= 600
    summary = summarise(detector, CACHE, ARCHAEAL_RUN, "CR-0003", circuit)
    proteins = sum(v["proteins"] for v in summary.values())
    assert proteins == sum(CACHE[u]["rule_matches"]["CR-0003"] for u in ARCHAEAL_RUN)
    # most archaea lack the relay, so the rule blocks most of the mapping
    assert summary["unsatisfiable"]["proteins"] > summary["satisfiable"]["proteins"]
