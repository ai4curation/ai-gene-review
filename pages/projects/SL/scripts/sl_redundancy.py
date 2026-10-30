#!/usr/bin/env python3
"""Test whether SL-unique over-annotation is explained by redundancy.

The SL project's headline claim is that the ``GO_REF:0000044`` pipeline fails on
**granularity** rather than truth: an under-specified UniProt subcellular
location maps to a GO term that is true but uninformative. If that is right,
the broad SL-unique annotations that reviewers flag should be exactly the ones
where the gene *already carries a more specific term from another source* — the
SL annotation adds nothing.

This script tests that directly. For each SL-unique annotation of a gene to term
T, it asks whether any other GO cellular-component term on that gene (from any
reference) is a proper descendant of T under ``is_a``/``part_of``. It then
cross-tabulates that answer against the reviewer's action.

    uv run python projects/SL/scripts/sl_redundancy.py
    uv run python projects/SL/scripts/sl_redundancy.py --sl SL-0162 --detail

Requires the local GO SQLite build (OAK ``sqlite:obo:go``); the first run
downloads it. Takes ~6 minutes over the full ``genes/`` tree.
"""

from __future__ import annotations

import argparse
import collections
import glob
import re
from pathlib import Path

SL_REF = "GO_REF:0000044"
SUBCELL_PREFIX = "UniProtKB-SubCell:"
ISSUE_ACTIONS = ("REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY")
CLOSURE_PREDICATES = ["rdfs:subClassOf", "BFO:0000050"]

ANNOTATION_RE = re.compile(r"^\s*- term:\n\s+id: (GO:\d+)\n(.*?)(?=^\s*- term:|\Z)", re.S | re.M)
ACTION_RE = re.compile(r"\n\s+action: ([A-Z_]+)")


def load_gene_annotations(root: Path):
    """Return per-gene CC terms and the SL-unique subset.

    Yields ``(species, gene, all_cc_terms, sl_unique)`` where ``sl_unique`` maps
    a term to ``(name, sl_id)``.
    """
    for path in sorted(glob.glob(str(root / "genes" / "*" / "*" / "*-goa.tsv"))):
        parts = Path(path).parts
        species, gene = parts[-3], parts[-2]
        lines = Path(path).read_text(errors="ignore").splitlines()
        if len(lines) < 2:
            continue
        header = lines[0].split("\t")
        try:
            i_term = header.index("GO TERM")
            i_name = header.index("GO NAME")
            i_aspect = header.index("GO ASPECT")
            i_ref = header.index("REFERENCE")
            i_with = header.index("WITH/FROM")
        except ValueError:
            continue

        by_term: dict = collections.defaultdict(list)
        for line in lines[1:]:
            cols = line.split("\t")
            if len(cols) <= max(i_term, i_name, i_aspect, i_ref, i_with):
                continue
            if not cols[i_aspect].startswith(("cellular_component", "C")):
                continue
            by_term[(cols[i_term], cols[i_name])].append((cols[i_ref], cols[i_with]))

        all_cc = {term for term, _ in by_term}
        sl_unique = {}
        for (term, name), evidence in by_term.items():
            if {ref for ref, _ in evidence} != {SL_REF}:
                continue
            sls = sorted(
                {
                    p
                    for _, w in evidence
                    for p in w.split("|")
                    if p.startswith(SUBCELL_PREFIX)
                }
            )
            sl_unique[term] = (name, sls[0].replace(SUBCELL_PREFIX, "") if sls else "")
        if sl_unique:
            yield species, gene, all_cc, sl_unique


