#!/usr/bin/env python3
"""Closure-aware GO enrichment (ORA) of a metabolite set, via Rhea + rhea2go.

This turns the *coverage* bridge into an actual *enrichment*: which GO functions
are over-represented among the enzymes that act on a study's metabolites,
relative to the whole Rhea/GO metabolic universe?

Pipeline:

    metabolite ChEBI  --normalize-->  Rhea participant id(s)        [chebi.rhea_forms]
        --participates in-->  Rhea reaction(s)                      [rhea.py]
            --rhea2go-->  GO molecular-function term(s)             [rhea.py]
                --is_a / part_of closure-->  ancestor GO terms      [go-basic.obo]

Entities are **Rhea participant metabolites**. The background universe is every
participant that maps (through rhea2go + closure) to at least one GO term; the
foreground is the study metabolites mapped into that same participant space. For
each GO term we run a one-sided hypergeometric (Fisher) over-representation test
and report Benjamini-Hochberg FDR.

Because rhea2go is a molecular-function mapping, the directly-reached terms are
GO **molecular function**; closure over ``is_a`` and ``part_of`` lifts them to
more general function terms (and, where ChEBI/GO model it, the occasional parent
of another aspect). True biological-*process* lift needs the enzyme/gene layer
(GOA / GO-CAM) and is the documented next step — but even at MF level the value
GO adds over a flat pathway list is visible: the ontology aggregates many
specific enzyme activities into significantly-enriched higher-level functions.

Everything is computed live (Rhea REST, GO rhea2go, go-basic.obo, OLS4) and
cached under ``.cache/``; nothing is hardcoded.

Usage:
    uv run python go_enrichment.py --chebi-file studies/MTBLS1.chebi.txt \\
        --out studies/MTBLS1-GO-ENRICHMENT.md --title "MTBLS1 GO enrichment" \\
        --source "MetaboLights MTBLS1"
"""
from __future__ import annotations

import argparse
import math
import sys
from collections import defaultdict
from pathlib import Path

import chebi
import rhea

GO_OBO_URL = "https://current.geneontology.org/ontology/go-basic.obo"


# --------------------------------------------------------------------------- #
# GO ontology closure (is_a + part_of) from go-basic.obo
# --------------------------------------------------------------------------- #
def load_go_obo() -> tuple[dict[str, set[str]], dict[str, str], dict[str, str]]:
    """Return (parents, label, namespace) for every GO term in go-basic.obo."""
    text = rhea._cached_text("go-basic.obo", GO_OBO_URL)  # reuse cached downloader
    parents: dict[str, set[str]] = defaultdict(set)
    label: dict[str, str] = {}
    namespace: dict[str, str] = {}
    cur: str | None = None
    in_term = False
    obsolete = False
    for line in text.splitlines():
        if line == "[Term]":
            cur, in_term, obsolete = None, True, False
            continue
        if line.startswith("["):  # [Typedef] etc.
            in_term = False
            continue
        if not in_term:
            continue
        if line.startswith("id: GO:"):
            cur = line[4:].strip()
        elif line.startswith("is_obsolete: true"):
            obsolete = True
        elif cur and not obsolete and line.startswith("name: "):
            label[cur] = line[6:].strip()
        elif cur and not obsolete and line.startswith("namespace: "):
            namespace[cur] = line[11:].strip()
        elif cur and not obsolete and line.startswith("is_a: GO:"):
            parents[cur].add(line[6:].split("!")[0].strip())
        elif cur and not obsolete and line.startswith("relationship: part_of GO:"):
            parents[cur].add(line[len("relationship: part_of "):].split("!")[0].strip())
    return parents, label, namespace


def ancestors_of(term: str, parents: dict[str, set[str]],
                 memo: dict[str, frozenset[str]]) -> frozenset[str]:
    """Reflexive ancestor closure of ``term`` over is_a + part_of."""
    if term in memo:
        return memo[term]
    acc = {term}
    memo[term] = frozenset(acc)  # guard against cycles
    for p in parents.get(term, ()):  # noqa: SIM118
        acc |= ancestors_of(p, parents, memo)
    result = frozenset(acc)
    memo[term] = result
    return result


# --------------------------------------------------------------------------- #
# Hypergeometric over-representation
# --------------------------------------------------------------------------- #
def hypergeom_sf(k: int, N: int, K: int, n: int) -> float:
    """P(X >= k) for X ~ Hypergeometric(N, K, n). Exact, via math.comb."""
    total = math.comb(N, n)
    if total == 0:
        return 1.0
    upper = min(K, n)
    s = sum(math.comb(K, i) * math.comb(N - K, n - i) for i in range(k, upper + 1))
    return s / total


def bh_fdr(pvals: list[float]) -> list[float]:
    """Benjamini-Hochberg adjusted p-values, returned in input order."""
    m = len(pvals)
    order = sorted(range(m), key=lambda i: pvals[i])
    adj = [0.0] * m
    prev = 1.0
    for rank, idx in enumerate(reversed(order), start=1):
        i = m - rank + 1
        val = min(prev, pvals[idx] * m / i)
        adj[idx] = prev = val
    return adj


# --------------------------------------------------------------------------- #
# Enrichment
# --------------------------------------------------------------------------- #
def build_annotations(idx: rhea.RheaIndex, parents: dict[str, set[str]]
                      ) -> dict[str, frozenset[str]]:
    """Rhea participant ChEBI -> closed set of GO terms (via rhea2go + closure)."""
    memo: dict[str, frozenset[str]] = {}
    ann: dict[str, set[str]] = defaultdict(set)
    for chebi_id, rxns in idx.participant_to_reactions.items():
        for rid in rxns:
            go = idx.reaction_to_go.get(rid)
            if go:
                ann[chebi_id] |= ancestors_of(go[0], parents, memo)
    return {c: frozenset(g) for c, g in ann.items() if g}


