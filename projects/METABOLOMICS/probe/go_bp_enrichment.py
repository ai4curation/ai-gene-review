#!/usr/bin/env python3
"""Closure-aware GO **biological-process** enrichment of a metabolite set.

The molecular-function enrichment ([`go_enrichment.py`](go_enrichment.py)) stops
at enzyme *activities* because `rhea2go` is an MF mapping. To reach GO biological
**process** we go through the enzyme/gene layer — the documented next step:

    metabolite ChEBI --normalize--> Rhea participant --in--> Rhea reaction
        --catalyzed by--> human Swiss-Prot enzyme (UniProt)
            --GOA--> GO biological-process term --closure--> ancestors

Restricting to one organism (human, taxon 9606 — MTBLS1 is human urine) keeps
the enzyme fan-out tractable and biologically apt: a single UniProt download of
reviewed human enzymes with catalytic activity yields, per enzyme, *both* its
Rhea reactions and its GO BP annotations. Entities are **enzymes** (a standard
gene-set ORA); the foreground is the enzymes that catalyse reactions involving
the study metabolites, the background is all human metabolic enzymes.

Hub/cofactor metabolites (ATP, NAD(P), CoA, H2O, Pi…) catalyse a large fraction
of enzymes; the ORA background absorbs most of that, but they can still inflate
the foreground, so `--exclude-cofactors` is offered (default on) to drop a small
set of currency metabolites. Everything is live + cached; nothing is hardcoded.

Usage:
    uv run python go_bp_enrichment.py --chebi-file studies/MTBLS1.chebi.txt \\
        --out studies/MTBLS1-GO-BP-ENRICHMENT.md --source "MetaboLights MTBLS1"
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

import chebi
import rhea
from go_enrichment import ancestors_of, bh_fdr, hypergeom_sf, load_go_obo

UNIPROT = "https://rest.uniprot.org/uniprotkb/search"
# Currency/cofactor metabolites are identified *data-drivenly* by their degree in
# the Rhea network (number of reactions they participate in) rather than a
# hand-curated id list. The observed top of the degree distribution (computed
# from the cached Rhea participant table) is exactly the currency set, while the
# first genuine signal metabolite sits below the default threshold:
#   hydron 10342 · water 6724 · dioxygen 2946 · CoA 1649 · ATP 1384 ·
#   NADP 1382 · NADPH 1375 · NAD 1282 · diphosphate 1221 · NADH 1209 ·
#   CO2 1087 · phosphate 1061 · SAM 954 · ADP 898 · FMN 892 · ... · ammonium 545
#   | --- default cutoff 500 --- | 2-oxoglutarate(2-) 456 · acetyl-CoA 417 (kept)
# So threshold 500 drops the unambiguous currency and keeps central metabolites
# like 2-oxoglutarate and acetyl-CoA.
DEFAULT_COFACTOR_DEGREE = 500


def _get(url: str, timeout: int = 90, retries: int = 3):
    # Retry with exponential backoff like rhea._get_text / chebi._get_json, so a
    # transient failure mid-pagination in download_enzymes() does not lose progress.
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "ai-gene-review-metabolomics/1.0"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.headers, resp.read().decode(errors="replace")
        except Exception as e:  # noqa: BLE001 - retry on any transient network error
            last = e
            time.sleep(2 ** attempt)
    raise RuntimeError(f"UniProt request failed after {retries} tries: {url}: {last}")


def download_enzymes(taxon: int = 9606) -> str:
    """All reviewed enzymes (catalytic activity) of ``taxon`` with Rhea + GO-BP.

    Follows UniProt REST cursor pagination and concatenates the TSV pages; cached
    per taxon.
    """
    cache = rhea.CACHE / f"uniprot_enzymes_{taxon}.tsv"
    if cache.exists():
        return cache.read_text()
    params = urllib.parse.urlencode({
        "query": f"reviewed:true AND organism_id:{taxon} AND (cc_catalytic_activity:*)",
        "fields": "accession,rhea,go_p", "format": "tsv", "size": 500,
    })
    url = f"{UNIPROT}?{params}"
    rows: list[str] = []
    header: str | None = None
    while url:
        hdr, text = _get(url)
        lines = text.splitlines()
        if lines:
            if header is None:
                header = lines[0]
            rows.extend(lines[1:])
        link = hdr.get("Link", "")
        m = re.search(r'<([^>]+)>;\s*rel="next"', link)
        url = m.group(1) if m else None
    out = "\n".join([header or "Entry\tRhea ID\tGO"] + rows) + "\n"
    rhea.CACHE.mkdir(parents=True, exist_ok=True)
    cache.write_text(out)
    return out


_GO = re.compile(r"\[(GO:\d+)\]")


def parse_enzymes(text: str):
    """Return (enzyme->rhea reaction ids, enzyme->GO BP ids, reaction->enzymes)."""
    enz_rhea: dict[str, set[str]] = {}
    enz_bp: dict[str, set[str]] = {}
    rxn_enz: dict[str, set[str]] = defaultdict(set)
    for line in text.splitlines()[1:]:
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        acc, rhea_field, go_field = parts[0], parts[1], parts[2]
        rxns = {r.replace("RHEA:", "") for r in rhea_field.split() if r.startswith("RHEA:")}
        bps = set(_GO.findall(go_field))
        if not rxns:
            continue
        enz_rhea[acc] = rxns
        enz_bp[acc] = bps
        for r in rxns:
            rxn_enz[r].add(acc)
    return enz_rhea, enz_bp, rxn_enz


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--chebi-file", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--title", default="Metabolite-set GO biological-process enrichment")
    ap.add_argument("--source")
    ap.add_argument("--top", type=int, default=30)
    ap.add_argument("--keep-cofactors", action="store_true",
                    help="do NOT drop currency/cofactor metabolites (default: drop)")
    ap.add_argument("--cofactor-degree", type=int, default=DEFAULT_COFACTOR_DEGREE,
                    help="Rhea reaction-degree at/above which a participant is treated "
                         "as currency/cofactor (default %(default)s)")
    ap.add_argument("--taxon", type=int, default=9606,
                    help="NCBI taxon for the enzyme/GO-BP layer (default 9606 = human)")
    args = ap.parse_args()

    tokens = []
    for line in args.chebi_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            tokens.append(line.split()[0].split("\t")[0])

    print(f"Loading Rhea network, taxon {args.taxon} enzymes (UniProt), GO ontology ...",
          file=sys.stderr)
    idx = rhea.RheaIndex()
    enz_rhea, enz_bp, rxn_enz = parse_enzymes(download_enzymes(args.taxon))
    parents, label, namespace = load_go_obo()
    print(f"  taxon-{args.taxon} enzymes with Rhea: {len(enz_rhea)}; "
          f"reactions catalysed: {len(rxn_enz)}", file=sys.stderr)

    # enzyme -> closed BP set (restricted to biological_process namespace)
    memo: dict = {}
    enz_bp_closed: dict[str, frozenset[str]] = {}
    for acc, bps in enz_bp.items():
        acc_terms: set[str] = set()
        for g in bps:
            for a in ancestors_of(g, parents, memo):
                if namespace.get(a) == "biological_process":
                    acc_terms.add(a)
        if acc_terms:
            enz_bp_closed[acc] = frozenset(acc_terms)

    all_parts = set(idx.participant_to_reactions.keys())
    degree = {c: len(rs) for c, rs in idx.participant_to_reactions.items()}
    is_cofactor = (lambda c: (not args.keep_cofactors)
                   and degree.get(c, 0) >= args.cofactor_degree)
    # study metabolites -> implicated Rhea reactions
    implicated_rxns: set[str] = set()
    used_metabolites = 0
    excluded_cofactors: set[str] = set()
    for tok in tokens:
        seed = chebi.resolve_curie(tok)
        if not seed:
            continue
        forms = {f for f in chebi.rhea_forms(seed, all_parts) if not is_cofactor(f)}
        if not forms and chebi.rhea_forms(seed, all_parts):
            excluded_cofactors.add(seed)
            continue
        rxns = set()
        for f in forms:
            rxns |= idx.reactions_for(f)
        if rxns:
            used_metabolites += 1
        implicated_rxns |= rxns

    foreground = {e for r in implicated_rxns for e in rxn_enz.get(r, ())} & set(enz_bp_closed)
    background = set(enz_bp_closed)
    N, n = len(background), len(foreground)
    print(f"  metabolites used: {used_metabolites}; implicated reactions: {len(implicated_rxns)}",
          file=sys.stderr)
    print(f"  foreground enzymes: {n} / background {N}", file=sys.stderr)

    term_bg: dict[str, int] = defaultdict(int)
    term_fg: dict[str, int] = defaultdict(int)
    for e in background:
        for g in enz_bp_closed[e]:
            term_bg[g] += 1
    for e in foreground:
        for g in enz_bp_closed[e]:
            term_fg[g] += 1

    records = []
    for g, k in term_fg.items():
        K = term_bg[g]
        if K < 3 or K == N:
            continue
        p = hypergeom_sf(k, N, K, n)
        fold = (k / n) / (K / N) if K and n else 0.0
        records.append([g, label.get(g, "?"), k, n, K, N, fold, p])
    fdr = bh_fdr([r[7] for r in records])
    for r, q in zip(records, fdr):
        r.append(q)
    records.sort(key=lambda r: (r[8], r[7], -r[6]))
    records = records[:args.top]

    print(f"\n== TOP GO BP (N={N}, n={n}) ==", file=sys.stderr)
    for g, lab, k, n_, K, N_, fold, p, q in records[:15]:
        print(f"  FDR={q:.1e}  {fold:4.1f}x  {k}/{n_} vs {K}/{N_}  {g} {lab}", file=sys.stderr)

    rel = "../" if args.out.parent.name == "studies" else ""
    L = ["---", f'title: "{args.title}"', "---\n", f"# {args.title}\n"]
    if args.source:
        L.append(f"**Input:** {args.source}\n")
    L.append(f"Generated by [`go_bp_enrichment.py`]({rel}go_bp_enrichment.py) — GO")
    L.append("**biological-process** ORA via the enzyme/gene layer: metabolite → Rhea")
    L.append("reaction → human Swiss-Prot enzyme (UniProt) → GO BP, with `is_a`/`part_of`")
    L.append("closure and a one-sided hypergeometric test (BH-FDR). Live + cached.\n")
    L.append(f"- **Foreground**: {n} human enzymes catalysing reactions that involve the study")
    L.append(f"  metabolites ({used_metabolites} metabolites mapped to reactions).")
    L.append(f"- **Background**: {N} human reviewed metabolic enzymes with ≥1 GO BP term.")
    if args.keep_cofactors:
        L.append("- **Currency/cofactor metabolites**: kept.\n")
    else:
        L.append(f"- **Currency/cofactor metabolites**: excluded by Rhea reaction-degree "
                 f"≥ {args.cofactor_degree} ({len(excluded_cofactors)} of the study's metabolites "
                 f"dropped: {', '.join(sorted(excluded_cofactors)) or 'none'}).\n")
    L.append("## Top enriched GO biological processes\n")
    L.append("| GO BP term | k/n | K/N | Fold | FDR |")
    L.append("|---|---:|---:|---:|---:|")
    for g, lab, k, n_, K, N_, fold, p, q in records:
        L.append(f"| {g} {lab} | {k}/{n_} | {K}/{N_} | {fold:.1f}× | {q:.1e} |")
    L.append("\n## Where this sits\n")
    L.append("This completes the bridge from metabolomics to GO **biological process** by")
    L.append("routing through the curated enzyme/gene annotations (the layer GO-CAM also")
    L.append("builds on). It is organism-specific (human) by construction.")
    # Cross-link only to companion reports that actually exist for this study.
    sibs = []
    for tag, desc in [("GO-ENRICHMENT", "GO molecular-function enrichment (activities)"),
                      ("KEGG-BASELINE", "KEGG-pathway baseline (membership)")]:
        cand = Path(args.out).name.replace("GO-BP-ENRICHMENT", tag)
        if (Path(args.out).parent / cand).exists():
            sibs.append(f"[{desc}]({cand})")
    if sibs:
        L.append("Compare with " + " and ".join(sibs) + " on the same metabolites.")
    args.out.write_text("\n".join(L) + "\n")
    print(f"\nWrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
