#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = ["pyyaml"]
# ///
"""Profile the UniProtKB members of a Pfam family before writing a curated rule on it.

``high_value_unique.py`` shortlists (family, term) pairs from reviewed members. A
rule fires on every member, reviewed or not, so before one is written this probe
shows what the whole family looks like:

* each reviewed member, with its EC numbers, whether it carries the term, and its
  other molecular functions;
* for the unreviewed members: how many already carry the term or a descendant,
  which domain architectures and lineages they fall in, and how many carry a
  different non-binding function that the term would sit beside or contradict;
* which other InterPro entries the members match, and what interpro2go gives
  through them.

``--require`` and ``--exclude`` restrict the members to those with or without
another signature (Pfam or InterPro accession), and ``--taxon`` to a lineage name,
to test a candidate condition set. A member list is the UniProt TSV stream for
``xref:pfam-<PF>``, cached under ``data/probe`` (``--download`` fetches it).

Nothing is asserted and nothing is hardcoded; the output is a description of the
family as UniProt has it on the day of the download.
"""
from __future__ import annotations

import argparse
import collections
import csv
import gzip
import re
import subprocess
import sys
from pathlib import Path

from high_value_unique import BINDING, DATA, MF_ROOT, parse_ext2go, parse_go, parse_interpro

PROBE = DATA / "probe"
FIELDS = ("accession,reviewed,protein_name,organism_name,lineage,length,ec,xref_pfam,"
          "xref_interpro,go_f,fragment,xref_panther,xref_ncbifam,xref_cdd")
GO_ID = re.compile(r"\[(GO:\d{7})\]")
RANKS = ("domain", "kingdom", "phylum", "class")


def fetch(pfam: str) -> Path:
    PROBE.mkdir(parents=True, exist_ok=True)
    dest = PROBE / f"{pfam}.tsv.gz"
    if not dest.exists():
        subprocess.run(
            ["curl", "-sS", "--fail", "--retry", "3", "-o", str(dest), "-G",
             "https://rest.uniprot.org/uniprotkb/stream",
             "--data-urlencode", f"query=xref:pfam-{pfam}",
             "--data-urlencode", f"fields={FIELDS}",
             "--data-urlencode", "format=tsv", "--data-urlencode", "compressed=true"],
            check=True)
    return dest