def enrich(foreground: set[str], ann: dict[str, frozenset[str]],
           label: dict[str, str], namespace: dict[str, str], top: int = 30):
    universe = set(ann)
    fg = foreground & universe
    N, n = len(universe), len(fg)
    term_universe: dict[str, int] = defaultdict(int)
    term_fg: dict[str, int] = defaultdict(int)
    for c in universe:
        for g in ann[c]:
            term_universe[g] += 1
    for c in fg:
        for g in ann[c]:
            term_fg[g] += 1

    records = []
    for g, k in term_fg.items():
        K = term_universe[g]
        # Skip the trivial root-ish terms covering ~everything, and singletons.
        if K < 2 or K == N:
            continue
        p = hypergeom_sf(k, N, K, n)
        fold = (k / n) / (K / N) if K and n else 0.0
        records.append([g, label.get(g, "?"), namespace.get(g, "?"), k, n, K, N, fold, p])

    fdr = bh_fdr([r[8] for r in records])
    for r, q in zip(records, fdr):
        r.append(q)
    records.sort(key=lambda r: (r[9], r[8], -r[7]))
    return N, n, records[:top]


def write_report(out: Path, title: str, source: str | None, N: int, n: int,
                 records, rel_prefix: str) -> None:
    L = []
    L.append("---")
    L.append(f'title: "{title}"')
    L.append("---\n")
    L.append(f"# {title}\n")
    if source:
        L.append(f"**Input:** {source}\n")
    L.append(f"Generated by [`go_enrichment.py`]({rel_prefix}go_enrichment.py) — closure-aware")
    L.append("hypergeometric (Fisher) over-representation of GO terms reached from the")
    L.append("metabolite set through Rhea + `rhea2go`, with `is_a`/`part_of` closure from")
    L.append("`go-basic.obo`. All inputs fetched live; nothing hardcoded.\n")
    L.append(f"- **Foreground**: {n} study metabolites mapped into Rhea-participant space")
    L.append(f"  (normalized for protonation + skeleton).")
    L.append(f"- **Background universe**: {N} Rhea participants reaching ≥1 GO term via rhea2go.")
    L.append(f"- **Test**: one-sided hypergeometric per GO term; **Benjamini-Hochberg FDR**.\n")
    L.append("## Top enriched GO terms\n")
    L.append("| GO term | Aspect | k/n | K/N | Fold | FDR |")
    L.append("|---|---|---:|---:|---:|---:|")
    aspect = {"molecular_function": "MF", "biological_process": "BP", "cellular_component": "CC"}
    for g, lab, ns, k, n_, K, N_, fold, p, q in records:
        L.append(f"| {g} {lab} | {aspect.get(ns, ns)} | {k}/{n_} | {K}/{N_} | "
                 f"{fold:.1f}× | {q:.1e} |")
    L.append("\n## Reading this\n")
    L.append("`k/n` = foreground metabolites annotated to the term / foreground size;")
    L.append("`K/N` = same in the background universe; `Fold` = (k/n)/(K/N). Terms reached")
    L.append("via `rhea2go` are GO **molecular function**; closure lifts them to more general")
    L.append("function terms. BP-level lift via the enzyme/gene layer (GOA / GO-CAM) is the")
    L.append(f"documented next step (see the [project page]({rel_prefix}../../METABOLOMICS.md)).")
    L.append("\n## Method / reproducibility\n")
    L.append(f"- Normalization: [`chebi.py`]({rel_prefix}chebi.py); Rhea + rhea2go:")
    L.append(f"  [`rhea.py`]({rel_prefix}rhea.py); GO closure: `go-basic.obo` (cached).")
    L.append("- Hypergeometric + BH-FDR implemented in-module (no scipy dependency).")
    out.write_text("\n".join(L) + "\n")
    print(f"\nWrote {out}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chebi-file", type=Path, required=True, help="one CHEBI:xxxxx id per line")
    ap.add_argument("--out", type=Path, required=True, help="results markdown path")
    ap.add_argument("--title", default="Metabolite-set GO enrichment (via Rhea + rhea2go)")
    ap.add_argument("--source", help="provenance note")
    ap.add_argument("--top", type=int, default=30)
    args = ap.parse_args()

    tokens = []
    for line in args.chebi_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            tokens.append(line.split()[0].split("\t")[0])

    print("Loading Rhea + rhea2go + GO ontology ...", file=sys.stderr)
    idx = rhea.RheaIndex()
    parents, label, namespace = load_go_obo()
    print(f"  GO terms: {len(label)}; building closed annotations ...", file=sys.stderr)
    ann = build_annotations(idx, parents)
    all_parts: set[str] = set(idx.participant_to_reactions.keys())

    foreground: set[str] = set()
    for tok in tokens:
        seed = chebi.resolve_curie(tok)
        if seed:
            foreground |= chebi.rhea_forms(seed, all_parts)
    print(f"  foreground participants: {len(foreground)}; universe: {len(ann)}", file=sys.stderr)

    N, n, records = enrich(foreground, ann, label, namespace, top=args.top)
    print(f"\n== TOP ENRICHED (N={N}, n={n}) ==", file=sys.stderr)
    for g, lab, ns, k, n_, K, N_, fold, p, q in records[:15]:
        print(f"  FDR={q:.1e}  {fold:4.1f}x  {k}/{n_} vs {K}/{N_}  {g} {lab}", file=sys.stderr)

    rel_prefix = "../" if args.out.parent.name == "studies" else ""
    write_report(args.out, args.title, args.source, N, n, records, rel_prefix)
    return 0


if __name__ == "__main__":
    sys.exit(main())
