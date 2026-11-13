#!/usr/bin/env python3
"""Measure the headroom for a hand-written ``cdd2go`` mapping.

Companion to ``ncbifam_go_gain.py``, which cannot be reused for CDD. That script
propagates a model's *own* NCBI-curated GO term and measures the closure-aware
gain. CDD-proper has no native GO (established in ``../NCBIFam.md``), so there is
nothing to propagate and no gain to compute: a ``cdd2go`` file would have to be
**authored**, term by term, not ingested.

That changes the question. Before writing any terms, the thing worth knowing is
whether the proteins a CDD model matches are *already annotated by other routes*.
If they are, an authored mapping buys little however good the model is. So this
probe measures three things, live:

1. **Integration.** How many of InterPro's CDD models are integrated into an
   InterPro entry at all. An unintegrated model contributes nothing to GOA,
   because CDD reaches GO only through ``interpro2go``.

2. **Headroom.** For a deterministic sample of *unintegrated* models: how many
   UniProtKB entries carry the model, and how many of those already have some
   molecular-function annotation (``go:0003674``, closure-aware, so any MF
   descendant counts). The difference is the population an authored mapping
   could actually reach. This is the CDD analogue of ``gain`` and needs no
   proposed term.

3. **Worked example.** For a named model and a proposed GO term, the ordinary
   closure-aware gain, computed exactly as ``ncbifam_go_gain.py`` does.

Counts come from the UniProtKB REST ``x-total-results`` header; no records are
fetched. Entry metadata comes from the InterPro API.

Usage::

    uv run python cdd_go_gap_probe.py --integration
    uv run python cdd_go_gap_probe.py --headroom --sample 40
    uv run python cdd_go_gap_probe.py --gain cd21555:GO:0009055
"""

from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.parse
import urllib.request

INTERPRO_CDD = "https://www.ebi.ac.uk/interpro/api/entry/cdd/"
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
UA = "cdd-go-gap-probe/1.0"


def _get_json(url: str, timeout: int = 90) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
        return json.load(resp)


def count(query: str, timeout: int = 40) -> int | None:
    """UniProtKB hit count for a query, or None when the request fails."""
    params = urllib.parse.urlencode({"query": query, "size": 0})
    req = urllib.request.Request(
        f"{UNIPROT_SEARCH}?{params}", headers={"User-Agent": UA}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310
            val = resp.headers.get("x-total-results")
            return int(val) if val is not None else None
    except Exception:  # pragma: no cover - network dependent
        return None


def fetch_entries(page_size: int = 200, limit: int | None = None) -> list[dict]:
    """Every CDD entry InterPro knows, with its integration status."""
    out: list[dict] = []
    url = f"{INTERPRO_CDD}?page_size={page_size}"
    while url:
        data = _get_json(url)
        for row in data.get("results", []):
            out.append(row["metadata"])
        if limit is not None and len(out) >= limit:
            return out[:limit]
        url = data.get("next")
        if url:
            time.sleep(0.2)
    return out


def report_integration(entries: list[dict]) -> dict:
    total = len(entries)
    integrated = sum(1 for e in entries if e.get("integrated"))
    with_go = sum(1 for e in entries if e.get("go_terms"))
    unintegrated = total - integrated
    print(f"CDD models in InterPro            : {total}")
    print(
        f"  integrated into an InterPro entry: {integrated} ({integrated / total:.1%})"
    )
    print(
        f"  NOT integrated                   : {unintegrated} ({unintegrated / total:.1%})"
    )
    print(f"  carrying GO terms of their own   : {with_go}")
    return {"total": total, "integrated": integrated, "unintegrated": unintegrated}


def report_headroom(entries: list[dict], sample: int, sleep: float) -> None:
    """For unintegrated models: how many matched entries still lack any MF term."""
    unint = sorted(
        (e["accession"] for e in entries if not e.get("integrated")),
    )
    if not unint:
        print("No unintegrated CDD models found.", file=sys.stderr)
        return
    # Deterministic, evenly spaced sample so the result is reproducible.
    step = max(1, len(unint) // sample)
    picks = unint[::step][:sample]
    print(
        f"# deterministic sample of {len(picks)} of {len(unint)} unintegrated models\n"
    )
    print("cdd\tN_all\tN_all_mf\theadroom_all\tN_rev\tN_rev_mf\theadroom_rev")
    tot_all = tot_rev = 0
    scored = 0
    for acc in picks:
        sig = f"xref:cdd-{acc}"
        n_all = count(sig)
        n_mf = count(f"{sig} AND go:0003674")
        n_rev = count(f"{sig} AND reviewed:true")
        n_rev_mf = count(f"{sig} AND go:0003674 AND reviewed:true")
        h_all = (n_all - n_mf) if None not in (n_all, n_mf) else None
        h_rev = (n_rev - n_rev_mf) if None not in (n_rev, n_rev_mf) else None
        if h_all is not None:
            tot_all += h_all
            scored += 1
        if h_rev is not None:
            tot_rev += h_rev
        print(f"{acc}\t{n_all}\t{n_mf}\t{h_all}\t{n_rev}\t{n_rev_mf}\t{h_rev}")
        time.sleep(sleep)
    print(f"\n# models scored: {scored}")
    print(f"# headroom, Swiss-Prot (reviewed) [PRIMARY]: {tot_rev}")
    print(f"# headroom, all UniProtKB (secondary)      : {tot_all}")


def report_gain(spec: str) -> None:
    """Closure-aware gain for one model and one proposed GO term, e.g. cd21555:GO:0009055."""
    acc, _, go = spec.partition(":")
    goid = go.split(":")[-1]
    sig = f"xref:cdd-{acc}"
    n_all = count(sig)
    n_all_go = count(f"{sig} AND go:{goid}")
    n_rev = count(f"{sig} AND reviewed:true")
    n_rev_go = count(f"{sig} AND go:{goid} AND reviewed:true")
    print(f"model {acc} -> {go}")
    print(
        f"  all UniProtKB : carries={n_all} already_has_term={n_all_go} gain={n_all - n_all_go}"
    )
    print(
        f"  Swiss-Prot    : carries={n_rev} already_has_term={n_rev_go} gain={n_rev - n_rev_go}"
    )


def main(argv=None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument(
        "--integration", action="store_true", help="integration statistics only"
    )
    p.add_argument(
        "--headroom", action="store_true", help="MF headroom for unintegrated models"
    )
    p.add_argument(
        "--gain",
        metavar="cdXXXXX:GO:NNNNNNN",
        help="closure-aware gain for one model/term",
    )
    p.add_argument(
        "--sample", type=int, default=40, help="models to score for --headroom"
    )
    p.add_argument(
        "--sleep", type=float, default=0.25, help="pause between UniProt calls"
    )
    p.add_argument(
        "--limit", type=int, default=None, help="stop after N entries (testing)"
    )
    args = p.parse_args(argv)

    if args.gain:
        report_gain(args.gain)
        return 0

    if not (args.integration or args.headroom):
        p.print_help()
        return 1

    entries = fetch_entries(limit=args.limit)
    report_integration(entries)
    if args.headroom:
        print()
        report_headroom(entries, args.sample, args.sleep)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
