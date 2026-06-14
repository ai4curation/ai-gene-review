"""Select the genuinely-dark test set for hypothesis H1.

H1: structures/structure-papers fill annotation gaps that traditional (non-structure)
publications would not. The fair test set is NOT famous, heavily-studied genes (whose
text already suffices) but genuinely under-characterized proteins where:

  * the gene is GAP_OPPORTUNITY (has an uncited structure paper predating its last
    experimental curation),
  * it has ZERO experimental molecular-function annotations (exp_mf == 0), and
  * its literature is shallow (few distinct PMIDs cited in GOA), so there is little
    non-structure text that could fill the gap instead, and
  * the deposited structure actually carries a bound cofactor/metal or is a complex,
    i.e. there is structural evidence capable of pinning an MF/CC term.

The ranking favors the most under-characterized genes with the most informative
structures -- the cleanest cases to ask "could the non-structure pubs have filled
this?".

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
    gap = list(csv.DictReader(gap_tsv.open(), delimiter="\t"))
    gene_info: Dict[Tuple[str, str], dict] = {
        (r["organism"], r["gene"]): r
        for r in csv.DictReader(gene_enriched.open(), delimiter="\t")
    }
    enr_by_pdb = {r["pdb_id"]: r for r in csv.DictReader(enriched.open(), delimiter="\t")}

    # Group GAP_OPPORTUNITY papers by gene.
    by_gene: Dict[Tuple[str, str], List[dict]] = {}
    for r in gap:
        if r["category"] != "GAP_OPPORTUNITY":
            continue
        by_gene.setdefault((r["organism"], r["gene"]), []).append(r)

    rows: List[H1Row] = []
    for (organism, gene), papers in by_gene.items():
        gi = gene_info.get((organism, gene), {})
        exp_mf = gi.get("exp_mf", "")
        # Restrict to the genuinely dark set: no experimental MF annotation.
        if exp_mf != "0":
            continue

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
