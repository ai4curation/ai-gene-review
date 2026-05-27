"""Tests for gene deep-research provider coverage tooling."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "deep_research_coverage.py"
SPEC = importlib.util.spec_from_file_location("deep_research_coverage", MODULE_PATH)
assert SPEC is not None and SPEC.loader is not None
deep_research_coverage = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = deep_research_coverage
SPEC.loader.exec_module(deep_research_coverage)


def write_review(genes_root: Path, organism: str, gene: str, *, uniprot_id: str = "P1") -> Path:
    gene_dir = genes_root / organism / gene
    gene_dir.mkdir(parents=True)
    review_path = gene_dir / f"{gene}-ai-review.yaml"
    review_path.write_text(
        f"id: {uniprot_id}\n"
        f"gene_symbol: {gene}\n"
        "taxon:\n"
        "  id: NCBITaxon:9606\n"
        "  label: Homo sapiens\n",
        encoding="utf-8",
    )
    return review_path


def write_research(genes_root: Path, organism: str, gene: str, provider: str) -> Path:
    path = genes_root / organism / gene / f"{gene}-deep-research-{provider}.md"
    path.write_text(
        "---\n"
        f"provider: {provider}\n"
        "start_time: '2026-05-19T00:00:00'\n"
        "end_time: '2026-05-19T00:10:00'\n"
        "---\n\n"
        "# Report\n",
        encoding="utf-8",
    )
    return path


def test_parse_research_filename_accepts_provider_files_and_ignores_non_provider_files():
    parse = deep_research_coverage.parse_research_filename

    assert parse(Path("TP53-deep-research-openai.md")) == ("TP53", "openai")
    assert parse(Path("TP53-deep-research-perplexity-lite.md")) == (
        "TP53",
        "perplexity-lite",
    )
    assert parse(Path("TP53-deep-research-openscientist.md")) == (
        "TP53",
        "openscientist",
    )
    assert parse(Path("TP53-deep-research-bioreason-sft.md")) == (
        "TP53",
        "bioreason-sft",
    )

    assert parse(Path("TP53-deep-research.md")) is None
    assert parse(Path("TP53-deep-research-manual.md")) is None
    assert parse(Path("TP53-deep-research-openai-citations.md")) is None
    assert parse(Path("TP53-deep-research-openai.md.citations.md")) is None
    assert parse(Path("TP53-citations.md")) is None


def test_missing_provider_filtering_uses_gene_reviews_and_provider_files(tmp_path):
    genes_root = tmp_path / "genes"
    write_review(genes_root, "human", "TP53")
    write_review(genes_root, "human", "BRCA1")
    write_review(genes_root, "ECOLI", "SecB")
    write_research(genes_root, "human", "TP53", "openai")
    write_research(genes_root, "human", "BRCA1", "falcon")
    (genes_root / "human" / "TP53" / "TP53-deep-research-openai-citations.md").write_text(
        "citations only\n", encoding="utf-8"
    )

    rows = deep_research_coverage.build_coverage(genes_root)
    missing_openai = deep_research_coverage.filter_rows(
        rows, missing_provider="openai"
    )

    assert {row.key for row in rows} == {"human/TP53", "human/BRCA1", "ECOLI/SecB"}
    assert {row.key for row in missing_openai} == {"human/BRCA1", "ECOLI/SecB"}
    tp53 = next(row for row in rows if row.key == "human/TP53")
    assert tp53.providers == ("openai",)
    assert tp53.provider_count == 1


def test_dry_run_backfill_attempts_generate_just_commands(tmp_path):
    genes_root = tmp_path / "genes"
    write_review(genes_root, "human", "CFAP300")
    write_review(genes_root, "human", "TP53")
    write_research(genes_root, "human", "TP53", "openscientist")
    rows = deep_research_coverage.build_coverage(genes_root)

    attempts = deep_research_coverage.build_backfill_attempts(
        rows,
        provider="openscientist",
        genes_root=genes_root,
        extra_args=["--fallback", "perplexity-lite"],
    )

    assert len(attempts) == 1
    attempt = attempts[0]
    assert attempt.organism == "human"
    assert attempt.gene == "CFAP300"
    assert attempt.status == "DRY_RUN"
    assert (
        attempt.command
        == "just deep-research-openscientist human CFAP300 --fallback perplexity-lite"
    )
    assert attempt.output_file.endswith(
        "genes/human/CFAP300/CFAP300-deep-research-openscientist.md"
    )
