#!/usr/bin/env python3
"""Estimate the GO annotation gain from ingesting NCBIFAM's own GO assignments.

NCBIFAM HMM models (``hmm_PGAP.tsv``) carry NCBI-curated ``go_terms`` that GO
does not ingest (there is no ``ncbifam2go`` external2go file -- see
``../NCBIFam.md``). This probe quantifies, live against UniProtKB, how many
GO annotations would be *gained* if a model's NCBI GO term were propagated to
every entry that already carries the model's signature.

For each NCBIFAM model with a GO term, UniProt is asked:

    gain = N(carries the NCBIFAM signature) - N(carries it AND already has the GO term)

This mirrors the RHEA project's ``rhea_annotation_gain.py``. Two important
properties carry over:

  * UniProt's ``go:<id>`` query is **closure-aware** (matches the term and its
    descendants), so a model whose GO term is already covered by a more specific
    child counts as *no gain* -- the gain is a closure-filtered estimate, not a
    naive exact-match one. A high gain therefore means the NCBI GO term (or any
    descendant) is genuinely absent, i.e. NCBIFAM's assignment is not reaching
    GOA (the model is unintegrated in InterPro, or its InterPro entry lacks an
    interpro2go row).
  * Gain is reported for **Swiss-Prot (reviewed)** -- the curation-relevant,
    trustworthy number -- and for all of UniProtKB (mostly TrEMBL) as context.

Counts use the UniProtKB REST ``x-total-results`` header (no records fetched).

Usage::

    uv run python ncbifam_go_gain.py --sample 25            # deterministic equivalog sample
    uv run python ncbifam_go_gain.py --accessions TIGR00873,NF003202.0
    uv run python ncbifam_go_gain.py --family-type equivalog --single-go --sample 40
"""

from __future__ import annotations

import argparse
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

HMM_PGAP_URL = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv"
SEARCH = "https://rest.uniprot.org/uniprotkb/search"
UA = "ai-gene-review-ncbifam/1.0"

COL_ACCESSION, COL_FAMILY_TYPE, COL_PRODUCT, COL_EC, COL_GO = 0, 6, 10, 13, 14


def _load_hmm(cache: Path) -> list[list[str]]:
    if not cache.exists():
        req = urllib.request.Request(HMM_PGAP_URL, headers={"User-Agent": UA})
        with urllib.request.urlopen(req, timeout=120) as resp:  # noqa: S310
            cache.write_bytes(resp.read())
    lines = cache.read_text("utf-8", "replace").splitlines()
    return [ln.split("\t") for ln in lines[1:] if ln]


def count(query: str, timeout: int = 40) -> int | None:
    params = urllib.parse.urlencode({"query": query, "size": 0})
    req = urllib.request.Request(f"{SEARCH}?{params}", headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
            val = resp.headers.get("x-total-results")
            return int(val) if val is not None else None
    except Exception:  # pragma: no cover - network dependent
        return None


def _xref_id(acc: str) -> str:
    """UniProt indexes the NCBIFAM xref without the version suffix (NF003202.0 -> NF003202)."""
    return acc.split(".")[0]


def select(
    rows: list[list[str]], family_type: str | None, single_go: bool, sample: int
) -> list[tuple[str, str, str, str]]:
    out: list[tuple[str, str, str, str]] = []
    for r in rows:
        if len(r) <= COL_GO:
            continue
        go = r[COL_GO].strip()
        if not go:
            continue
        if family_type and r[COL_FAMILY_TYPE] != family_type:
            continue
        if single_go and not go.replace(" ", "").replace(",", "+").count("+") == 0:
            # keep only a single GO id
            if (
                len([t for t in go.replace(",", " ").split() if t.startswith("GO:")])
                != 1
            ):
                continue
        first_go = next(t for t in go.replace(",", " ").split() if t.startswith("GO:"))
        out.append(
            (r[COL_ACCESSION], first_go, r[COL_EC].strip(), r[COL_PRODUCT].strip())
        )
    out.sort(key=lambda t: t[0])  # deterministic
    if sample and len(out) > sample:
        step = len(out) / sample
        out = [out[int(i * step)] for i in range(sample)]
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--hmm-cache", type=Path, default=Path("/tmp/hmm_PGAP.tsv"))
    ap.add_argument("--accessions", help="comma-separated NCBIFAM accessions to score")
    ap.add_argument("--family-type", default="equivalog")
    ap.add_argument(
        "--single-go", action="store_true", help="only models with exactly one GO id"
    )
    ap.add_argument("--sample", type=int, default=25)
    ap.add_argument("--sleep", type=float, default=0.3)
    args = ap.parse_args(argv)

    rows = _load_hmm(args.hmm_cache)
    if args.accessions:
        wanted = set(args.accessions.split(","))
        by_acc = {r[COL_ACCESSION]: r for r in rows if len(r) > COL_GO}
        by_acc.update({_xref_id(r[COL_ACCESSION]): r for r in rows if len(r) > COL_GO})
        picks = []
        for w in wanted:
            r = by_acc.get(w)
            if not r or not r[COL_GO].strip():
                print(f"# skip {w}: not found or no GO", file=sys.stderr)
                continue
            first_go = next(
                t for t in r[COL_GO].replace(",", " ").split() if t.startswith("GO:")
            )
            picks.append(
                (r[COL_ACCESSION], first_go, r[COL_EC].strip(), r[COL_PRODUCT].strip())
            )
    else:
        picks = select(rows, args.family_type, args.single_go, args.sample)

    print(
        "ncbifam\tgo\tN_all\tN_all_go\tgain_all\tN_rev\tN_rev_go\tgain_rev\tec\tproduct"
    )
    tot = tot_rev = 0
    nz_rev = 0
    for acc, go, ec, product in picks:
        xid = _xref_id(acc)
        goid = go.split(":")[1]
        sig = f"xref:ncbifam-{xid}"
        n_all = count(sig)
        n_all_go = count(f"{sig} AND go:{goid}")
        n_rev = count(f"{sig} AND reviewed:true")
        n_rev_go = count(f"{sig} AND go:{goid} AND reviewed:true")
        g_all = (n_all - n_all_go) if None not in (n_all, n_all_go) else None
        g_rev = (n_rev - n_rev_go) if None not in (n_rev, n_rev_go) else None
        if g_all:
            tot += g_all
        if g_rev:
            tot_rev += g_rev
            nz_rev += 1
        print(
            f"{acc}\t{go}\t{n_all}\t{n_all_go}\t{g_all}\t{n_rev}\t{n_rev_go}\t{g_rev}"
            f"\t{ec}\t{product[:50]}"
        )
        time.sleep(args.sleep)

    print(f"\n# models scored: {len(picks)} (non-zero reviewed gain: {nz_rev})")
    print(f"# TOTAL new annotations, Swiss-Prot (reviewed) [PRIMARY]: {tot_rev}")
    print(f"# TOTAL new annotations, all UniProtKB (secondary/TrEMBL): {tot}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
