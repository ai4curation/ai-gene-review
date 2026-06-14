"""Rank GAP_OPPORTUNITY structure papers into a prioritized review worklist.

Takes the curation-citation gap (``curation_gap.py`` output) and keeps only
GAP_OPPORTUNITY rows -- structure papers that predate the gene's last experimental
GO curation yet are never cited by GOA. Each is scored by combining:

  * the existing per-gene ``priority_score`` (encodes dark-MF / eukaryote /
    contested-catalytic signals from ``pdb_gene_enriched.tsv``), plus
  * paper-level functional richness of the deposited structures (bound cofactor,
    bound ligand, multi-chain complex) and the number of structures.

The result is an actionable list of the structure papers most worth folding into
gene reviews next. This is project-specific glue; the reusable GOA parsing lives in
``ai_gene_review.validation.goa_validator``.

Usage:
    uv run python projects/PDB/gap_worklist.py
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass, fields
from pathlib import Path
from typing import Dict, List, Tuple

# Paper-level functional-evidence bonuses (added to the gene priority_score).
COFACTOR_BONUS = 3.0  # bound cofactor most directly pins a molecular function
COMPLEX_BONUS = 1.5  # multi-chain assembly informs complex membership / CC
LIGAND_BONUS = 1.5  # any bound meaningful ligand = functional context
PER_STRUCTURE_WEIGHT = 0.5  # robustness from independent depositions
MAX_STRUCTURE_BONUS = 3.0


@dataclass
class WorklistRow:
    rank: int
    worklist_score: float
    organism: str
    gene: str
    pmid: str
    paper_year: str
    n_structures: int
    gene_priority_score: float
    candidate_reason: str
    exp_mf: str
    paper_has_cofactor: bool
    paper_has_complex: bool
    cofactors: str
    ligands: str
    pdb_ids: str
    already_in_review: bool


def _load_tsv(path: Path) -> List[dict]:
    with path.open() as f:
        return list(csv.DictReader(f, delimiter="\t"))


def _truthy(val: str) -> bool:
    return str(val).strip().lower() in {"true", "1", "yes"}


def build(
    gap_tsv: Path, gene_enriched: Path, enriched: Path
) -> List[WorklistRow]:
    gap = _load_tsv(gap_tsv)
    gene_info: Dict[Tuple[str, str], dict] = {
        (r["organism"], r["gene"]): r for r in _load_tsv(gene_enriched)
    }
    enr_by_pdb: Dict[str, dict] = {r["pdb_id"]: r for r in _load_tsv(enriched)}

    rows: List[WorklistRow] = []
    for r in gap:
        if r["category"] != "GAP_OPPORTUNITY":
            continue
        key = (r["organism"], r["gene"])
        gi = gene_info.get(key, {})
        base = float(gi.get("priority_score") or 0.0)

        pdb_ids = [p for p in r["pdb_ids"].split(";") if p]
        structs = [enr_by_pdb[p] for p in pdb_ids if p in enr_by_pdb]
        any_cofactor = any(_truthy(s.get("has_cofactor", "")) for s in structs)
        any_complex = any(_truthy(s.get("is_complex", "")) for s in structs)
        any_ligand = any(int(s.get("n_meaningful") or 0) > 0 for s in structs)
        ligand_union = sorted(
            {
                lig
                for s in structs
                for lig in (s.get("ligands_meaningful") or "").split(",")
                if lig
            }
        )

        n = int(r["n_structures"])
        score = (
            base
            + min(n * PER_STRUCTURE_WEIGHT, MAX_STRUCTURE_BONUS)
            + (COFACTOR_BONUS if any_cofactor else 0.0)
            + (COMPLEX_BONUS if any_complex else 0.0)
            + (LIGAND_BONUS if any_ligand else 0.0)
        )

        rows.append(
            WorklistRow(
                rank=0,
                worklist_score=round(score, 2),
                organism=r["organism"],
                gene=r["gene"],
                pmid=r["pmid"],
                paper_year=r["year"],
                n_structures=n,
                gene_priority_score=base,
                candidate_reason=gi.get("candidate_reason", ""),
                exp_mf=gi.get("exp_mf", ""),
                paper_has_cofactor=any_cofactor,
                paper_has_complex=any_complex,
                cofactors=gi.get("cofactors", ""),
                ligands=",".join(ligand_union),
                pdb_ids=r["pdb_ids"],
                already_in_review=_truthy(r["in_ai_review"]),
            )
        )

    # Rank: unreviewed first, then by score; reviewed pinned to the bottom.
    rows.sort(key=lambda w: (w.already_in_review, -w.worklist_score, w.gene))
    for i, w in enumerate(rows, 1):
        w.rank = i
    return rows


def write_tsv(rows: List[WorklistRow], out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    cols = [f.name for f in fields(WorklistRow)]
    with out.open("w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(cols)
        for r in rows:
            w.writerow([getattr(r, c) for c in cols])


def _gene_rollup(rows: List[WorklistRow]) -> List[dict]:
    """Collapse per-paper rows to one entry per gene (the review unit).

    A curator reviews a gene once, weighing all its uncited structure papers
    together; this aggregates them and keeps the best-scoring representative paper.
    """
    by_gene: Dict[Tuple[str, str], List[WorklistRow]] = {}
    for r in rows:
        by_gene.setdefault((r.organism, r.gene), []).append(r)
    out: List[dict] = []
    for (organism, gene), grp in by_gene.items():
        best = max(grp, key=lambda w: (w.worklist_score, w.n_structures))
        out.append(
            {
                "organism": organism,
                "gene": gene,
                "score": best.worklist_score,
                "candidate_reason": best.candidate_reason,
                "exp_mf": best.exp_mf,
                "n_uncited_papers": len(grp),
                "total_structures": sum(w.n_structures for w in grp),
                "best_paper": best.pmid,
                "best_paper_year": best.paper_year,
                "ligands": best.ligands,
                "already_in_review": all(w.already_in_review for w in grp),
            }
        )
    out.sort(key=lambda d: (d["already_in_review"], -d["score"], d["gene"]))
    return out


def write_md(rows: List[WorklistRow], out: Path, top: int = 30) -> str:
    genes = [g for g in _gene_rollup(rows) if not g["already_in_review"]]
    lines = [
        "# PDB GAP_OPPORTUNITY review worklist",
        "",
        "Genes whose deposited structure papers predate their last experimental GO "
        "curation yet are never cited by GOA -- i.e. structural evidence that "
        "curation had the opportunity to use but did not. Ranked by gene priority "
        "(dark-MF / eukaryote / contested-catalytic) plus the cofactor / ligand / "
        "complex richness and number of the uncited structures. Collapsed to one row "
        "per gene (the review unit); per-paper detail is in `data/gap_worklist.tsv`.",
        "",
        f"- Genes with >=1 uncited GAP_OPPORTUNITY structure paper: **{len(genes)}**.",
        f"- Showing top **{min(top, len(genes))}**.",
        "",
        "**Caveat:** bound ligands/cofactors are taken from the whole PDB entry, so "
        "for a subunit solved inside a megacomplex (ribosome, spliceosome, "
        "chaperonin) the ligands may belong to the assembly, not this protein. Treat "
        "the ligand column as a hint, and confirm per-chain contacts during review.",
        "",
        "| # | gene | org | score | reason | exp_MF | uncited papers | total str | best paper | ligands |",
        "| - | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for i, g in enumerate(genes[:top], 1):
        lines.append(
            f"| {i} | {g['gene']} | {g['organism']} | {g['score']} | "
            f"{g['candidate_reason']} | {g['exp_mf']} | {g['n_uncited_papers']} | "
            f"{g['total_structures']} | {g['best_paper']} ({g['best_paper_year']}) | "
            f"{g['ligands'][:36]} |"
        )
    text = "\n".join(lines) + "\n"
    out.write_text(text)
    return text


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    base = Path("projects/PDB")
    ap.add_argument("--gap-tsv", type=Path, default=base / "data/curation_gap.tsv")
    ap.add_argument(
        "--gene-enriched", type=Path, default=base / "data/pdb_gene_enriched.tsv"
    )
    ap.add_argument("--enriched", type=Path, default=base / "data/pdb_enriched.tsv")
    ap.add_argument("--out-tsv", type=Path, default=base / "data/gap_worklist.tsv")
    ap.add_argument("--out-md", type=Path, default=base / "GAP_WORKLIST.md")
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()

    rows = build(args.gap_tsv, args.gene_enriched, args.enriched)
    write_tsv(rows, args.out_tsv)
    print(write_md(rows, args.out_md, top=args.top))
    print(f"Wrote {len(rows)} ranked rows -> {args.out_tsv}")


if __name__ == "__main__":
    main()