def lineage_at(lineage: str, rank: str) -> str:
    for part in lineage.split(", "):
        if part.endswith(f"({rank})"):
            return part.rsplit(" (", 1)[0]
    return "-"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("pfam")
    ap.add_argument("go_id", nargs="+", help="term(s) the rule would assign")
    ap.add_argument("--download", action="store_true", help="fetch the member list if missing")
    ap.add_argument("--require", action="append", default=[], help="signature the member must also match")
    ap.add_argument("--exclude", action="append", default=[], help="signature the member must not match")
    ap.add_argument("--taxon", action="append", default=[], help="lineage name the member must fall in")
    ap.add_argument("--not-taxon", action="append", default=[], help="lineage name the member must not fall in")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--list-lacking", type=int, default=0,
                    help="list this many unreviewed members that carry a different function")
    args = ap.parse_args()

    path = PROBE / f"{args.pfam}.tsv.gz"
    if args.download:
        path = fetch(args.pfam)
    if not path.exists():
        print(f"ERROR: {path} missing; re-run with --download", file=sys.stderr)
        return 2

    parents, go_name, alt, obsolete, namespace, go_version = parse_go(DATA / "go-basic.obo")
    interpro2go, i2g_version = parse_ext2go(DATA / "interpro2go.txt", "InterPro")
    _, ipr_type, ipr_name, _, interpro_release = parse_interpro(DATA / "interpro.xml.gz")

    cache: dict[str, frozenset[str]] = {}

    def closure(t: str) -> frozenset[str]:
        if t not in cache:
            seen, stack = {t}, [t]
            while stack:
                for p in parents.get(stack.pop(), ()):
                    if p not in seen:
                        seen.add(p)
                        stack.append(p)
            cache[t] = frozenset(seen)
        return cache[t]

    depth_cache = {MF_ROOT: 0}

    def depth(t: str) -> int:
        if t not in depth_cache:
            depth_cache[t] = 1 + max((depth(p) for p in parents.get(t, ())), default=-1)
        return depth_cache[t]

    tops = {t for t, ps in parents.items() if MF_ROOT in ps} - {BINDING}

    def norm(t: str) -> str | None:
        t = alt.get(t, t)
        return None if t in obsolete or t not in go_name else t

    terms = [norm(t) for t in args.go_id]
    if None in terms:
        print(f"ERROR: unknown or obsolete GO id in {args.go_id}", file=sys.stderr)
        return 2

    rows = []
    with gzip.open(path, "rt", newline="") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            sigs = set(filter(None, (r["Pfam"] + r["InterPro"] + r.get("PANTHER", "")
                                     + r.get("NCBIfam", "") + r.get("CDD", "")).split(";")))
            sigs |= {s.split(":")[0] for s in sigs}
            if any(x not in sigs for x in args.require) or any(x in sigs for x in args.exclude):
                continue
            lineage = r["Taxonomic lineage"]
            names = {p.rsplit(" (", 1)[0] for p in lineage.split(", ")}
            if any(t not in names for t in args.taxon) or any(t in names for t in args.not_taxon):
                continue
            direct = {g for g in (norm(x) for x in GO_ID.findall(r["Gene Ontology (molecular function)"])) if g}
            closed: set[str] = set()
            for g in direct:
                closed |= closure(g)
            r["_direct"], r["_closed"] = direct, closed
            r["_pfams"] = tuple(sorted(filter(None, r["Pfam"].split(";"))))
            r["_iprs"] = tuple(filter(None, r["InterPro"].split(";")))
            rows.append(r)

    def other_function(r: dict, term: str) -> str | None:
        rest = [t for t in r["_closed"] - closure(term) if t != MF_ROOT and closure(t) & tops]
        # a descendant of the term is not "another" function
        rest = [t for t in rest if term not in closure(t)]
        return max(sorted(rest), key=depth) if rest else None

    reviewed = [r for r in rows if r["Reviewed"] == "reviewed"]
    unreviewed = [r for r in rows if r["Reviewed"] != "reviewed"]
    cond = " ".join([f"+{x}" for x in args.require] + [f"-{x}" for x in args.exclude]
                    + [f"in:{x}" for x in args.taxon] + [f"notin:{x}" for x in args.not_taxon]) or "none"
    print(f"# {args.pfam}: {len(rows):,} UniProtKB members ({len(reviewed):,} reviewed, "
          f"{len(unreviewed):,} unreviewed); extra conditions: {cond}")
    print(f"InterPro {interpro_release}; {i2g_version}; GO {go_version}; member list {path.name}\n")

    for term in terms:
        print(f"## {term} {go_name[term]}\n")
        print("### Reviewed members\n")
        print("| accession | organism | length | EC | has term | other non-binding function | Pfam |")
        print("|---|---|---:|---|---|---|---|")
        for r in sorted(reviewed, key=lambda r: (term not in r["_closed"], r["Organism"])):
            other = other_function(r, term)
            print(f"| {r['Entry']} | {r['Organism'][:40]} | {r['Length']} | {r['EC number']} | "
                  f"{'yes' if term in r['_closed'] else 'NO'} | {go_name[other] if other else ''} | "
                  f"{' '.join(r['_pfams'])} |")
        n = len(unreviewed)
        have = [r for r in unreviewed if term in r["_closed"]]
        lack = [r for r in unreviewed if term not in r["_closed"]]
        differ = [(r, other_function(r, term)) for r in lack]
        differ = [(r, o) for r, o in differ if o]
        ancestors = closure(term) - {term, MF_ROOT}
        general = sum(1 for r in lack if r["_closed"] & ancestors)
        print(f"\n### Unreviewed members: {n:,}\n")
        if n:
            print(f"- carry the term or a descendant: {len(have):,} ({100 * len(have) / n:.1f}%)")
            print(f"- lack it: {len(lack):,}; of those, carry a non-root ancestor: {general:,}; "
                  f"carry a different non-binding function: {len(differ):,}; "
                  f"fragments: {sum(1 for r in lack if r['Fragment'])}")
            fn = collections.Counter(go_name[o] for _, o in differ)
            print("- most common different functions among those lacking the term: "
                  + "; ".join(f"{k} ({v:,})" for k, v in fn.most_common(args.top)))
            for r, o in differ[: args.list_lacking]:
                print(f"  - {r['Entry']} {r['Protein names'][:60]} | {r['Organism'][:35]} | {go_name[o]} | "
                      f"{' '.join(r['_pfams'])}")
        print()

    def breakdown(title: str, counter: collections.Counter, total: int, label=lambda k: k) -> None:
        print(f"### {title}\n")
        for k, v in counter.most_common(args.top):
            print(f"- {v:,} ({100 * v / total:.1f}%) {label(k)}")
        if len(counter) > args.top:
            print(f"- … {len(counter) - args.top:,} more")
        print()

    if unreviewed:
        n = len(unreviewed)
        for rank in RANKS:
            breakdown(f"Unreviewed by {rank}",
                      collections.Counter(lineage_at(r["Taxonomic lineage"], rank) for r in unreviewed), n)
        breakdown("Unreviewed by Pfam architecture (set of families)",
                  collections.Counter(r["_pfams"] for r in unreviewed), n, lambda k: " ".join(k))
        breakdown("Pfam families co-occurring",
                  collections.Counter(p for r in unreviewed for p in set(r["_pfams"]) - {args.pfam}), n)
        ipr = collections.Counter(i for r in unreviewed for i in r["_iprs"])

        def ipr_label(k: str) -> str:
            mf = sorted(go_name.get(alt.get(g, g), g) for g in interpro2go.get(k, ())
                        if namespace.get(alt.get(g, g)) == "molecular_function")
            return f"{k} {ipr_name.get(k, '')} [{ipr_type.get(k, '?')}] -> {'; '.join(mf) or 'no MF term'}"

        breakdown("InterPro entries matched, with their interpro2go molecular-function terms", ipr, n, ipr_label)
        breakdown("Protein names",
                  collections.Counter(re.sub(r" \(.*", "", r["Protein names"]) for r in unreviewed), n)
        lengths = sorted(int(r["Length"]) for r in unreviewed)
        print(f"Length: median {lengths[len(lengths) // 2]}, 5th-95th percentile "
              f"{lengths[len(lengths) // 20]}-{lengths[-len(lengths) // 20 - 1]}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
