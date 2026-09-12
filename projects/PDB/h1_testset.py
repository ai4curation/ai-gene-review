"""Select the genuinely-dark test set for hypothesis H1.

H1: structures/structure-papers fill annotation gaps that traditional (non-structure)
publications would not. The fair test set is NOT famous, heavily-studied genes (whose
text already suffices).

METHODOLOGICAL NOTE (important): an earlier version of this selector used the
GAP_OPPORTUNITY bucket filtered to exp_mf==0. That was subtly wrong: GAP_OPPORTUNITY
is, by construction, the set of genes that HAVE experimental curation (it is precisely
what distinguishes it from GAP_NO_EXP_CURATION). So every GAP_OPPORTUNITY gene has some
experimental annotation, and a structure can only ever corroborate -- which is exactly
what we observed (SPR, TOMM5, HSPB3, CFAP61 all came back STRUCTURE_CORROBORATES).

The correct H1 frontier is GAP_NO_EXP_CURATION: genes with an uncited structure paper
AND NO experimental GO annotation of any aspect. For these the structure is the only
candidate route to an experimental-grade annotation, so they are the genes where a
structure could plausibly fill a gap that the (absent) experimental literature did not.
We keep those whose structures carry a bound cofactor/metal or are a complex -- i.e.
there is diagnostic structural evidence capable of pinning an MF/CC term.

Reuses ai_gene_review.validation.goa_validator (parse_goa_file, referenced_pmids,
EXPERIMENTAL_EVIDENCE_CODES). Project-specific glue lives here.

Usage:
    uv run python projects/PDB/h1_testset.py
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Dict, List, Tuple

from ai_gene_review.validation.goa_validator import (
    EXPERIMENTAL_EVIDENCE_CODES,
    GOAValidator,
    referenced_pmids,
)


@dataclass
class H1Row:
    rank: int
    score: float
    organism: str
    gene: str
    exp_mf: str
    distinct_goa_pmids: int
    distinct_exp_pmids: int
    n_uncited_structure_papers: int
    structure_has_cofactor: bool
    structure_is_complex: bool
    cofactors: str
    best_paper: str
    best_paper_year: str


def _truthy(v: str) -> bool:
    return str(v).strip().lower() in {"true", "1", "yes"}


def build(gap_tsv: Path, gene_enriched: Path, enriched: Path, genes_dir: Path) -> List[H1Row]:
    validator = GOAValidator()
    with gap_tsv.open() as fh:
        gap = list(csv.DictReader(fh, delimiter="\t"))
    with gene_enriched.open() as fh:
        gene_info: Dict[Tuple[str, str], dict] = {
            (r["organism"], r["gene"]): r for r in csv.DictReader(fh, delimiter="\t")
        }
    with enriched.open() as fh:
        enr_by_pdb = {r["pdb_id"]: r for r in csv.DictReader(fh, delimiter="\t")}

    # Group GAP_NO_EXP_CURATION papers by gene -- the correct H1 frontier
    # (uncited structure paper AND no experimental annotation of any aspect).
    by_gene: Dict[Tuple[str, str], List[dict]] = {}
    for r in gap:
        if r["category"] != "GAP_NO_EXP_CURATION":
            continue
        by_gene.setdefault((r["organism"], r["gene"]), []).append(r)

    rows: List[H1Row] = []
    for (organism, gene), papers in by_gene.items():
        gi = gene_info.get((organism, gene), {})
        # Confirm no experimental annotation of any aspect.
        if gi.get("exp_total", "") not in ("0", ""):
            continue
        exp_mf = gi.get("exp_mf", "")

        goa_file = genes_dir / organism / gene / f"{gene}-goa.tsv"
        if not goa_file.exists():
            continue
        anns = validator.parse_goa_file(goa_file)
        all_pmids = referenced_pmids(anns)
        exp_pmids = referenced_pmids(anns, evidence_codes=EXPERIMENTAL_EVIDENCE_CODES)

        # Structure richness over all this gene's uncited structures.
        pdb_ids = [p for r in papers for p in r["pdb_ids"].split(";") if p]
        structs = [enr_by_pdb[p] for p in pdb_ids if p in enr_by_pdb]
        has_cof = any(_truthy(s.get("has_cofactor", "")) for s in structs)
        is_cplx = any(_truthy(s.get("is_complex", "")) for s in structs)
        if not (has_cof or is_cplx):
            continue  # nothing structural to pin an MF/CC term on

        best = max(papers, key=lambda r: int(r["n_structures"]))
        n_distinct = len(all_pmids)
        # Score: shallow literature (fewer pubs => more likely structure-unique) and
        # informative structures rank highest. 8/(1+distinct_pmids) rewards scarcity.
        score = (
            8.0 / (1 + n_distinct)
            + (2.0 if has_cof else 0.0)
            + (1.0 if is_cplx else 0.0)
            + min(len(papers), 4) * 0.25
        )
        rows.append(
            H1Row(
                rank=0,
                score=round(score, 2),
                organism=organism,
                gene=gene,
                exp_mf=exp_mf,
                distinct_goa_pmids=n_distinct,
                distinct_exp_pmids=len(exp_pmids),
                n_uncited_structure_papers=len(papers),
                structure_has_cofactor=has_cof,
                structure_is_complex=is_cplx,
                cofactors=gi.get("cofactors", ""),
                best_paper=best["pmid"],
                best_paper_year=best["year"],
            )
        )

    rows.sort(key=lambda h: (-h.score, h.distinct_goa_pmids, h.gene))
    for i, h in enumerate(rows, 1):
        h.rank = i
    return rows


def main() -> None:
    base = Path("projects/PDB")
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gap-tsv", type=Path, default=base / "data/curation_gap.tsv")
    ap.add_argument("--gene-enriched", type=Path, default=base / "data/pdb_gene_enriched.tsv")
    ap.add_argument("--enriched", type=Path, default=base / "data/pdb_enriched.tsv")
    ap.add_argument("--genes-dir", type=Path, default=Path("genes"))
    ap.add_argument("--out-tsv", type=Path, default=base / "data/h1_testset.tsv")
    args = ap.parse_args()

    rows = build(args.gap_tsv, args.gene_enriched, args.enriched, args.genes_dir)
    cols = [f.name for f in fields(H1Row)]
    with args.out_tsv.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(cols)
        for r in rows:
            w.writerow([getattr(r, c) for c in cols])

    print(f"Genuinely-dark H1 test set: {len(rows)} genes (exp_mf==0, cofactor/complex structure)\n")
    print(f"{'#':>2} {'gene':10s}{'org':8s}{'score':6s}{'GOA_pmids':10s}{'exp_pmids':10s}"
          f"{'#str_papers':12s}{'cof':4s}{'cplx':5s}{'paper':14s}{'cofactors'}")
    for r in rows[:25]:
        print(f"{r.rank:>2} {r.gene:10s}{r.organism:8s}{r.score:<6}{r.distinct_goa_pmids:<10}"
              f"{r.distinct_exp_pmids:<10}{r.n_uncited_structure_papers:<12}"
              f"{'Y' if r.structure_has_cofactor else '-':4s}"
              f"{'Y' if r.structure_is_complex else '-':5s}{r.best_paper:14s}{r.cofactors[:24]}")
    print(f"\nWrote {len(rows)} rows -> {args.out_tsv}")


if __name__ == "__main__":
    main()
