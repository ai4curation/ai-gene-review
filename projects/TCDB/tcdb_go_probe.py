#!/usr/bin/env python3
"""Characterise the TCDB -> GO relationship, in both directions.

Unlike RHEA (``rhea2go``) or EC (``ec2go``), **TCDB has no external2go mapping**
in the GO release (see ``TCDB-METHODOLOGY.md``). TCDB does publish its own
GO associations at ``https://tcdb.org/cgi-bin/projectv/public/go.py`` -- a flat
``GO-id <TAB> TC-number <TAB> family-name`` dump -- but that dump is an
aggregation of member-protein annotations across all three GO aspects, not a
curated tc2go pipeline, so it is noisy (integral-component-of-membrane,
protein binding, catalytic activity on channels ...).

This probe computes, all live / reproducible:

  --tcdb-go   characterise the go.py dump (rows, distinct GO ids, distinct TC
              numbers/families, aspect skew via the transporter-activity MF
              closure, generic-term noise).
  --gap       reverse gap: of reviewed Swiss-Prot entries carrying a TCDB
              cross-reference, how many carry NO GO transporter-activity term
              (``go:0005215`` closure) at all -- the "falls through the cracks"
              signal, here structural because there is no pipeline.

Nothing is hard-coded; every number is fetched from the live source. Missing
network access => the script reports what it could not fetch rather than
inventing a value.

Usage::

    uv run python tcdb_go_probe.py --tcdb-go
    uv run python tcdb_go_probe.py --gap
    uv run python tcdb_go_probe.py --all
"""
from __future__ import annotations

import argparse
import collections
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

TCDB_GO_URL = "https://tcdb.org/cgi-bin/projectv/public/go.py"
QUICKGO_DESC = (
    "https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/{go}/descendants?relations=is_a"
)
UNIPROT_SEARCH = "https://rest.uniprot.org/uniprotkb/search"
# GO roots whose is_a closure defines a "transporter activity" molecular function.
TRANSPORTER_MF_ROOTS = ["GO:0022857", "GO:0005215"]
DATA = Path(__file__).resolve().parent / "data"
CACHE_TCDB_GO = DATA / "tcdb_go.tsv"


def _get(url: str, accept: str = "text/plain", timeout: int = 90) -> str:
    req = urllib.request.Request(url, headers={"Accept": accept, "User-Agent": "ai-gene-review-tcdb-probe"})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 (trusted URLs)
        return r.read().decode("utf-8", "replace")


def _uniprot_count(query: str) -> int | None:
    """Return X-Total-Results for a UniProt query, or None if unreachable."""
    url = f"{UNIPROT_SEARCH}?" + urllib.parse.urlencode({"query": query, "format": "list", "size": 0})
    req = urllib.request.Request(url, headers={"Accept": "text/plain"})
    try:
        with urllib.request.urlopen(req, timeout=90) as r:  # noqa: S310
            val = r.headers.get("X-Total-Results")
            return int(val) if val is not None else None
    except Exception as e:  # noqa: BLE001 (external system)
        print(f"  ! UniProt query failed ({query!r}): {e}", file=sys.stderr)
        return None


def load_tcdb_go(refresh: bool = False) -> list[tuple[str, str, str]]:
    """Return [(go_id, tc_number, family_name)] from go.py, caching to data/."""
    if refresh or not CACHE_TCDB_GO.exists():
        DATA.mkdir(exist_ok=True)
        CACHE_TCDB_GO.write_text(_get(TCDB_GO_URL))
        print(f"# fetched go.py -> {CACHE_TCDB_GO}")
    rows: list[tuple[str, str, str]] = []
    for line in CACHE_TCDB_GO.read_text().splitlines():
        parts = line.rstrip("\n").split("\t")
        if len(parts) >= 2 and parts[0].startswith("GO:"):
            rows.append((parts[0].strip(), parts[1].strip(), parts[2].strip() if len(parts) > 2 else ""))
    return rows


def transporter_mf_closure() -> set[str]:
    """is_a closure (descendants + self) of the transporter-activity MF roots, via QuickGO."""
    closure: set[str] = set()
    for root in TRANSPORTER_MF_ROOTS:
        data = json.loads(_get(QUICKGO_DESC.format(go=root), accept="application/json"))
        for res in data.get("results", []):
            closure.add(res["id"])
            for d in res.get("descendants") or []:
                closure.add(d)
    return closure


