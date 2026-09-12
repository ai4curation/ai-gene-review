#!/usr/bin/env python3
"""Subfamily placement + catalytic-site analysis for a patatin/pPLA protein.

Pipeline (all results derived from the input FASTA; nothing hardcoded):
  1. Multiple sequence alignment with FAMSA (pyfamsa).
  2. Pairwise %identity of every reference to the QUERY (computed from the MSA).
  3. Neighbour-joining tree (BioPython) -> report the QUERY's sister group.
  4. Catalytic-site analysis: locate the patatin nucleophile elbow (G-x-S-x-G,
     catalytic Ser) and the catalytic Asp column from the conservation pattern of
     the reference enzymes, then report what residue the QUERY carries there.

The QUERY is identified by a label/header starting with 'QUERY'.

Usage:
    uv run python scripts/analyze.py --fasta data/sequences.fasta --outdir results
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from Bio import Phylo
from Bio.Align import MultipleSeqAlignment
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from pyfamsa import Aligner, Sequence


def read_fasta(path: Path) -> list[tuple[str, str]]:
    recs: list[tuple[str, str]] = []
    name = None
    seq: list[str] = []
    for line in path.read_text().splitlines():
        if line.startswith(">"):
            if name is not None:
                recs.append((name, "".join(seq)))
            name = line[1:].split()[0]  # label|accession token
            seq = []
        else:
            seq.append(line.strip())
    if name is not None:
        recs.append((name, "".join(seq)))
    return recs


def run_msa(recs: list[tuple[str, str]]) -> list[tuple[str, str]]:
    seqs = [Sequence(n.encode(), s.encode()) for n, s in recs]
    aligner = Aligner(guide_tree="upgma")
    msa = aligner.align(seqs)
    return [(s.id.decode(), s.sequence.decode()) for s in msa]


def pairwise_identity(qaln: str, raln: str) -> tuple[float, float, int]:
    """Return (%identity over aligned columns, %coverage of query, aligned_cols)."""
    matches = aligned = qlen = 0
    for q, r in zip(qaln, raln):
        if q != "-":
            qlen += 1
        if q != "-" and r != "-":
            aligned += 1
            if q == r:
                matches += 1
    ident = 100.0 * matches / aligned if aligned else 0.0
    cov = 100.0 * aligned / qlen if qlen else 0.0
    return ident, cov, aligned


def column_consensus(aln: dict[str, str], names: list[str], col: int) -> tuple[str, float]:
    """Most common non-gap residue in a column over `names`, and its fraction."""
    residues = [aln[n][col] for n in names if aln[n][col] != "-"]
    if not residues:
        return "-", 0.0
    res, count = Counter(residues).most_common(1)[0]
    return res, count / len(residues)


def find_motif_columns(aln: dict[str, str], ref_names: list[str], ncols: int):
    """Detect catalytic Ser (G-x-S-x-G) and catalytic Asp columns from reference
    conservation. Returns dict with column indices and supporting stats.

    `ref_names` here should be the CORE ACTIVE reference set (single-domain active
    patatin enzymes) so the catalytic columns are cleanly conserved. The query and
    any pseudoenzyme / atypical large members are excluded by the caller.
    """
    cons = [column_consensus(aln, ref_names, c) for c in range(ncols)]

    # Catalytic Ser = the best-conserved consensus-S column that sits in a
    # G-x-S-x-G context (conserved G at -2 and +2). Pick the HIGHEST conservation
    # (the patatin nucleophile elbow Ser is ~invariant among active enzymes).
    ser_candidates = []
    for c in range(2, ncols - 2):
        res, frac = cons[c]
        if res == "S" and frac >= 0.6:
            gm2, fm2 = cons[c - 2]
            gp2, fp2 = cons[c + 2]
            if gm2 == "G" and gp2 == "G" and fm2 >= 0.5 and fp2 >= 0.5:
                ser_candidates.append((c, frac, fm2, fp2))
    ser_candidates.sort(key=lambda x: x[1], reverse=True)
    ser_col = ser_candidates[0][0] if ser_candidates else None

    # Catalytic Asp = the best-conserved consensus-D column (after the Ser) whose
    # following column is a conserved G (the patatin DG/DGG block).
    asp_candidates = []
    start = (ser_col + 1) if ser_col is not None else 1
    for c in range(start, ncols - 1):
        res, frac = cons[c]
        if res == "D" and frac >= 0.55:
            gp1, fp1 = cons[c + 1]
            if gp1 == "G" and fp1 >= 0.4:
                asp_candidates.append((c, frac, fp1))
    asp_candidates.sort(key=lambda x: x[1], reverse=True)
    asp_col = asp_candidates[0][0] if asp_candidates else None

    return {
        "ser_col": ser_col,
        "asp_col": asp_col,
        "ser_candidates": ser_candidates,
        "asp_candidates": asp_candidates,
        "consensus": cons,
    }


def scan_catalytic_motifs(name: str, raw_seq: str) -> dict:
    """Scan a RAW (ungapped) sequence for the two diagnostic patatin catalytic
    motifs, independent of any MSA:
      - nucleophile elbow  G-x-S-x-G  (contains the catalytic Ser)
      - oxyanion / glycine-rich block  D-G-G-G  (patatin block I)
    Returns presence flags and matched positions (1-based)."""
    import re
    gxsxg = [(m.start() + 3, m.group(1))
             for m in re.finditer(r"(?=(G.S.G))", raw_seq)]
    dggg = [(m.start() + 1, m.group(0)) for m in re.finditer(r"DGGG", raw_seq)]
    # broader oxyanion variant DGG (some members are DGA/DGG)
    dgg = [(m.start() + 1, m.group(0)) for m in re.finditer(r"DG[GA]", raw_seq)]
    return {
        "sequence": name,
        "length": len(raw_seq),
        "GxSxG_nucleophile_count": len(gxsxg),
        "GxSxG_positions": ";".join(f"{p}:{s}" for p, s in gxsxg) or "NONE",
        "DGGG_oxyanion_count": len(dggg),
        "DGGG_positions": ";".join(f"{p}:{s}" for p, s in dggg) or "NONE",
        "DGG_or_DGA_count": len(dgg),
    }


def ungapped_index(aln_seq: str, col: int) -> int | None:
    """1-based residue index in the ungapped sequence for an alignment column."""
    if aln_seq[col] == "-":
        return None
    return sum(1 for ch in aln_seq[: col + 1] if ch != "-")


def window(aln_seq: str, col: int, flank: int = 2) -> str:
    return aln_seq[max(0, col - flank): col + flank + 1]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fasta", type=Path, default=Path("data/sequences.fasta"))
    ap.add_argument("--outdir", type=Path, default=Path("results"))
    ap.add_argument(
        "--catalytic-exclude", nargs="*", default=["pPLAI_", "pPLAIIId_PLP9"],
        help="Label substrings to EXCLUDE from the catalytic-consensus reference "
             "set (default: the atypical large pPLA-I and the annotated inactive "
             "pseudoenzyme PLP9). Subfamily placement still uses all references.",
    )
    args = ap.parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    recs = read_fasta(args.fasta)
    query = next((n for n, _ in recs if n.upper().startswith("QUERY")), None)
    if query is None:
        raise SystemExit("No QUERY sequence found (header must start with 'QUERY')")

    aligned = run_msa(recs)
    aln = dict(aligned)
    ncols = len(next(iter(aln.values())))
    ref_names = [n for n, _ in aligned if n != query]

    # Save MSA
    (args.outdir / "alignment.fasta").write_text(
        "\n".join(f">{n}\n{s}" for n, s in aligned) + "\n"
    )

    # 1. Pairwise identity to query
    rows = []
    for n in ref_names:
        ident, cov, ncol = pairwise_identity(aln[query], aln[n])
        rows.append((n, ident, cov, ncol))
    rows.sort(key=lambda x: x[1], reverse=True)
    with (args.outdir / "pairwise_identity_to_query.tsv").open("w") as fh:
        fh.write("reference\tpct_identity\tpct_query_coverage\taligned_cols\n")
        for n, ident, cov, ncol in rows:
            fh.write(f"{n}\t{ident:.1f}\t{cov:.1f}\t{ncol}\n")

    # 2. NJ tree + query sister group
    bio_aln = MultipleSeqAlignment(
        [SeqRecord(Seq(s), id=n, description="") for n, s in aligned]
    )
    dm = DistanceCalculator("identity").get_distance(bio_aln)
    nj_tree = DistanceTreeConstructor().nj(dm)
    Phylo.write(nj_tree, args.outdir / "nj_tree.newick", "newick")

    qclade = next(t for t in nj_tree.get_terminals() if t.name == query)
    # Report nearest references by patristic (tree) distance — robust to the long
    # branch a truncated query produces (a 'parent clade' readout can be misleading).
    dists = sorted(
        ((t.name, nj_tree.distance(qclade, t)) for t in nj_tree.get_terminals()
         if t.name != query),
        key=lambda x: x[1],
    )
    sisters = [n for n, _ in dists[:4]]

    # 2b. MSA-independent motif scan on raw sequences (nucleophile + oxyanion)
    raw = {n: s.replace("-", "") for n, s in aligned}
    motif_scan = [scan_catalytic_motifs(n, raw[n]) for n, _ in aligned]
    with (args.outdir / "motif_scan.tsv").open("w") as fh:
        cols = ["sequence", "length", "GxSxG_nucleophile_count", "GxSxG_positions",
                "DGGG_oxyanion_count", "DGGG_positions", "DGG_or_DGA_count"]
        fh.write("\t".join(cols) + "\n")
        for row in motif_scan:
            fh.write("\t".join(str(row[c]) for c in cols) + "\n")

    # 3. Catalytic site (detect columns from CORE ACTIVE single-domain enzymes)
    core_active = [
        n for n in ref_names
        if not any(sub in n for sub in args.catalytic_exclude)
    ]
    motif = find_motif_columns(aln, core_active, ncols)

    # Verification dump: residue of EVERY sequence at the detected catalytic
    # columns (so the column choice can be eyeballed; the pseudoenzyme PLP9 and
    # the query are included as test cases).
    with (args.outdir / "catalytic_columns_all_seqs.tsv").open("w") as fh:
        cols = {"catalytic_Ser": motif["ser_col"], "catalytic_Asp": motif["asp_col"]}
        fh.write("sequence\t" + "\t".join(
            f"{r}(col{c})" for r, c in cols.items()) + "\tin_core_active\n")
        for n, s in aligned:
            vals = [aln[n][c] if c is not None else "?" for c in cols.values()]
            fh.write(f"{n}\t" + "\t".join(vals) +
                     f"\t{'yes' if n in core_active else 'no'}\n")

    cat_rows = []
    cat_summary: dict = {}
    for role, col in (("catalytic_Ser", motif["ser_col"]), ("catalytic_Asp", motif["asp_col"])):
        if col is None:
            cat_summary[role] = {"detected": False}
            continue
        ref_res, ref_frac = column_consensus(aln, core_active, col)
        q_res = aln[query][col]
        q_idx = ungapped_index(aln[query], col)
        cat_rows.append((role, col, ref_res, f"{ref_frac:.2f}", q_res,
                         q_idx if q_idx else "gap", window(aln[query], col)))
        cat_summary[role] = {
            "detected": True,
            "alignment_col": col,
            "ref_consensus": ref_res,
            "ref_conservation": round(ref_frac, 3),
            "query_residue": q_res,
            "query_resnum": q_idx,
            "query_window": window(aln[query], col),
            "match": q_res == ref_res,
        }
    with (args.outdir / "catalytic_site.tsv").open("w") as fh:
        fh.write("role\taln_col\tref_consensus\tref_conservation\tquery_residue\tquery_resnum\tquery_window\n")
        for r in cat_rows:
            fh.write("\t".join(str(x) for x in r) + "\n")

    # GxSxG intact in query?
    gxsxg_ok = None
    if motif["ser_col"] is not None:
        w = window(aln[query], motif["ser_col"], flank=2).replace("-", "")
        gxsxg_ok = (len(w) == 5 and w[0] == "G" and w[2] == "S" and w[4] == "G")

    nearest = rows[0]
    summary = {
        "query": query,
        "n_references": len(ref_names),
        "nearest_reference_by_identity": {
            "reference": nearest[0], "pct_identity": round(nearest[1], 1),
            "pct_query_coverage": round(nearest[2], 1),
        },
        "top5_by_identity": [
            {"reference": n, "pct_identity": round(i, 1), "pct_query_coverage": round(c, 1)}
            for n, i, c, _ in rows[:5]
        ],
        "nj_sister_group": sisters,
        "catalytic_site": cat_summary,
        "query_GxSxG_intact": gxsxg_ok,
    }
    (args.outdir / "summary.json").write_text(json.dumps(summary, indent=2))

    print("=== SUBFAMILY PLACEMENT ===")
    print(f"Query: {query}  (vs {len(ref_names)} references)")
    print("Top hits by %identity:")
    for n, i, c, _ in rows[:6]:
        print(f"  {n:28s} id={i:5.1f}%  cov={c:5.1f}%")
    print(f"NJ sister group: {sisters}")
    print("\n=== CATALYTIC SITE ===")
    for role, info in cat_summary.items():
        if info.get("detected"):
            print(f"  {role}: ref consensus {info['ref_consensus']} "
                  f"({info['ref_conservation']:.0%}) | query has "
                  f"'{info['query_residue']}' at pos {info['query_resnum']} "
                  f"(window {info['query_window']}) | match={info['match']}")
        else:
            print(f"  {role}: NOT DETECTED")
    print(f"  Query G-x-S-x-G nucleophile elbow intact: {gxsxg_ok}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
