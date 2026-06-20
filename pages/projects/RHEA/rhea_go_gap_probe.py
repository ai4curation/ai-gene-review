#!/usr/bin/env python3
"""Probe the RHEA -> GO contribution and gap-propagation question.

This script supports the RHEA project (see ../RHEA.md). It answers two
questions with *live, reproducible* data and no hardcoded results:

1. CONTRIBUTION (forward): characterise the public ``rhea2go`` mapping that
   GOA uses to turn UniProt catalytic-activity (RHEA) assignments into GO
   molecular-function annotations (these land in GOA as ``GO_REF:0000116``,
   ``assigned_by=RHEA``, aspect F, evidence IEA).

2. GAP (reverse): for a set of RHEA reactions, ask how many UniProtKB
   entries carry the reaction as a catalytic activity but do *not* carry the
   GO molecular-function term that ``rhea2go`` maps that reaction to -- i.e.
   annotations that "fall through the cracks" and never propagate to GO.

IMPORTANT CAVEAT (read before trusting the gap numbers): the gap probe is an
EXACT-term match. An entry counted as "missing GO:X" may legitimately carry a
*more specific child* of GO:X instead (e.g. a specific receptor tyrosine
kinase term rather than the generic ``protein tyrosine kinase activity``).
A true over/under-propagation audit must therefore be CLOSURE-aware (subtract
entries that carry any descendant of the mapped term), exactly as the SPKW and
UNIPATHWAY projects do. The raw exact-match gap is an UPPER BOUND on the real
gap; treat high-gap reactions as *candidates* for closure-aware review, not as
confirmed gaps. The ``--ancestor-go`` style closure check needs an ontology
closure table (the go-db DuckDBs) which is not bundled here.

Usage:
    uv run python rhea_go_gap_probe.py --stats
    uv run python rhea_go_gap_probe.py --gap RHEA:10596 RHEA:21248
    uv run python rhea_go_gap_probe.py --gap-sample   # the pilot set

Requires only the Python standard library plus network access to
current.geneontology.org and rest.uniprot.org.
"""
from __future__ import annotations

import argparse
import re
import sys
import time
import urllib.parse
import urllib.request

RHEA2GO_URL = "https://current.geneontology.org/ontology/external2go/rhea2go"
UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/search"

# Pilot set used in RHEA.md: a spread of common/rare reactions across enzyme
# classes (kinase, ATPase, lyase, polymerase, ligase, decarboxylase,
# phosphatase) plus one reaction that has no rhea2go mapping at all.
PILOT_RHEA = [
    "RHEA:10596",  # protein tyrosine kinase activity      (GO:0004713)
    "RHEA:13065",  # ATP hydrolysis activity               (GO:0016887)
    "RHEA:16505",  # chorismate lyase activity             (GO:0008813)
    "RHEA:21248",  # 5'-3' RNA polymerase activity         (GO:0034062)
    "RHEA:15421",  # long-chain fatty acid-CoA ligase      (GO:0004467)
    "RHEA:11628",  # pyruvate decarboxylase activity       (GO:0004737)
    "RHEA:22636",  # dCTP diphosphatase activity           (GO:0047840)
    "RHEA:46608",  # (no rhea2go mapping -> "no GO term" gap class)
]

_LINE = re.compile(r"RHEA:(\d+) > GO:(.+) ; (GO:\d+)")


def load_rhea2go() -> dict[str, tuple[str, str]]:
    """Return {rhea_id: (go_id, go_label)} from the public rhea2go mapping."""
    with urllib.request.urlopen(RHEA2GO_URL, timeout=60) as resp:
        text = resp.read().decode()
    mapping: dict[str, tuple[str, str]] = {}
    for line in text.splitlines():
        if line.startswith("!"):
            continue
        m = _LINE.match(line)
        if m:
            mapping[m.group(1)] = (m.group(3), m.group(2))
    return mapping


def print_stats(mapping: dict[str, tuple[str, str]]) -> None:
    rheas = set(mapping)
    gos = {go for go, _ in mapping.values()}
    print("rhea2go mapping characterisation")
    print(f"  RHEA->GO mapping rows : {len(mapping)}")
    print(f"  distinct RHEA reactions: {len(rheas)}")
    print(f"  distinct GO terms      : {len(gos)}")
    print(f"  mean reactions per GO  : {len(rheas) / len(gos):.2f}")


def _norm(rhea: str) -> str:
    return rhea.split(":", 1)[1] if rhea.upper().startswith("RHEA:") else rhea


def uniprot_entries_for_rhea(rhea_num: str, size: int = 500, reviewed: bool = True):
    """Yield (accession, set_of_go_ids) for UniProtKB entries with this RHEA."""
    query = f"rhea:{rhea_num}"
    if reviewed:
        query += " AND reviewed:true"
    params = urllib.parse.urlencode(
        {"query": query, "fields": "accession,go_id", "format": "tsv", "size": size}
    )
    with urllib.request.urlopen(f"{UNIPROT_URL}?{params}", timeout=60) as resp:
        text = resp.read().decode()
    for row in text.splitlines()[1:]:
        if not row.strip():
            continue
        parts = row.split("\t")
        acc = parts[0]
        gids = set(parts[1].split("; ")) if len(parts) > 1 and parts[1] else set()
        yield acc, gids


def gap_probe(mapping, rhea_ids, size=500, sleep=1.0) -> None:
    print("RHEA\tGO\tGO_label\tN_reviewed\tN_missing_exact\tpct_missing\tnote")
    for rhea in rhea_ids:
        num = _norm(rhea)
        mapped = mapping.get(num)
        if mapped is None:
            print(f"RHEA:{num}\t-\t-\t-\t-\t-\tNO_rhea2go_mapping")
            continue
        go_id, go_label = mapped
        try:
            entries = list(uniprot_entries_for_rhea(num, size=size))
        except Exception as exc:  # network / API hiccup -> report, don't fake
            print(f"RHEA:{num}\t{go_id}\t{go_label}\tERR\t-\t-\t{exc}")
            continue
        n = len(entries)
        missing = sum(1 for _, gids in entries if go_id not in gids)
        pct = f"{100 * missing / n:.0f}%" if n else "-"
        note = "capped_at_size" if n == size else ""
        print(f"RHEA:{num}\t{go_id}\t{go_label}\t{n}\t{missing}\t{pct}\t{note}")
        time.sleep(sleep)


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stats", action="store_true", help="characterise rhea2go")
    p.add_argument("--gap", nargs="+", metavar="RHEA", help="gap-probe these RHEA ids")
    p.add_argument("--gap-sample", action="store_true", help="gap-probe the pilot set")
    p.add_argument("--size", type=int, default=500, help="UniProt page size cap")
    args = p.parse_args(argv)

    if not (args.stats or args.gap or args.gap_sample):
        p.print_help()
        return 1

    mapping = load_rhea2go()
    if args.stats:
        print_stats(mapping)
    if args.gap:
        gap_probe(mapping, args.gap, size=args.size)
    if args.gap_sample:
        gap_probe(mapping, PILOT_RHEA, size=args.size)
    return 0


if __name__ == "__main__":
    sys.exit(main())
