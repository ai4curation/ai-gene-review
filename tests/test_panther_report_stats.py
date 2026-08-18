"""Tests for the scope-table derivation behind `just panther-report-stats`.

The command exists because the report's table went stale four times. It then
acquired the most intricate logic in the CLI -- a PAINT-index join, an evidence
filter, a per-annotation aggregation, and a prefix-stripping trap that made the
first implementation print 52/45 instead of 100/76 -- with no test at all. Every
case below is one the command got wrong at some point, or one where getting it
wrong would change a published figure rather than crash.
"""

from pathlib import Path

import pytest
import yaml
from typer.testing import CliRunner

from ai_gene_review.cli import app

runner = CliRunner()


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repo skeleton the command can be pointed at."""
    (tmp_path / "modules").mkdir()
    (tmp_path / "interpro" / "panther").mkdir(parents=True)
    (tmp_path / "interpro" / "panther" / "panther-members.tsv").write_text(
        "uniprot_accession\tpanther_family_sf\nP1\tPTHR1:SF1\n"
    )
    (tmp_path / "interpro" / "panther" / "panther.obo").write_text(
        "format-version: 1.2\nontology: panther\n"
    )
    return tmp_path


def write_slice(repo: Path, family: str, rows: list[tuple[str, str, str, str]]) -> None:
    """Write a PAINT slice; each row is (node, go_id, evidence, seeds)."""
    directory = repo / "interpro" / "panther" / family
    directory.mkdir(parents=True, exist_ok=True)
    lines = ["family\tnode\tgo_id\taspect\tevidence\tnegated\tseeds\ttaxon\tdate"]
    for node, go_id, evidence, seeds in rows:
        lines.append(f"{family}\t{node}\t{go_id}\tF\t{evidence}\tfalse\t{seeds}\t\t")
    (directory / f"{family}-paint.tsv").write_text("\n".join(lines) + "\n")


def write_module(repo: Path, name: str, nodes: list[str]) -> None:
    document = {
        "module": {
            "id": "m",
            "parts": [
                {
                    "node": {
                        "annotons": [
                            {
                                "participant": {
                                    "family": {
                                        "ancestral_nodes": [
                                            {"term": {"id": n, "label": n.split(":")[1]}}
                                            for n in nodes
                                        ]
                                    }
                                }
                            }
                        ]
                    }
                }
            ],
        }
    }
    (repo / "modules" / name).write_text(yaml.safe_dump(document))


def run(repo: Path) -> str:
    result = runner.invoke(app, ["panther-report-stats", "--output-dir", str(repo)])
    assert result.exit_code == 0, result.output
    return result.output


def test_counts_citations_and_distinct_nodes_separately(repo):
    """One node cited twice is 2 citations, 1 node -- the row rename's whole point."""
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])
    write_module(repo, "b.yaml", ["PANTHER:PTN1"])

    assert "| PAINT node citations | 2 (of 1 distinct nodes) |" in run(repo)


def test_seed_count_is_not_inflated_by_prefix_stripping(repo):
    """The bug that printed 52/45: unioning bare accessions with prefixed tokens.

    The seed set must straddle the threshold for this to bite. Two UniProt seeds
    count as 2 (thin); double-counted they become 4 (not thin), which is exactly
    how the original bug hid thin nodes. A 4-seed fixture would pass either way.
    """
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct" in run(repo)


def test_non_uniprot_seeds_are_counted(repo):
    """Seeds are counted as written, so a PANTHER-node seed is still a seed.

    Counting only `UniProtKB:` tokens is the error that reported 82 seeds as
    180; the guard against it must not swing the other way and discard them.
    """
    write_slice(
        repo,
        "PTHR1",
        [("PTN1", "GO:1", "IBD", "PANTHER:PTN9|PANTHER:PTN8|UniProtKB:A|UniProtKB:B")],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 0 / 1 distinct" in run(repo)


def test_thinness_is_per_annotation_not_pooled_across_rows(repo):
    """PTN000329346's shape: two 3-seed rows. Pooled reads 5-6; per-term reads 3.

    Both annotations are thin. Pooling would credit each with seeds that were
    never used together to infer it.
    """
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "UniProtKB:A|UniProtKB:B|UniProtKB:Q"),
            ("PTN1", "GO:2", "IBD", "UniProtKB:C|UniProtKB:D|UniProtKB:Q"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 2 / 2 distinct" in run(repo)


def test_a_well_supported_sibling_does_not_rescue_a_thin_annotation(repo):
    """The quantifier the row label got wrong.

    Requiring EVERY annotation to be thin would report 0 here, even though the
    2-seed term is exactly the thinly-propagated claim the figure is about.
    """
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "|".join(f"UniProtKB:S{i}" for i in range(40))),
            ("PTN1", "GO:2", "IBD", "UniProtKB:A|UniProtKB:B"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 2 distinct" in run(repo)


def test_distinct_and_citation_weighted_aggregations_differ(repo):
    """A node cited twice contributes its annotation twice to the weighted count."""
    write_slice(repo, "PTHR1", [("PTN1", "GO:1", "IBD", "UniProtKB:A")])
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])
    write_module(repo, "b.yaml", ["PANTHER:PTN1"])

    assert (
        "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct (node, term) "
        "= 2 / 2 citation-weighted |" in run(repo)
    )


def test_non_ibd_rows_are_excluded(repo):
    """The evidence filter is part of the definition, not an implementation detail."""
    write_slice(
        repo,
        "PTHR1",
        [
            ("PTN1", "GO:1", "IBD", "UniProtKB:A"),
            ("PTN1", "GO:2", "IRD", "UniProtKB:B"),
        ],
    )
    write_module(repo, "a.yaml", ["PANTHER:PTN1"])

    assert "| PAINT annotations resting on <=3 seeds | 1 / 1 distinct" in run(repo)
