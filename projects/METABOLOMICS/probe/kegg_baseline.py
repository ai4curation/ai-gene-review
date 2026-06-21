#!/usr/bin/env python3
"""KEGG-pathway over-representation baseline for the same metabolite set.

This is the incumbent metabolomics-interpretation approach (pathway-membership
ORA, as in MetaboAnalyst over KEGG/SMPDB) implemented honestly and runnably, so
the GO-function enrichment ([`go_enrichment.py`](go_enrichment.py)) can be
compared against a like-for-like statistical baseline on the *same* study and
the *same* hypergeometric test.

Pipeline:

    metabolite ChEBI  --OLS xref-->  KEGG compound (Cxxxxx)
        --KEGG link-->  KEGG pathway(s) (mapNNNNN)
            --hypergeometric ORA + BH-FDR-->  enriched pathways

Background universe = all KEGG compounds that occur in at least one reference
pathway. Everything is fetched live (KEGG REST + OLS4) and cached; nothing is
hardcoded. (We cannot run the MetaboAnalyst web tool from here, so we reproduce
its KEGG-pathway ORA directly rather than pretending to call it.)

Usage:
    uv run python kegg_baseline.py --chebi-file studies/MTBLS1.chebi.txt \\
        --out studies/MTBLS1-KEGG-BASELINE.md --title "MTBLS1 KEGG baseline" \\
        --source "MetaboLights MTBLS1"
"""
from __future__ import annotations

import argparse
import sys
import urllib.parse
from collections import defaultdict
from pathlib import Path

import chebi
import rhea
from go_enrichment import bh_fdr, hypergeom_sf

KEGG = "https://rest.kegg.jp"


def load_pathway_compounds() -> tuple[dict[str, set[str]], dict[str, str]]:
    """Return (pathway -> compound set) and (pathway -> name) for reference maps."""
    links = rhea._cached_text("kegg_pathway_compound.tsv", f"{KEGG}/link/compound/pathway")
    pw2cpd: dict[str, set[str]] = defaultdict(set)
    for line in links.splitlines():
        parts = line.split("\t")
        if len(parts) != 2:
            continue
        pw, cpd = parts[0].replace("path:", ""), parts[1].replace("cpd:", "")
        if pw.startswith("map"):  # reference pathways (organism-independent)
            pw2cpd[pw].add(cpd)
    names: dict[str, str] = {}
    for line in rhea._cached_text("kegg_pathway_list.tsv", f"{KEGG}/list/pathway").splitlines():
        parts = line.split("\t")
        if len(parts) == 2:
            names[parts[0].replace("path:", "")] = parts[1]
    return pw2cpd, names


def chebi_to_kegg(chebi_id: str) -> str | None:
    """Map a ChEBI id to a KEGG compound via OLS cross-references."""
    term_json = chebi._get_json(
        f"{chebi.OLS}/ontologies/chebi/terms?iri="
        + urllib.parse.quote(chebi._iri(chebi_id), safe="")
    )
    terms = term_json.get("_embedded", {}).get("terms", [])
    if not terms:
        return None
    for xref in terms[0].get("annotation", {}).get("database_cross_reference", []):
        if xref.lower().startswith("kegg.compound:"):
            return xref.split(":", 1)[1]
    return None