def cmd_tcdb_go(_args: argparse.Namespace) -> None:
    rows = load_tcdb_go()
    gos = collections.Counter(r[0] for r in rows)
    tcs = {r[1] for r in rows}
    fams = {".".join(r[1].split(".")[:3]) for r in rows}
    print("== TCDB go.py dump ==")
    print(f"rows                        : {len(rows)}")
    print(f"distinct GO ids             : {len(gos)}")
    print(f"distinct TC numbers (5-lvl) : {len(tcs)}")
    print(f"distinct TC families (3-lvl): {len(fams)}")
    by_class = collections.Counter(r[1].split(".")[0] for r in rows)
    print("rows by TC class            : " + ", ".join(f"{k}={v}" for k, v in sorted(by_class.items())))

    print("\n-- classifying by transporter-activity MF closure (QuickGO) --")
    mf = transporter_mf_closure()
    print(f"transporter-activity MF closure size: {len(mf)}")
    gos_mf = {g for g in gos if g in mf}
    rows_mf = [r for r in rows if r[0] in mf]
    tc_mf = {r[1] for r in rows_mf}
    fam_mf = {".".join(t.split(".")[:3]) for t in tc_mf}
    n = len(rows)
    print(f"distinct GO ids that are transporter-activity MF : {len(gos_mf)}/{len(gos)} ({100*len(gos_mf)//len(gos)}%)")
    print(f"rows whose GO is transporter-activity MF         : {len(rows_mf)}/{n} ({100*len(rows_mf)//n}%)")
    print(f"TC numbers with >=1 transporter-activity MF term : {len(tc_mf)}/{len(tcs)} ({100*len(tc_mf)//len(tcs)}%)")
    print(f"TC families with >=1 transporter-activity MF term: {len(fam_mf)}/{len(fams)} ({100*len(fam_mf)//len(fams)}%)")

    print("\n-- most frequent GO terms (dominated by CC/BP, not MF activity) --")
    for g, c in gos.most_common(12):
        tag = "MF-transport" if g in mf else ""
        print(f"  {g}\t{c}\t{tag}")
    for noisy, lab in [("GO:0005515", "protein binding"), ("GO:0005488", "binding"),
                       ("GO:0003824", "catalytic activity"), ("GO:0008152", "metabolic process")]:
        print(f"  noise: {noisy} {lab}: {gos.get(noisy, 0)} rows")


def cmd_gap(_args: argparse.Namespace) -> None:
    print("== Reverse gap: reviewed Swiss-Prot entries carrying a TCDB xref ==")
    total = _uniprot_count("(database:tcdb) AND (reviewed:true)")
    all_kb = _uniprot_count("(database:tcdb)")
    with_tta = _uniprot_count("(database:tcdb) AND (reviewed:true) AND (go:0022857)")
    with_ta = _uniprot_count("(database:tcdb) AND (reviewed:true) AND (go:0005215)")
    without = _uniprot_count("(database:tcdb) AND (reviewed:true) NOT (go:0005215)")
    print(f"reviewed with TCDB xref               : {total}")
    print(f"all UniProtKB with TCDB xref          : {all_kb}")
    print(f"  ...with GO:0022857 (transmembrane)  : {with_tta}")
    print(f"  ...with GO:0005215 (transporter act): {with_ta}")
    print(f"  ...with NO transporter-activity term: {without}")
    if total and without is not None:
        print(f"\n>>> gap: {without}/{total} = {100*without/total:.1f}% of reviewed TCDB entries "
              "carry no GO transporter-activity term (upper bound; closure over GO:0005215).")
    print("\nNote: UniProt 'go:<id>' expands to descendants, so these counts are already "
          "ontology-closure filtered on the GO side.")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tcdb-go", action="store_true", help="characterise the go.py TCDB->GO dump")
    ap.add_argument("--gap", action="store_true", help="reverse gap via UniProt REST")
    ap.add_argument("--all", action="store_true", help="run everything")
    args = ap.parse_args(argv)
    if not (args.tcdb_go or args.gap or args.all):
        ap.print_help()
        return 1
    if args.tcdb_go or args.all:
        cmd_tcdb_go(args)
    if args.gap or args.all:
        print()
        cmd_gap(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
