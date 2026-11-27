"""Tests for the litscan gene-gap scan (offline unless marked integration)."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app
from ai_gene_review.litscan import gene_gap
from ai_gene_review.litscan.europepmc import publication_from_record
from ai_gene_review.litscan.gene_gap_sources import choose_entry

REPO = Path(__file__).resolve().parents[1]
CONFIG_PATH = REPO / "conf" / "litscan" / "gene_gap.yaml"


@pytest.fixture(scope="module")
def config() -> dict[str, Any]:
    return gene_gap.load_config(CONFIG_PATH)


def counts(**overrides: int) -> dict[str, int]:
    base = {
        "total": 0,
        "experimental": 0,
        "experimental_protein_binding": 0,
        "experimental_mf": 0,
        "experimental_aspects": 0,
        "iba": 0,
        "iea": 0,
        "homology": 0,
        "other": 0,
    }
    base.update(overrides)
    return base


def make_gene(**overrides: Any) -> dict[str, Any]:
    gene = {
        "accession": "P45944",
        "entry_name": "YQCI_BACSU",
        "symbol": "yqcI",
        "matched_symbol": "YqcI",
        "matched_in_title": True,
        "protein_name": "Uncharacterized protein YqcI",
        "organism": "Bacillus subtilis (strain 168)",
        "taxon_id": 224308,
        "folder": "BACSU",
        "reviewed": True,
        "protein_existence": "3: Inferred from homology",
        "annotation_counts": counts(total=2, iba=2),
        "family": {
            "panther_id": "PTHR40045",
            "panther_name": "YCGG FAMILY PROTEIN",
            "member_count": 900,
            "experimental_member_count": 0,
        },
        "unknown_function_domains": [],
        "paper_in_goa": False,
    }
    gene.update(overrides)
    return gene


def make_candidate(
    config: dict[str, Any],
    gene: dict[str, Any],
    *,
    pmid: str = "42980640",
    title: str = "",
) -> dict[str, Any]:
    title = (
        title or "YqcI/YcgG heme monooxygenases: a new fold for guanidine N-oxygenation"
    )
    paper = {
        "pmid": pmid,
        "reference_id": f"PMID:{pmid}",
        "title": title,
        "journal": "J Test",
        "publication_date": "2026-11-01",
        "doi": "10.1/x",
        "source": "MED",
        "pubmed_url": f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
        "europe_pmc_url": f"https://europepmc.org/article/MED/{pmid}",
        "abstract": "We purified recombinant YqcI and measured kcat for this uncharacterized protein.",
        "profiles": ["dark_gene"],
        "is_preprint": False,
        "full_text_available": True,
    }
    return gene_gap.score_candidate(paper, gene, config)


def test_config_validates_against_schema() -> None:
    assert gene_gap.validate_files([CONFIG_PATH]) == []


def test_bad_config_fails_validation(tmp_path: Path, config: dict[str, Any]) -> None:
    bad = copy.deepcopy(config)
    del bad["limits"]["max_issues"]
    bad["paper_scoring"][0]["field"] = "body"
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(bad))
    problems = gene_gap.validate_files([path])
    assert any("max_issues" in p for p in problems)
    assert any("body" in p for p in problems)


@pytest.mark.parametrize(
    "gene_overrides,expected_rules,excluded_rules",
    [
        # IBA-only uncharacterized protein in an unstudied family: maximal gap.
        (
            {},
            {
                "known_function_rows",
                "no_experimental_mf",
                "electronic_only",
                "uncharacterized_name",
                "family_experimental",
            },
            {
                "existing_review_not_citing",
                "already_in_goa",
                "total_annotations",
                "experimental_aspects",
            },
        ),
        # Well-annotated gene with a review that does not cite the paper.
        (
            {
                "protein_name": "Cellular tumor antigen p53",
                "annotation_counts": counts(
                    total=1000,
                    experimental=800,
                    experimental_protein_binding=500,
                    experimental_mf=600,
                    experimental_aspects=3,
                    iba=8,
                    iea=40,
                    other=152,
                ),
                "family": None,
                "review_path": "genes/human/TP53/TP53-ai-review.yaml",
            },
            {
                "known_function_rows",
                "total_annotations",
                "experimental_aspects",
                "existing_review_not_citing",
            },
            {"no_experimental_mf", "electronic_only", "uncharacterized_name"},
        ),
        # One experimental row but many ISO transfers from the ortholog: not dark.
        (
            {
                "annotation_counts": counts(
                    total=61,
                    experimental=1,
                    experimental_aspects=1,
                    homology=34,
                    iba=3,
                    iea=22,
                    other=1,
                )
            },
            {"no_experimental_mf", "total_annotations", "known_function_rows"},
            {"electronic_only", "experimental_aspects"},
        ),
        # Paper already used by GOA for the gene.
        ({"paper_in_goa": True}, {"already_in_goa"}, set()),
        # A Pfam DUF on the entry.
        ({"unknown_function_domains": ["DUF1234"]}, {"duf_domain"}, set()),
    ],
)
def test_score_gene_rules(
    config: dict[str, Any],
    gene_overrides: dict[str, Any],
    expected_rules: set[str],
    excluded_rules: set[str],
) -> None:
    gene = {k: v for k, v in make_gene(**gene_overrides).items() if v is not None}
    rules = {c["rule"] for c in gene_gap.score_gene(gene, config["gene_scoring"])}
    assert expected_rules <= rules
    assert not (excluded_rules & rules)


def test_well_annotated_gene_is_down_ranked(config: dict[str, Any]) -> None:
    dark = make_candidate(config, make_gene())
    known = make_candidate(
        config,
        make_gene(
            accession="P04637",
            protein_name="Cellular tumor antigen p53",
            annotation_counts=counts(
                total=1000, experimental=800, experimental_mf=600, other=200
            ),
            family={
                "panther_id": "PTHR11447",
                "member_count": 3000,
                "experimental_member_count": 200,
            },
        ),
        pmid="1",
    )
    assert dark["score"] > known["score"]
    ranked = gene_gap.rank_candidates([known, dark], config["limits"])
    assert [c["gene"]["accession"] for c in ranked] == ["P45944", "P04637"]


@pytest.mark.parametrize(
    "title,rule",
    [
        ("A genome-wide CRISPR screen identifies regulators of X", "high_throughput"),
        ("FOO1 is a pseudokinase that scaffolds BAR", "pseudoenzyme_title"),
        ("FOO1 is catalytically inactive in vivo", "refutation"),
        ("Functions of FOO family proteins: a review", "review_like"),
        ("Prognostic biomarker FOO1 in a lung cancer cohort", "clinical"),
        (
            "Characterization of a previously uncharacterized protein FOO1",
            "first_characterization",
        ),
    ],
)
def test_score_paper_rules(config: dict[str, Any], title: str, rule: str) -> None:
    fired = {
        c["rule"]
        for c in gene_gap.score_paper(
            title,
            "",
            config["paper_scoring"],
            gene_in_title=False,
            matched_symbol="FOO1",
            full_text_available=True,
        )
    }
    assert rule in fired


@pytest.mark.parametrize(
    "title,abstract,full_text,expected,excluded",
    [
        # Background naming of the pseudoenzyme class is not a refutation.
        (
            "FOO1 supports glycolysis in melanoma cells",
            "The pseudokinase FOO1 is highly expressed in melanoma. FOO1 knockout "
            "cells proliferate less. FOO1 expression promotes a glycolytic phenotype.",
            True,
            {"phenotype_only", "indirect_effect", "gene_experiment"},
            {"refutation", "pseudoenzyme_title", "direct_assay", "abstract_only"},
        ),
        # A co-subject under a partner's title, with a binding assay and rescue.
        (
            "BAR2 suppresses the FOO1-BAZ1 axis in tumors",
            "BAR2 physically interacts with FOO1 and ubiquitinates FOO1 at the Lys102 "
            "residue. Loss of FOO1 destabilizes the BAZ1 complex. Elevated FOO1 "
            "expression counteracts BAR2-mediated radiosensitization.",
            True,
            {"gene_focus", "direct_assay", "rescue_or_epistasis"},
            {"phenotype_only", "abstract_only"},
        ),
        # Phenotype verbs are not rescue: "abolished" and "reversed" here report
        # the knockout phenotype, so the phenotype-only penalty stands.
        (
            "FOO1 in tumour metabolism",
            "FOO1 knockdown abolished tumour growth and reversed the glycolytic shift.",
            True,
            {"phenotype_only"},
            {"rescue_or_epistasis", "direct_assay"},
        ),
        # Passive loss-of-function reporting is not rescue either.
        (
            "FOO1 in tumour metabolism",
            "Tumour growth was prevented by FOO1 knockout, and the glycolytic shift "
            "was reversed by FOO1 silencing. FOO1 is re-expressed in metastases.",
            True,
            {"phenotype_only"},
            {"rescue_or_epistasis"},
        ),
        # Pharmacological epistasis still counts.
        (
            "FOO1 in kidney disease",
            "FOO1 overexpression aggravated the injury, an effect that was reversed "
            "by a PPARα agonist.",
            True,
            {"rescue_or_epistasis"},
            {"phenotype_only"},
        ),
        # A mechanistic phenotype rescue is not an indirect effect.
        (
            "FOO1 in tumour metabolism",
            "The knockout phenotype was rescued by wild-type FOO1.",
            True,
            {"rescue_or_epistasis"},
            {"indirect_effect", "phenotype_only"},
        ),
        # Abstract-only papers are flagged.
        ("FOO1 binds DNA", "", False, {"abstract_only"}, set()),
    ],
)
def test_score_paper_mechanism_rules(
    config: dict[str, Any],
    title: str,
    abstract: str,
    full_text: bool,
    expected: set[str],
    excluded: set[str],
) -> None:
    fired = {
        c["rule"]
        for c in gene_gap.score_paper(
            title,
            abstract,
            config["paper_scoring"],
            gene_in_title=False,
            matched_symbol="FOO1",
            full_text_available=full_text,
        )
    }
    assert expected <= fired
    assert not (excluded & fired)


def test_rank_caps_issues_and_one_per_paper(config: dict[str, Any]) -> None:
    limits = dict(config["limits"], max_issues=2, max_issues_per_paper=1)
    cands = [
        make_candidate(config, make_gene(accession="P1"), pmid="10"),
        make_candidate(config, make_gene(accession="P2"), pmid="10"),
        make_candidate(config, make_gene(accession="P3"), pmid="11"),
        make_candidate(config, make_gene(accession="P4"), pmid="12"),
    ]
    ranked = gene_gap.rank_candidates(cands, limits)
    eligible = [
        (c["paper"]["pmid"], c["gene"]["accession"])
        for c in ranked
        if c["issue_eligible"]
    ]
    assert eligible == [("10", "P1"), ("11", "P3")]
    assert [c["rank"] for c in ranked] == [1, 2, 3, 4]


def test_min_issue_score_blocks_weak_candidates(config: dict[str, Any]) -> None:
    weak = make_candidate(
        config,
        make_gene(
            protein_name="Kinase",
            annotation_counts=counts(total=100, experimental=60, experimental_mf=30),
            family=None,
            matched_in_title=False,
        ),
        title="Kinase signalling in cells",
    )
    assert weak["score"] < config["limits"]["min_issue_score"]
    assert not gene_gap.rank_candidates([weak], config["limits"])[0]["issue_eligible"]


def test_candidate_symbols_and_species(config: dict[str, Any]) -> None:
    stop = {s.lower() for s in config["symbol_stoplist"]}
    symbols = gene_gap.candidate_symbols(
        "CRISPR knockout of SLC25A51 in human cells reveals DNA damage",
        [("SLC25A51", "title"), ("MCART1", "abstract"), ("MCART1", "abstract")],
        stop,
        5,
    )
    assert symbols == [("SLC25A51", True), ("MCART1", False)]
    species = gene_gap.detect_species(
        "in human HEK293 cells and mice", config["species"]
    )
    assert [s["folder"] for s in species] == ["human", "mouse"]


def test_choose_entry_rejects_ambiguous() -> None:
    entries = [
        {"accession": f"P{i}", "symbol": "abc", "reviewed": True} for i in range(5)
    ]
    assert choose_entry(entries, "abc", 3) is None


def test_review_index_and_ledger(tmp_path: Path) -> None:
    review = tmp_path / "BACSU" / "yqcI" / "yqcI-ai-review.yaml"
    review.parent.mkdir(parents=True)
    review.write_text("id: P45944\ngene_symbol: yqcI\nreferences:\n- id: PMID:123\n")
    index = gene_gap.ReviewIndex.build(tmp_path)
    assert index.paths == {"P45944": str(review)}
    assert index.by_folder[("bacsu", "yqci")] == "P45944"
    assert index.cited["P45944"] == {"PMID:123"}
    assert gene_gap.ledger_references([{"body": "PMID:42980640\n<!-- marker -->"}]) == {
        "PMID:42980640"
    }


def test_packet_and_issue_bodies(tmp_path: Path, config: dict[str, Any]) -> None:
    update = make_candidate(
        config,
        make_gene(accession="P2", review_path="genes/BACSU/yqcI/yqcI-ai-review.yaml"),
        pmid="20",
    )
    ranked = gene_gap.rank_candidates(
        [make_candidate(config, make_gene()), update], config["limits"]
    )
    for cand in ranked:
        cand["issue_title"] = gene_gap.issue_title(cand)
        cand["issue_labels"] = gene_gap.issue_labels(cand)
    packet: dict[str, Any] = {
        "job": gene_gap.JOB,
        "generated_at": "2026-11-26T00:00:00+00:00",
        "date_from": "2026-10-27",
        "date_to": "2026-11-26",
        "include_preprints": False,
        "config_path": str(CONFIG_PATH),
        "queries": [
            {"profile": "dark_gene", "query": "q", "hit_count": 3, "fetched": 3}
        ],
        "paper_count": 3,
        "resolved_gene_count": 2,
        "suppressed": [{"reference_id": "PMID:9", "reason": "LEDGER"}],
        "candidates": ranked,
    }
    json_path, md_path = gene_gap.write_packet(packet, tmp_path)
    assert gene_gap.validate_files([json_path]) == []
    bodies = sorted((tmp_path / "issues" / packet["date_to"]).glob("*.md"))
    assert len(bodies) == 2
    first = next(b for b in bodies if b.name.endswith("-P45944.md")).read_text()
    assert first.rstrip().endswith(
        "<!-- litscan-gene-gap: PMID:42980640 UniProtKB:P45944 -->"
    )
    assert "| IBA | 2 |" in first
    assert "PTHR40045" in first and "0 with experimental GO" in first
    assert "just fetch-gene BACSU yqcI" in first
    second = next(b for b in bodies if b.name.endswith("-P2.md")).read_text()
    assert "Update the review of yqcI" in second
    assert "medium_effort" in md_path.read_text()
    # A re-run writes the same issue body files, not extra ones.
    gene_gap.write_packet(json.loads(json_path.read_text()), tmp_path)
    assert sorted((tmp_path / "issues" / packet["date_to"]).glob("*.md")) == bodies


def test_cli_validate_gene_gap() -> None:
    result = CliRunner().invoke(app, ["litscan", "validate-gene-gap", str(CONFIG_PATH)])
    assert result.exit_code == 0, result.output
    assert "0 problems" in result.output


@pytest.mark.integration
def test_cli_gene_gap_live(tmp_path: Path, config: dict[str, Any]) -> None:
    small = copy.deepcopy(config)
    small["limits"]["max_records_per_profile"] = 5
    small["query_profiles"] = small["query_profiles"][:1]
    cfg_path = tmp_path / "small.yaml"
    cfg_path.write_text(yaml.safe_dump(small))
    out = tmp_path / "out"
    result = CliRunner().invoke(
        app,
        [
            "litscan",
            "gene-gap",
            "--days",
            "30",
            "--config",
            str(cfg_path),
            "--genes-dir",
            str(tmp_path),
            "--output-dir",
            str(out),
        ],
    )
    assert result.exit_code == 0, result.output
    packets = list(out.glob("*-gene-gap.json"))
    assert len(packets) == 1
    assert gene_gap.validate_files(packets) == []


def test_reference_aliases_in_unlabelled_issue_title_and_closed_issue_body():
    assert gene_gap.ledger_references(
        [
            {"title": "Update with DOI:10.1101/Example and PPR1234"},
            {
                "state": "closed",
                "body": "See [paper](https://pubmed.ncbi.nlm.nih.gov/1234/).",
            },
        ]
    ) == {"DOI:10.1101/example", "PPR:PPR1234", "PMID:1234"}


def test_quickgo_counts_every_page_and_preserves_source_codes():
    from unittest.mock import Mock
    from ai_gene_review.litscan.gene_gap_sources import annotation_profile

    client = Mock()
    rows = [
        {
            "goEvidence": "IPI",
            "goId": "GO:0005515",
            "goAspect": "molecular_function",
            "reference": "PMID:1",
        },
        {
            "goEvidence": "IEA",
            "goId": "GO:0005576",
            "goAspect": "cellular_component",
            "reference": "GO_REF:0000002",
        },
    ]
    client.get.side_effect = [
        Mock(json=Mock(return_value={"results": [r], "numberOfHits": 2})) for r in rows
    ]
    profile = annotation_profile(client, "QTEST1")
    assert profile.counts["total"] == 2
    assert profile.counts["experimental_protein_binding"] == 1
    assert profile.evidence_codes == {"IEA": 1, "IPI": 1}
    assert profile.references == {"PMID:1", "GO_REF:0000002"}


def test_search_uses_cursor_and_honors_partial_final_page():
    from unittest.mock import Mock
    from ai_gene_review.litscan.europepmc import search

    client = Mock()

    def page(url, params):
        ids = ["1", "2"] if params["cursorMark"] == "*" else ["3", "4"]
        return Mock(
            json=lambda: {
                "hitCount": 4,
                "nextCursorMark": "cursor2",
                "resultList": {"result": [{"id": i, "source": "MED"} for i in ids]},
            }
        )

    client.get.side_effect = page
    hits, pubs = search("q", client=client, page_size=2, max_records=3)
    assert hits == 4
    assert [p.pmid for p in pubs] == ["1", "2", "3"]
    assert client.get.call_count == 2


def test_publisher_rejects_unapproved_ranks_and_skips_newly_filed_papers(
    tmp_path, monkeypatch
):
    import runpy
    import sys
    from unittest.mock import Mock

    script = REPO / ".github/scripts/file-gene-gap-issues.py"
    packet, log, ledger = (
        tmp_path / name for name in ("packet.json", "log.json", "ledger.json")
    )
    row = {
        "rank": 1,
        "issue_eligible": True,
        "paper": {"reference_id": "PMID:12", "doi": "", "europe_pmc_url": ""},
        "issue_title": "Review X",
        "issue_labels": ["litscan"],
        "issue_body_path": str(tmp_path / "01-X.md"),
    }
    packet.write_text(
        json.dumps({"candidates": [row, {**row, "rank": 2, "issue_eligible": False}]})
    )
    ledger.write_text(json.dumps([{"title": "Already filed PMID:12"}]))
    monkeypatch.setenv("GITHUB_REPOSITORY", "owner/repo")
    monkeypatch.setattr(sys, "argv", [str(script), str(packet), str(log), str(ledger)])
    gh = Mock()
    monkeypatch.setattr("subprocess.run", gh)

    def run_with(selection):
        log.write_text(
            json.dumps(
                [
                    {
                        "type": "result",
                        "subtype": "success",
                        "result": selection
                        if isinstance(selection, str)
                        else json.dumps(selection),
                    }
                ]
            )
        )
        runpy.run_path(str(script), run_name="__main__")

    with pytest.raises(ValueError, match="outside"):
        run_with([1, 2])
    run_with([1])
    gh.assert_not_called()
    # A labelled issue for a different accession also suppresses this paper.
    ledger.write_text(
        json.dumps([{"body": gene_gap.ledger_marker("PMID:12", "QOTHER")}])
    )
    run_with([1])
    gh.assert_not_called()
    ledger.write_text("[]")
    for reply in ("[[1]]", "[1] or [2]", "[true]", '{"ranks": [1]}'):
        with pytest.raises(ValueError):
            run_with(reply)
    body = Path(row["issue_body_path"])
    body.write_text("Contact @someone to follow up.")
    run_with([1])
    gh.assert_not_called()
    body.write_text("Review gene X using this paper.")
    run_with("Selected ranks:\n```json\n[1, 1]\n```")
    gh.assert_called_once()
    assert gh.call_args.args[0][-2:] == ["--body-file", str(body)]


@pytest.mark.parametrize(
    "abstract,expected",
    [
        ("FOO1 lacks catalytic activity.", True),
        ("The catalytically inactive FOO1 mutant served as a control.", False),
        ("We measured FOO1 abundance. BAR2 is a pseudokinase.", False),
        (
            "We tested catalytically inactive FOO1 (D5N vs. wild type) as a mutant control.",
            False,
        ),
    ],
)
def test_refutation_must_concern_candidate_not_mutant_or_neighbor(
    config, abstract, expected
):
    fired = gene_gap.score_paper(
        "A study of FOO1",
        abstract,
        config["paper_scoring"],
        gene_in_title=True,
        matched_symbol="FOO1",
        full_text_available=True,
    )
    assert ("refutation" in {r["rule"] for r in fired}) == expected


@pytest.mark.parametrize(
    "flags,expected",
    [
        ({"inEPMC": "Y", "isOpenAccess": "N"}, True),
        ({"inEPMC": "N", "isOpenAccess": "Y"}, True),
        ({"inEPMC": "N", "isOpenAccess": "N"}, False),
        ({}, False),
    ],
)
def test_full_text_availability_from_europe_pmc_record(
    flags: dict[str, str], expected: bool
) -> None:
    record = {"source": "MED", "id": "1", "pmid": "1", "title": "T", **flags}
    assert publication_from_record(record).full_text_available is expected


REVIEWED_ISSUES = Path("tests/input/litscan/gene_gap_reviewed_issues.yaml")


def test_reviewed_issues_rank_gap_closers_first(config: dict[str, Any]) -> None:
    """Regression on the curators' verdicts for the first six filed issues.

    The two papers that closed a gap (NPM3: direct binding, rescue and reporter
    assays under a partner's title; Mtdh: a gene with no experimental MF) must
    outrank the three that did not: TRIB2 (knockout phenotype, pseudokinase as
    background), Trib3 (rat gene covered by ISO transfers) and Pes1 (BP and CC
    already experimentally annotated).
    """
    records = yaml.safe_load(REVIEWED_ISSUES.read_text())
    scores = {
        r["gene"]["symbol"]: gene_gap.score_candidate(r["paper"], r["gene"], config)[
            "score"
        ]
        for r in records
    }
    closed = {r["gene"]["symbol"] for r in records if r["closed_gap"]}
    assert closed == {"NPM3", "Mtdh"}
    assert min(scores[s] for s in closed) > max(
        scores[s] for s in ("TRIB2", "Trib3", "Pes1")
    ), scores


def test_rescore_packet_keeps_previous_rank(config: dict[str, Any]) -> None:
    ranked = gene_gap.rank_and_title(
        [
            make_candidate(config, make_gene(accession="P1"), pmid="10"),
            make_candidate(config, make_gene(accession="P2"), pmid="11"),
        ],
        config["limits"],
    )
    packet = {"job": gene_gap.JOB, "date_to": "2026-11-26", "candidates": ranked}
    rescored = gene_gap.rescore_packet(packet, config)
    assert [c["previous_rank"] for c in rescored["candidates"]] == [1, 2]
    assert [c["score"] for c in rescored["candidates"]] == [c["score"] for c in ranked]


def test_paper_rule_order_is_checked(tmp_path: Path, config: dict[str, Any]) -> None:
    bad = copy.deepcopy(config)
    rules = bad["paper_scoring"]
    pheno = next(r for r in rules if r["id"] == "phenotype_only")
    rules.remove(pheno)
    rules.insert(0, pheno)
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(bad))
    problems = gene_gap.validate_files([path])
    assert any(
        "unless_rules direct_assay is not an earlier rule" in p for p in problems
    )


def test_cli_rescore_refuses_to_overwrite_and_old_packets(
    tmp_path: Path, config: dict[str, Any]
) -> None:
    ranked = gene_gap.rank_and_title(
        [make_candidate(config, make_gene())], config["limits"]
    )
    packet: dict[str, Any] = {
        "job": gene_gap.JOB,
        "generated_at": "2026-11-26T00:00:00+00:00",
        "date_from": "2026-10-28",
        "date_to": "2026-11-26",
        "include_preprints": False,
        "queries": [],
        "paper_count": 1,
        "resolved_gene_count": 1,
        "suppressed": [],
        "candidates": ranked,
    }
    src = tmp_path / "2026-11-26-gene-gap.json"
    src.write_text(json.dumps(packet))
    runner = CliRunner()
    same = runner.invoke(
        app, ["litscan", "rescore-gene-gap", str(src), "--output-dir", str(tmp_path)]
    )
    assert same.exit_code != 0 and "must differ" in same.output
    out = tmp_path / "rescore"
    ok = runner.invoke(
        app, ["litscan", "rescore-gene-gap", str(src), "--output-dir", str(out)]
    )
    assert ok.exit_code == 0, ok.output
    assert (out / "2026-11-26-gene-gap.json").exists()
    del packet["candidates"][0]["gene"]["annotation_counts"]["homology"]
    src.write_text(json.dumps(packet))
    old = runner.invoke(
        app, ["litscan", "rescore-gene-gap", str(src), "--output-dir", str(out)]
    )
    assert old.exit_code != 0 and "re-run the scan" in old.output
