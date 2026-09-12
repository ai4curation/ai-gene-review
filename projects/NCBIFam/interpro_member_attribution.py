#!/usr/bin/env python3
"""Re-join the repo's InterPro2GO (GO_REF:0000002) annotations to InterPro member DBs.

In GOA, an InterPro2GO annotation's WITH/FROM names only the integrated
``InterPro:IPRnnnnnn`` entry -- the underlying member-database signature (NCBIFAM,
CDD, Pfam, ...) is **masked** (see ../NCBIFam.md). This script recovers that
attribution: for every GO_REF:0000002 row in this repo's ``genes/**/*-goa.tsv``, it
looks up the cited InterPro entry's ``member_databases`` via the InterPro API and asks
*which member databases could have produced the annotation* -- in particular how often
NCBIFAM or CDD contributes, and how often it is the **sole** integrated signature
(the strongest attribution).

The per-entry API responses are cached (``--cache``, default under ``/tmp``) so the run
is resumable: re-running continues from the cache and only fetches missing entries.

Data (live, no auth):
  * InterPro entry detail: https://www.ebi.ac.uk/interpro/api/entry/interpro/<IPR>

Usage::

    uv run python interpro_member_attribution.py            # fetch (resumable) + report
    uv run python interpro_member_attribution.py --report-only   # report from cache only
"""

from __future__ import annotations

import argparse
import json
import time
import urllib.request
from collections import Counter
from pathlib import Path

API = "https://www.ebi.ac.uk/interpro/api/entry/interpro/{}"
UA = "ai-gene-review-ncbifam/1.0"
REPO = Path(__file__).resolve().parents[2]


def iter_goref2_rows() -> list[tuple[str, str]]:
    """(InterPro id, GO id) for every GO_REF:0000002 annotation in the repo's goa files."""
    out: list[tuple[str, str]] = []
    for goa in REPO.glob("genes/**/*-goa.tsv"):
        for line in goa.read_text("utf-8", "replace").splitlines():
            c = line.split("\t")
            if len(c) < 11 or c[9] != "GO_REF:0000002":
                continue
            iprs = [w.split(":", 1)[1] for w in c[10].split("|") if w.startswith("InterPro:IPR")]
            go = c[4]
            for ipr in iprs:
                out.append((ipr, go))
    return out


def load_cache(path: Path) -> dict[str, list[str]]:
    return json.loads(path.read_text()) if path.exists() else {}


def fetch_member_dbs(ipr: str) -> list[str] | None:
    """Member-database keys integrated into an InterPro entry (None on fetch failure)."""
    req = urllib.request.Request(API.format(ipr), headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:  # noqa: S310
            md = json.load(resp)["metadata"].get("member_databases") or {}
            return sorted(md.keys())
    except Exception:  # pragma: no cover - network dependent
        return None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--cache", type=Path, default=Path("/tmp/interpro_member_dbs.json"))
    ap.add_argument("--report-only", action="store_true")
    ap.add_argument("--sleep", type=float, default=0.1)
    args = ap.parse_args(argv)

    rows = iter_goref2_rows()
    distinct = sorted({ipr for ipr, _ in rows})
    cache = load_cache(args.cache)

    if not args.report_only:
        missing = [i for i in distinct if i not in cache]
        for n, ipr in enumerate(missing, 1):
            mds = fetch_member_dbs(ipr)
            if mds is not None:
                cache[ipr] = mds
            if n % 100 == 0 or n == len(missing):
                args.cache.write_text(json.dumps(cache))
                print(f"  fetched {n}/{len(missing)} (cache={len(cache)})")
            time.sleep(args.sleep)
        args.cache.write_text(json.dumps(cache))

    # ---- report ----
    resolved = {i: cache[i] for i in distinct if i in cache}
    entry_db = Counter()           # distinct InterPro entries containing each member DB
    for mds in resolved.values():
        for db in mds:
            entry_db[db] += 1

    row_db = Counter()             # annotation rows whose entry contains each member DB
    rows_ncbifam_sole = rows_cdd_sole = 0
    rows_resolved = 0
    for ipr, _go in rows:
        mds = resolved.get(ipr)
        if mds is None:
            continue
        rows_resolved += 1
        for db in mds:
            row_db[db] += 1
        if mds == ["ncbifam"]:
            rows_ncbifam_sole += 1
        if mds == ["cdd"]:
            rows_cdd_sole += 1

    print("\n=== InterPro2GO (GO_REF:0000002) member-database attribution, repo gene set ===")
    print(f"annotation rows                : {len(rows)}  (resolved to a cached entry: {rows_resolved})")
    print(f"distinct InterPro entries      : {len(distinct)}  (resolved: {len(resolved)})")

    print("\n-- distinct InterPro entries containing each member DB --")
    for db, c in entry_db.most_common():
        print(f"  {db:14} {c:5}  ({100 * c / len(resolved):.0f}% of resolved entries)")

    print("\n-- annotation rows whose InterPro entry integrates each member DB --")
    for db, c in row_db.most_common():
        print(f"  {db:14} {c:5}  ({100 * c / rows_resolved:.0f}% of resolved rows)")

    print("\n-- sole-signature attribution (entry's ONLY member DB) --")
    print(f"  NCBIFAM is the sole integrated signature: {rows_ncbifam_sole} rows")
    print(f"  CDD is the sole integrated signature    : {rows_cdd_sole} rows")
    ncbifam_rows = row_db.get("ncbifam", 0)
    cdd_rows = row_db.get("cdd", 0)
    print(
        f"\nHeadline: NCBIFAM contributes a signature to {ncbifam_rows} and CDD to {cdd_rows} of "
        f"{rows_resolved} resolved GO_REF:0000002 rows -- a contribution entirely INVISIBLE in GOA, "
        f"which shows only the InterPro id."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