def resolve_foreground(tokens: list[str]) -> tuple[set[str], list[str]]:
    """Study metabolites -> KEGG compounds (trying the seed, then its proton family)."""
    fg: set[str] = set()
    unmapped: list[str] = []
    for tok in tokens:
        seed = tok if tok.upper().startswith("CHEBI:") else (
            (lambda t: t.curie if t else None)(chebi.search_neutral(tok)))
        if not seed:
            unmapped.append(tok)
            continue
        kegg = chebi_to_kegg(seed)
        if kegg is None:  # try charge variants
            for cid in chebi.protonation_family(seed):
                kegg = chebi_to_kegg(cid)
                if kegg:
                    break
        if kegg:
            fg.add(kegg)
        else:
            unmapped.append(seed)
    return fg, unmapped


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chebi-file", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--title", default="Metabolite-set KEGG pathway ORA (baseline)")
    ap.add_argument("--source")
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()

    tokens = []
    for line in args.chebi_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            tokens.append(line.split()[0].split("\t")[0])

    print("Loading KEGG pathway/compound links ...", file=sys.stderr)
    pw2cpd, names = load_pathway_compounds()
    cpd2pw: dict[str, set[str]] = defaultdict(set)
    for pw, cpds in pw2cpd.items():
        for c in cpds:
            cpd2pw[c].add(pw)
    universe = set(cpd2pw)
    print(f"  reference pathways: {len(pw2cpd)}; compounds in pathways: {len(universe)}",
          file=sys.stderr)

    fg_all, unmapped = resolve_foreground(tokens)
    fg = fg_all & universe
    N, n = len(universe), len(fg)
    print(f"  foreground KEGG compounds: {len(fg_all)} ({n} in pathway universe); "
          f"unmapped: {len(unmapped)}", file=sys.stderr)

    records = []
    for pw, cpds in pw2cpd.items():
        K = len(cpds)
        k = len(fg & cpds)
        if k == 0 or K < 2:
            continue
        p = hypergeom_sf(k, N, K, n)
        fold = (k / n) / (K / N) if K and n else 0.0
        records.append([pw, names.get(pw, "?"), k, n, K, N, fold, p])
    fdr = bh_fdr([r[7] for r in records])
    for r, q in zip(records, fdr):
        r.append(q)
    records.sort(key=lambda r: (r[8], r[7], -r[6]))
    records = records[:args.top]

    print(f"\n== TOP KEGG PATHWAYS (N={N}, n={n}) ==", file=sys.stderr)
    for pw, nm, k, n_, K, N_, fold, p, q in records[:15]:
        print(f"  FDR={q:.1e}  {fold:4.1f}x  {k}/{n_} vs {K}/{N_}  {pw} {nm}", file=sys.stderr)

    rel = "../" if args.out.parent.name == "studies" else ""
    L = ["---", f'title: "{args.title}"', "---\n", f"# {args.title}\n"]
    if args.source:
        L.append(f"**Input:** {args.source}\n")
    L.append(f"Generated by [`kegg_baseline.py`]({rel}kegg_baseline.py) — KEGG-pathway")
    L.append("over-representation (the MetaboAnalyst/KEGG-style incumbent), same one-sided")
    L.append("hypergeometric + BH-FDR as the GO enrichment, on the same study. Live + cached.\n")
    L.append(f"- **Foreground**: {n} study metabolites mapped to KEGG compounds in pathways "
             f"({len(fg_all)} mapped total; {len(unmapped)} unmapped).")
    L.append(f"- **Background universe**: {N} KEGG compounds occurring in reference pathways.\n")
    L.append("## Top enriched KEGG pathways\n")
    L.append("| KEGG pathway | k/n | K/N | Fold | FDR |")
    L.append("|---|---:|---:|---:|---:|")
    for pw, nm, k, n_, K, N_, fold, p, q in records:
        L.append(f"| {pw} {nm} | {k}/{n_} | {K}/{N_} | {fold:.1f}× | {q:.1e} |")
    L.append("\n## Why compare\n")
    L.append("KEGG/SMPDB ORA reports **pathway membership** — broad buckets like")
    L.append("\"amino acid metabolism\". The [GO enrichment]("
             f"{Path(args.out).name.replace('KEGG-BASELINE', 'GO-ENRICHMENT')}) reports the")
    L.append("specific **molecular activities** (transaminase, amino-acid oxidase, racemase)")
    L.append("and uses the ontology's `is_a`/`part_of` closure to aggregate them — a")
    L.append("complementary, finer-grained readout on the identical metabolite set and test.")
    args.out.write_text("\n".join(L) + "\n")
    print(f"\nWrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
