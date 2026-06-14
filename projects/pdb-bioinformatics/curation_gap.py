"""Measure whether PDB structure papers are referenced by GO/MOD curation.

Question: to what extent are the primary publications behind deposited PDB
structures *overlooked* by normal GO annotation? We can approximate this by
checking, for each structure that has a linked primary publication (PMID), whether
that PMID is cited in the REFERENCE column of the gene's GOA file. If a structure
paper is never referenced by any GO annotation for that gene, the structural
evidence is a candidate for being overlooked by curation.

Important interpretation caveats (see CURATION_GAP.md):
  * "Not cited" does NOT mean the function is unannotated -- the same function may
    be captured from a different paper. It means the *structural* study specifically
    did not enter the evidence trail for that gene.
  * The RCSB primary-citation PMID is sometimes a methods/deposition paper rather
    than the functional paper.
  * Structures published after the most recent GOA annotation reflect curation lag,
    not an oversight; we separate those (GAP_LAG) from genes that were curated after
    the structure appeared (GAP_OPPORTUNITY).
  * Genes with no experimental annotations at all (only IEA/IBA electronic
    annotation) never cite primary literature; a gap there (GAP_NO_EXP_CURATION)
    reflects absence of manual curation, a distinct category.

Reusable parsing lives in the core module
``ai_gene_review.validation.goa_validator`` (``GOAValidator.parse_goa_file`` and
``referenced_pmids``); this script is the project-specific analysis on top of it.

Usage:
    uv run python projects/pdb-bioinformatics/curation_gap.py \
        --enriched projects/pdb-bioinformatics/data/pdb_enriched.tsv \
        --genes-dir genes \
        --out-tsv projects/pdb-bioinformatics/data/curation_gap.tsv \
        --out-md projects/pdb-bioinformatics/CURATION_GAP.md
"""

from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set

from ai_gene_review.validation.goa_validator import (
    EXPERIMENTAL_EVIDENCE_CODES,
    GOAValidator,
    referenced_pmids,
)


@dataclass
class StructurePaperRow:
    """One (gene, structure-paper) pair and its curation-citation status."""

    organism: str
    gene: str
    pmid: str
    year: str
    n_structures: int
    pdb_ids: str
    category: str
    cited_evidence_codes: str
    latest_goa_year: str
    latest_exp_goa_year: str
    in_publications_cache: bool
    in_ai_review: bool


def _load_structure_papers(
    enriched: Path,
) -> Dict[tuple, Dict[str, dict]]:
    """Group structure papers by (organism, gene) -> {pmid: {pdb_ids, year}}.

    Only entries that carry a primary-citation PMID are kept (structures with no
    linked publication cannot be assessed for citation by curation).
    """
    by_gene: Dict[tuple, Dict[str, dict]] = defaultdict(dict)
    with enriched.open() as f:
        for r in csv.DictReader(f, delimiter="\t"):
            pmid = (r.get("pmid") or "").strip()
            if not pmid:
                continue
            pmid = pmid if pmid.startswith("PMID:") else f"PMID:{pmid}"
            key = (r["organism"], r["gene"])
            slot = by_gene[key].setdefault(
                pmid, {"pdb_ids": [], "year": (r.get("year") or "").strip()}
            )
            slot["pdb_ids"].append(r["pdb_id"])
            if (r.get("year") or "").strip() and not slot["year"]:
                slot["year"] = r["year"].strip()
    return by_gene


def _latest_year(annotations) -> str:
    """Most recent annotation DATE (YYYYMMDD -> YYYY) across a set of annotations."""
    years = [a.date[:4] for a in annotations if a.date and a.date[:4].isdigit()]
    return max(years) if years else ""


def _classify(
    *,
    cited: bool,
    paper_year: str,
    latest_exp_year: str,
    has_experimental: bool,
) -> str:
    """Bucket a (gene, structure-paper) pair.

    The lag boundary uses the latest *experimental* annotation year -- i.e. when a
    curator last engaged with direct evidence -- not the overall latest GOA date,
    which is inflated by electronic (IEA/IBA) re-annotation pipeline refreshes.
    """
    if cited:
        return "CITED"
    if not has_experimental:
        return "GAP_NO_EXP_CURATION"
    if paper_year and latest_exp_year and paper_year > latest_exp_year:
        return "GAP_LAG"
    return "GAP_OPPORTUNITY"


def analyze(enriched: Path, genes_dir: Path) -> List[StructurePaperRow]:
    """Build the per-(gene, structure-paper) curation-citation table."""
    validator = GOAValidator()
    by_gene = _load_structure_papers(enriched)
    rows: List[StructurePaperRow] = []

    for (organism, gene), papers in sorted(by_gene.items()):
        gene_dir = genes_dir / organism / gene
        goa_file = gene_dir / f"{gene}-goa.tsv"
        review_file = gene_dir / f"{gene}-ai-review.yaml"
        if not goa_file.exists():
            # No GOA on disk -> cannot assess; record as such.
            for pmid, info in papers.items():
                rows.append(
                    StructurePaperRow(
                        organism, gene, pmid, info["year"], len(info["pdb_ids"]),
                        ";".join(info["pdb_ids"]), "NO_GOA_FILE", "", "", "",
                        False, False,
                    )
                )
            continue

        annotations = validator.parse_goa_file(goa_file)
        all_cited = referenced_pmids(annotations)
        exp_annotations = [
            a for a in annotations if a.evidence_code in EXPERIMENTAL_EVIDENCE_CODES
        ]
        has_experimental = bool(exp_annotations)
        latest = _latest_year(annotations)
        latest_exp = _latest_year(exp_annotations)
        review_text = review_file.read_text() if review_file.exists() else ""

        for pmid, info in sorted(papers.items()):
            cited = pmid in all_cited
            category = _classify(
                cited=cited,
                paper_year=info["year"],
                latest_exp_year=latest_exp,
                has_experimental=has_experimental,
            )
            bare = pmid.split(":", 1)[1]
            rows.append(
                StructurePaperRow(
                    organism=organism,
                    gene=gene,
                    pmid=pmid,
                    year=info["year"],
                    n_structures=len(info["pdb_ids"]),
                    pdb_ids=";".join(info["pdb_ids"]),
                    category=category,
                    cited_evidence_codes=",".join(sorted(all_cited.get(pmid, set()))),
                    latest_goa_year=latest,
                    latest_exp_goa_year=latest_exp,
                    in_publications_cache=(
                        Path("publications") / f"PMID_{bare}.md"
                    ).exists(),
                    in_ai_review=(bare in review_text),
                )
            )
    return rows


