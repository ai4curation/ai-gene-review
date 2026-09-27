"""Tests for the homology-propagation export, browser payload and statistics."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from ai_gene_review.export.propagation_export import collect_propagation_data
from ai_gene_review.tools.build_propagation_browser import (
    build_propagation_browser,
    encode_propagation_data,
)
from ai_gene_review.tools.propagation_stats import render

HEADER = ("GENE PRODUCT DB\tGENE PRODUCT ID\tSYMBOL\tQUALIFIER\tGO TERM\tGO NAME\tGO ASPECT\t"
          "ECO ID\tGO EVIDENCE CODE\tREFERENCE\tWITH/FROM\tTAXON ID\tTAXON NAME\tASSIGNED BY\t"
          "GENE NAME\tDATE")


def _goa(*rows: tuple[str, ...]) -> str:
    lines = [HEADER]
    for qualifier, term, name, aspect, ev, ref, with_from in rows:
        lines.append("\t".join(["UniProtKB", "P0DP28", "Calm3", qualifier, term, name, aspect,
                                "ECO:0000266", ev, ref, with_from, "10090", "Mus musculus",
                                "MGI", "Calmodulin-3", "20250101"]))
    return "\n".join(lines) + "\n"


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repository with one mouse gene, its review, and a donor cache."""
    gene = tmp_path / "genes" / "mouse" / "Calm3"
    gene.mkdir(parents=True)
    (gene / "Calm3-goa.tsv").write_text(_goa(
        # ISO from the human ortholog; the target also has IBA to a child term.
        ("enables", "GO:0005509", "calcium ion binding", "molecular_function",
         "ISO", "GO_REF:0000119", "UniProtKB:P0DP25"),
        # ISO from a rat paralog only; donor no longer carries the term.
        ("located_in", "GO:0000785", "chromatin", "cellular_component",
         "ISO", "GO_REF:0000096", "RGD:2257"),
        ("enables", "GO:0099999", "child of calcium ion binding", "molecular_function",
         "IBA", "GO_REF:0000033", "PANTHER:PTN000549682|UniProtKB:P62157|FB:FBgn0000253"),
        # Not homology propagation: must be excluded.
        ("enables", "GO:0005509", "calcium ion binding", "molecular_function",
         "IEA", "GO_REF:0000002", "InterPro:IPR002048"),
    ))
    (gene / "Calm3-ai-review.yaml").write_text(
        "id: P0DP28\ngene_symbol: Calm3\nexisting_annotations:\n"
        "- term: {id: GO:0000785, label: chromatin}\n"
        "  evidence_type: ISO\n  original_reference_id: GO_REF:0000096\n"
        "  review:\n    summary: paralog donor\n    action: KEEP_AS_NON_CORE\n"
        "    propagation_review:\n      root_cause: NO_FAILURE_NON_CORE\n"
        "      failure_modes: [WRONG_ORTHOLOG_OR_PARALOG]\n"
    )
    (gene / "Calm3-ai-review.html").write_text("<html></html>")
    data = tmp_path / "projects" / "HOMOLOGY_PROPAGATION" / "data"
    data.mkdir(parents=True)
    (data / "donor-entities.tsv").write_text(
        "xref\taccession\tsymbol\ttaxon_id\torganism\treviewed\n"
        "RGD:2257\tP0DP29\tCalm1\t10116\tRattus norvegicus (Rat)\ttrue\n"
        "UniProtKB:P0DP25\tP0DP25\tCALM3\t9606\tHomo sapiens (Human)\ttrue\n")
    (data / "donor-annotations.tsv").write_text(
        "accession\tterm_id\tevidence_codes\tassigned_by\treferences\n"
        "P0DP25\tGO:0005509\tIDA,IEA\tUniProt\tPMID:1\n")
    (data / "donor-annotations-checked.tsv").write_text(
        "accession\tterm_id\nP0DP25\tGO:0005509\nP0DP29\tGO:0000785\n")
    (data / "term-ancestors.tsv").write_text("term_id\tancestors\nGO:0099999\tGO:0005509\n")
    return tmp_path


def _by_term(rows: list[dict]) -> dict[tuple[str, str], dict]:
    return {(r["term_id"], r["evidence"]): r for r in rows}


def test_collects_only_homology_rows(repo: Path) -> None:
    rows = collect_propagation_data(repo)["rows"]
    assert sorted((r["term_id"], r["evidence"]) for r in rows) == [
        ("GO:0000785", "ISO"), ("GO:0005509", "ISO"), ("GO:0099999", "IBA")]


