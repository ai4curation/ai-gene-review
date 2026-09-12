#!/usr/bin/env python3
"""Characterise the NCBIFAM / CDD -> GO contribution and coverage gap.

This is the NCBIFam project's reproducible probe, in the spirit of the RHEA
project's ``rhea_go_gap_probe.py``. It computes, live, the numbers cited in
``../NCBIFam.md`` so the scoping claims are reproducible rather than asserted.

NCBIFAM and CDD are InterPro *member databases*: they reach GOA only through
InterPro integration (``interpro2go`` -> ``GO_REF:0000002``). There is no public
``ncbifam2go`` / ``cdd2go`` external2go file. NCBIFAM, however, ships its *own*
NCBI-curated GO/EC assignments in the PGAP HMM metadata, which GO does not
ingest -- the basis for a curated ``ncbifam2go`` gap-fill mapping.

Data sources (all live, no auth):
  * NCBIFAM HMM metadata : https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv
  * InterPro member counts: https://www.ebi.ac.uk/interpro/api/entry/{db}/
  * interpro2go           : https://current.geneontology.org/ontology/external2go/interpro2go

Usage::

    uv run python ncbifam_cdd_probe.py --stats          # all summary stats
    uv run python ncbifam_cdd_probe.py --ncbifam-go      # NCBIFAM GO/EC coverage only
    uv run python ncbifam_cdd_probe.py --interpro-coverage

No third-party dependencies (urllib only); a network connection is required.
"""

from __future__ import annotations

import argparse
import sys
import urllib.request
from typing import Optional

HMM_PGAP_URL = "https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv"
INTERPRO_API = "https://www.ebi.ac.uk/interpro/api"
INTERPRO2GO_URL = "https://current.geneontology.org/ontology/external2go/interpro2go"

# Column indices in hmm_PGAP.tsv (0-based), as of the 2026 release.
COL_ACCESSION = 0
COL_LABEL = 2
COL_FAMILY_TYPE = 6
COL_PRODUCT_NAME = 10
COL_EC = 13
COL_GO = 14


def _get(url: str, timeout: int = 90) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "ncbifam-cdd-probe/1.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:  # noqa: S310 (trusted hosts)
        return resp.read()


def _interpro_count(path: str) -> Optional[int]:
    """Return the ``count`` field of an InterPro entry-list endpoint."""
    try:
        import json

        data = json.loads(_get(f"{INTERPRO_API}/{path}?page_size=1"))
        return int(data.get("count")) if "count" in data else None
    except Exception as exc:  # pragma: no cover - network dependent
        print(f"  ! {path}: {exc}", file=sys.stderr)
        return None


def ncbifam_go_stats() -> None:
    """NCBI-curated GO/EC coverage of the NCBIFAM HMM collection."""
    print("== NCBIFAM PGAP HMM metadata (NCBI-native GO/EC) ==")
    raw = _get(HMM_PGAP_URL).decode("utf-8", "replace").splitlines()
    rows = [line.split("\t") for line in raw[1:] if line]
    n = len(rows)

    def has(col: int) -> int:
        return sum(1 for r in rows if len(r) > col and r[col].strip())

    n_go = has(COL_GO)
    n_ec = has(COL_EC)

    # GO terms are space/comma separated; count distinct.
    go_terms: set[str] = set()
    for r in rows:
        if len(r) > COL_GO and r[COL_GO].strip():
            for tok in r[COL_GO].replace(",", " ").split():
                if tok.startswith("GO:"):
                    go_terms.add(tok)

    fam_types: dict[str, int] = {}
    for r in rows:
        if len(r) > COL_FAMILY_TYPE:
            fam_types[r[COL_FAMILY_TYPE]] = fam_types.get(r[COL_FAMILY_TYPE], 0) + 1

    print(f"  models total            : {n}")
    print(f"  models with GO term(s)  : {n_go} ({100 * n_go / n:.0f}%)")
    print(f"  models with EC number(s): {n_ec} ({100 * n_ec / n:.0f}%)")
    print(f"  distinct GO terms used  : {len(go_terms)}")
    print("  family_type (top 6, 'equivalog' = 1:1 function transfer):")
    for ft, c in sorted(fam_types.items(), key=lambda kv: -kv[1])[:6]:
        print(f"    {ft or '(blank)':<22} {c}")


def interpro_coverage() -> None:
    """Integration status of NCBIFAM / CDD signatures in InterPro."""
    print("== InterPro member-database integration (route to GO) ==")
    for db in ("ncbifam", "cdd"):
        total = _interpro_count(f"entry/{db}/")
        integ = _interpro_count(f"entry/integrated/{db}/")
        unint = _interpro_count(f"entry/unintegrated/{db}/")
        if None in (total, integ, unint):
            print(f"  {db}: incomplete (network)")
            continue
        pct = 100 * integ / total if total else 0
        print(
            f"  {db:<8} total={total:>6}  integrated={integ:>6} ({pct:.0f}%)"
            f"  unintegrated={unint:>6}  <- cannot reach GO via interpro2go"
        )


def interpro2go_stats() -> None:
    print("== interpro2go (the only GOA route, GO_REF:0000002) ==")
    text = _get(INTERPRO2GO_URL).decode("utf-8", "replace").splitlines()
    rows = [ln for ln in text if ln.startswith("InterPro:")]
    ipr = {ln.split()[0] for ln in rows}
    version = next((ln for ln in text if ln.startswith("!version")), "")
    print(f"  {version.strip()}")
    print(f"  mapping rows          : {len(rows)}")
    print(f"  distinct InterPro ids : {len(ipr)}")
    print("  (NCBIFAM/CDD GO is delivered only where their signature is")
    print("   integrated into one of these InterPro entries.)")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stats", action="store_true", help="run all sections")
    ap.add_argument("--ncbifam-go", action="store_true")
    ap.add_argument("--interpro-coverage", action="store_true")
    ap.add_argument("--interpro2go", action="store_true")
    args = ap.parse_args()

    run_all = args.stats or not any(
        (args.ncbifam_go, args.interpro_coverage, args.interpro2go)
    )

    if run_all or args.ncbifam_go:
        ncbifam_go_stats()
        print()
    if run_all or args.interpro_coverage:
        interpro_coverage()
        print()
    if run_all or args.interpro2go:
        interpro2go_stats()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