def write_tsv(rows: List[StructurePaperRow], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = list(StructurePaperRow.__dataclass_fields__.keys())
    with out.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(fields)
        for r in rows:
            w.writerow([getattr(r, k) for k in fields])


def summarize(rows: List[StructurePaperRow]) -> str:
    """Render a markdown summary of the curation-citation gap."""
    cats = Counter(r.category for r in rows)
    total = len(rows)
    genes = {(r.organism, r.gene) for r in rows}
    # Genes with >=1 structure paper but ZERO cited -> structurally "blind" curation
    by_gene_cats: Dict[tuple, Set[str]] = defaultdict(set)
    for r in rows:
        by_gene_cats[(r.organism, r.gene)].add(r.category)
    genes_no_struct_cited = sorted(
        g for g, cs in by_gene_cats.items() if "CITED" not in cs
    )

    def pct(n: int) -> str:
        return f"{100 * n / total:.0f}%" if total else "n/a"

    lines = [
        "# Are PDB structure papers overlooked by GO/MOD curation?",
        "",
        "Per (gene, structure-paper) status: is the structure's primary publication "
        "cited in the gene's GOA REFERENCE column?",
        "",
        f"- Structure papers assessed (gene x PMID pairs): **{total}** "
        f"across **{len(genes)}** genes",
        f"- **CITED** by GOA: **{cats['CITED']}** ({pct(cats['CITED'])})",
        f"- **GAP_OPPORTUNITY** (not cited; gene curated experimentally after the "
        f"structure's year): **{cats['GAP_OPPORTUNITY']}** "
        f"({pct(cats['GAP_OPPORTUNITY'])})",
        f"- **GAP_LAG** (not cited; structure newer than latest GOA annotation): "
        f"**{cats['GAP_LAG']}** ({pct(cats['GAP_LAG'])})",
        f"- **GAP_NO_EXP_CURATION** (not cited; gene has no experimental GO "
        f"annotations at all): **{cats['GAP_NO_EXP_CURATION']}** "
        f"({pct(cats['GAP_NO_EXP_CURATION'])})",
        f"- NO_GOA_FILE (could not assess): **{cats['NO_GOA_FILE']}**",
        "",
        f"Genes where **no** structure paper is cited by GOA: "
        f"**{len(genes_no_struct_cited)}** / {len(genes)}.",
        "",
        "## Interpretation",
        "",
        "`GAP_OPPORTUNITY` is the headline signal: the structure's paper existed "
        "while the gene was being experimentally curated, yet no GO annotation "
        "references it. These are the strongest candidates for structural evidence "
        "that curation overlooked. `GAP_LAG` is excusable curation latency; "
        "`GAP_NO_EXP_CURATION` reflects genes that received only electronic "
        "annotation (a different problem). Caveat: 'not cited' means the structural "
        "study is absent from the evidence trail, not necessarily that the function "
        "is unannotated.",
        "",
        "## Top GAP_OPPORTUNITY structure papers (by number of deposited structures)",
        "",
        "Genes with many deposited structures sharing an uncited primary publication, "
        "despite later experimental GO curation -- the best targets to fold structural "
        "evidence into review.",
        "",
        "| gene | organism | structure paper | paper yr | # structures | latest exp. curation |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    opp = sorted(
        (r for r in rows if r.category == "GAP_OPPORTUNITY"),
        key=lambda r: (-r.n_structures, r.gene),
    )
    for r in opp[:15]:
        lines.append(
            f"| {r.gene} | {r.organism} | {r.pmid} | {r.year} | "
            f"{r.n_structures} | {r.latest_exp_goa_year} |"
        )
    return "\n".join(lines) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--enriched",
        type=Path,
        default=Path("projects/pdb-bioinformatics/data/pdb_enriched.tsv"),
    )
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument(
        "--out-tsv",
        type=Path,
        default=Path("projects/pdb-bioinformatics/data/curation_gap.tsv"),
    )
    ap.add_argument(
        "--out-md",
        type=Path,
        default=Path("projects/pdb-bioinformatics/CURATION_GAP.md"),
    )
    args = ap.parse_args()

    rows = analyze(args.enriched, args.genes_dir)
    write_tsv(rows, args.out_tsv)
    summary = summarize(rows)
    args.out_md.write_text(summary)
    print(summary)
    print(f"Wrote {len(rows)} rows -> {args.out_tsv}")


if __name__ == "__main__":
    main()