def test_ortholog_donor_is_resolved_and_supported(repo: Path) -> None:
    row = _by_term(collect_propagation_data(repo)["rows"])[("GO:0005509", "ISO")]
    assert row["method"] == "Alliance human→mouse ISO"
    assert row["donors"][0]["symbol"] == "CALM3"
    assert row["donor_species"] == ["Homo sapiens"]
    assert row["donor_support"] == "EXPERIMENTAL"
    assert row["symbol_match"] == "SAME_SYMBOL"
    # The IBA to a child term already entails this ISO row.
    assert row["iba_on_target"] == "MORE_SPECIFIC"
    assert row["action"] == "NOT_IN_REVIEW"


def test_paralog_donor_and_review_join(repo: Path) -> None:
    row = _by_term(collect_propagation_data(repo)["rows"])[("GO:0000785", "ISO")]
    assert row["symbol_match"] == "DIFFERENT_SYMBOL"
    assert row["donor_support"] == "ABSENT"
    assert row["iba_on_target"] == "NONE"
    assert row["action"] == "KEEP_AS_NON_CORE"
    assert row["root_cause"] == "NO_FAILURE_NON_CORE"
    assert row["failure_modes"] == ["WRONG_ORTHOLOG_OR_PARALOG"]
    assert row["review_link"] == "genes/mouse/Calm3/Calm3-ai-review.html"


def test_iba_row_keeps_node_and_seed_species(repo: Path) -> None:
    row = _by_term(collect_propagation_data(repo)["rows"])[("GO:0099999", "IBA")]
    assert row["nodes"] == ["PANTHER:PTN000549682"]
    assert row["donor_count"] == 2
    assert "donor_species" not in row
    assert "donor_support" not in row


def test_payload_round_trips(repo: Path) -> None:
    rows = collect_propagation_data(repo)["rows"]
    encoded = encode_propagation_data(rows, {"built": "x"})
    payload = json.loads(encoded.removeprefix("window.propagationPayload=").rstrip(";\n"))
    strings, donors = payload["strings"], payload["donors"]
    decoded = []
    for packed in payload["rows"]:
        row = {}
        for field, value in zip(payload["fields"], packed):
            if value is None:
                continue
            if field == "donors":
                row[field] = [{f: strings[v] for f, v in zip(payload["donor_fields"], donors[i])
                               if v is not None} for i in value]
            elif isinstance(value, list):
                row[field] = [strings[v] for v in value]
            elif field == "donor_count":
                row[field] = value
            else:
                row[field] = strings[value]
        decoded.append(row)

    def drop_empty(row: dict) -> dict:
        return {k: ([{f: x for f, x in d.items() if x} for d in v] if k == "donors" else v)
                for k, v in row.items()}

    assert decoded == [drop_empty(r) for r in rows]


def test_build_writes_browser_and_manifest(repo: Path) -> None:
    out = repo / "app" / "propagation"
    result = build_propagation_browser(repo, out)
    assert result["rows"] == 3
    assert (out / "index.html").read_text().count("propagationPayload") >= 1
    assert json.loads((out / "source-files.json").read_text()) == [
        "genes/mouse/Calm3/Calm3-ai-review.html"]


def test_stats_render_sections(repo: Path) -> None:
    text = render(collect_propagation_data(repo)["rows"], {"generated": "2026-01-01"})
    assert "## What does ISO add on top of IBA?" in text
    assert "Homo sapiens → Mus musculus" in text
    assert "Rattus norvegicus → Mus musculus" in text


def test_stats_count_annotations_not_donor_lines(repo: Path) -> None:
    """Donor lines that join one review entry are one MIXED annotation.

    The second line differs only in a non-negating qualifier, which
    ``load_reviews`` ignores, so it must not become a separate unit.
    """
    from ai_gene_review.tools.propagation_stats import annotation_units

    goa = repo / "genes" / "mouse" / "Calm3" / "Calm3-goa.tsv"
    goa.write_text(_goa(
        ("located_in", "GO:0000785", "chromatin", "cellular_component",
         "ISO", "GO_REF:0000096", "RGD:2257"),
        ("is_active_in", "GO:0000785", "chromatin", "cellular_component",
         "ISO", "GO_REF:0000096", "RGD:2259"),
    ))
    data = repo / "projects" / "HOMOLOGY_PROPAGATION" / "data"
    with (data / "donor-entities.tsv").open("a") as handle:
        handle.write("RGD:2259\tP0DP31\tCalm3\t10116\tRattus norvegicus (Rat)\ttrue\n")
    rows = collect_propagation_data(repo)["rows"]
    assert len(rows) == 2
    units = annotation_units(rows)
    assert len(units) == 1
    assert units[0]["symbol_match"] == "MIXED"
    assert units[0]["donor_lines"] == 2
    # Both lines join one review entry, so both donors belong to the unit.
    assert [d["id"] for d in units[0]["donors"]] == ["RGD:2257", "RGD:2259"]
    assert units[0]["donor_species"] == ["Rattus norvegicus"]
    text = render(rows, {"generated": "2026-01-01"})
    assert "2 GOA lines → 1 annotations" in text