def load_actions(root: Path, species: str, gene: str, terms: set[str]) -> dict[str, str]:
    path = root / "genes" / species / gene / f"{gene}-ai-review.yaml"
    if not path.exists():
        return {}
    text = path.read_text(errors="ignore")
    start = text.find("\nexisting_annotations:")
    if start < 0:
        return {}
    end = text.find("\ncore_functions:", start)
    body = text[start : end if end > 0 else len(text)]
    out = {}
    for match in ANNOTATION_RE.finditer(body):
        term = match.group(1)
        if term not in terms or SL_REF not in match.group(2):
            continue
        action = ACTION_RE.search(match.group(2))
        out[term] = action.group(1) if action else "NONE"
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--sl", help="Restrict to one SL identifier, e.g. SL-0162.")
    parser.add_argument("--detail", action="store_true", help="List every annotation.")
    parser.add_argument("--min-n", type=int, default=10)
    args = parser.parse_args()

    from oaklib import get_adapter

    adapter = get_adapter("sqlite:obo:go")
    descendant_cache: dict[str, set[str]] = {}

    def descendants(term: str) -> set[str]:
        if term not in descendant_cache:
            descendant_cache[term] = set(
                adapter.descendants([term], predicates=CLOSURE_PREDICATES)
            ) - {term}
        return descendant_cache[term]

    rows = []
    for species, gene, all_cc, sl_unique in load_gene_annotations(args.root):
        actions = load_actions(args.root, species, gene, set(sl_unique))
        for term, (name, sl) in sl_unique.items():
            if args.sl and sl != args.sl:
                continue
            more_specific = sorted((all_cc - {term}) & descendants(term))
            rows.append(
                {
                    "species": species,
                    "gene": gene,
                    "term": term,
                    "name": name,
                    "sl": sl,
                    "redundant": bool(more_specific),
                    "covered_by": more_specific,
                    "action": actions.get(term),
                }
            )

    reviewed = [r for r in rows if r["action"]]
    print(f"## Redundancy of SL-unique annotations\n")
    print(f"- SL-unique annotations examined: **{len(rows)}**")
    print(f"- with a review action: **{len(reviewed)}**")
    red = [r for r in reviewed if r["redundant"]]
    print(
        f"- of those, the gene already carries a more specific CC term from another source: "
        f"**{len(red)}/{len(reviewed)} ({100 * len(red) / max(1, len(reviewed)):.0f}%)**"
    )

    def rate(subset):
        if not subset:
            return "n/a"
        issues = sum(1 for r in subset if r["action"] in ISSUE_ACTIONS)
        return f"{issues}/{len(subset)} ({100 * issues / len(subset):.0f}%)"

    print(f"\n### Issue rate, split by redundancy\n")
    print("| Group | n | Issue rate | KEEP_AS_NON_CORE |")
    print("|---|---|---|---|")
    for label, subset in (
        ("Redundant (more specific term present)", red),
        ("Not redundant (SL term is the most specific)", [r for r in reviewed if not r["redundant"]]),
    ):
        knc = sum(1 for r in subset if r["action"] == "KEEP_AS_NON_CORE")
        pct = f"{100 * knc / len(subset):.0f}%" if subset else "n/a"
        print(f"| {label} | {len(subset)} | {rate(subset)} | {knc} ({pct}) |")

    by_sl: dict = collections.defaultdict(list)
    for r in reviewed:
        by_sl[(r["sl"], r["name"])].append(r)
    print(f"\n### By SL location (>= {args.min_n} reviewed)\n")
    print("| SL | GO term | n | Redundant | Issue rate | Issue rate if redundant | if not |")
    print("|---|---|---|---|---|---|---|")
    for (sl, name), subset in sorted(by_sl.items(), key=lambda kv: -len(kv[1])):
        if len(subset) < args.min_n:
            continue
        rsub = [r for r in subset if r["redundant"]]
        nsub = [r for r in subset if not r["redundant"]]
        print(
            f"| {sl} | {name} | {len(subset)} | {len(rsub)} "
            f"({100 * len(rsub) / len(subset):.0f}%) | {rate(subset)} | {rate(rsub)} | {rate(nsub)} |"
        )

    if args.detail:
        print("\n### Detail\n")
        print("| Species | Gene | Term | Action | Redundant | Covered by |")
        print("|---|---|---|---|---|---|")
        for r in sorted(reviewed, key=lambda r: (r["sl"], r["species"], r["gene"])):
            covered = ", ".join(r["covered_by"][:4]) or "-"
            print(
                f"| {r['species']} | {r['gene']} | {r['term']} | {r['action']} | "
                f"{'yes' if r['redundant'] else 'no'} | {covered} |"
            )


if __name__ == "__main__":
    main()
