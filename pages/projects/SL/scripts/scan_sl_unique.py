#!/usr/bin/env python3
"""Find and score SL-unique GO annotations across the ai-gene-review corpus.

An annotation is **SL-unique** when a gene's only source for a GO term is
``GO_REF:0000044`` -- the UniProt subcellular-location pipeline. This is the
localization analogue of the SPKW project's keyword-unique annotations
(``GO_REF:0000043``), with one important difference: the GAF's WITH/FROM column
records the source ``UniProtKB-SubCell:SL-xxxx`` identifier directly, so the
source-level view SPKW had to reconstruct via external2go is available for free.

Emits three tables for ``projects/SL/SL-METHODOLOGY.md``:

1. corpus totals and aspect breakdown;
2. per-GO-term review outcomes, sorted by issue rate;
3. per-SL-location review outcomes, with SL names resolved from the UniProt API
   (``--offline`` skips the lookup and prints bare identifiers).

    uv run python projects/SL/scripts/scan_sl_unique.py

Takes roughly 5 minutes over the full ``genes/`` tree. Nothing is hardcoded:
rerun and paste the output.
"""

from __future__ import annotations

import argparse
import collections
import glob
import json
import re
import urllib.request
from pathlib import Path

SL_REF = "GO_REF:0000044"
SUBCELL_PREFIX = "UniProtKB-SubCell:"

# Actions that mean the reviewer judged the annotation wrong or misplaced, as
# opposed to merely peripheral (KEEP_AS_NON_CORE) or fine (ACCEPT).
ISSUE_ACTIONS = ("REMOVE", "MARK_AS_OVER_ANNOTATED", "MODIFY")

ANNOTATION_RE = re.compile(r"^\s*- term:\n\s+id: (GO:\d+)\n(.*?)(?=^\s*- term:|\Z)", re.S | re.M)
ACTION_RE = re.compile(r"\n\s+action: ([A-Z_]+)")


def scan_goa(root: Path):
    """Return SL-unique annotations as (species, gene, term, name, aspect, sl)."""
    per: dict = collections.defaultdict(lambda: collections.defaultdict(list))
    for path in glob.glob(str(root / "genes" / "*" / "*" / "*-goa.tsv")):
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
        for line in lines[1:]:
            cols = line.split("\t")
            if len(cols) <= max(i_term, i_name, i_aspect, i_ref, i_with):
                continue
            key = (cols[i_term], cols[i_name], cols[i_aspect])
            per[(species, gene)][key].append((cols[i_ref], cols[i_with]))

    unique = []
    for (species, gene), terms in per.items():
        for (term, name, aspect), evidence in terms.items():
            if {ref for ref, _ in evidence} != {SL_REF}:
                continue
            sls = sorted(
                {
                    part
                    for _, with_from in evidence
                    for part in with_from.split("|")
                    if part.startswith(SUBCELL_PREFIX)
                }
            )
            unique.append((species, gene, term, name, aspect, ";".join(sls)))
    return unique


def scan_reviews(root: Path, unique):
    """Attach the review action for each SL-unique annotation that has one."""
    wanted = collections.defaultdict(set)
    for species, gene, term, *_ in unique:
        wanted[(species, gene)].add(term)

    actions: dict[tuple[str, str, str], str] = {}
    for (species, gene), terms in wanted.items():
        path = root / "genes" / species / gene / f"{gene}-ai-review.yaml"
        if not path.exists():
            continue
        text = path.read_text(errors="ignore")
        start = text.find("\nexisting_annotations:")
        if start < 0:
            continue
        end = text.find("\ncore_functions:", start)
        body = text[start : end if end > 0 else len(text)]
        for match in ANNOTATION_RE.finditer(body):
            term = match.group(1)
            if term not in terms or SL_REF not in match.group(2):
                continue
            action = ACTION_RE.search(match.group(2))
            actions[(species, gene, term)] = action.group(1) if action else "NONE"
    return actions


def resolve_sl_names(sl_ids, offline: bool) -> dict[str, str]:
    """Resolve SL identifiers to their UniProt names."""
    names: dict[str, str] = {}
    if offline:
        return names
    for sl in sl_ids:
        bare = sl.replace(SUBCELL_PREFIX, "")
        try:
            with urllib.request.urlopen(
                f"https://rest.uniprot.org/locations/{bare}"
            ) as handle:
                names[sl] = json.load(handle).get("name", "?")
        except Exception:
            names[sl] = "?"
    return names


def summarize(counter: collections.Counter) -> tuple[int, int, str]:
    total = sum(counter.values())
    issues = sum(counter[a] for a in ISSUE_ACTIONS)
    detail = ", ".join(f"{a} {n}" for a, n in counter.most_common())
    return total, issues, detail


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--min-n", type=int, default=10, help="Minimum reviewed count to list a row.")
    parser.add_argument("--offline", action="store_true", help="Skip UniProt SL name resolution.")
    args = parser.parse_args()

    unique = scan_goa(args.root)
    actions = scan_reviews(args.root, unique)

    genes = {(u[0], u[1]) for u in unique}
    aspects = collections.Counter(u[4] for u in unique)
    print("## Corpus totals\n")
    print(f"- SL-unique annotations (sole source {SL_REF}): **{len(unique)}**")
    print(f"- distinct gene folders: **{len(genes)}**")
    print(f"- reviewed SL-unique annotations: **{len(actions)}**")
    print(f"- aspect: {dict(aspects)}")

    overall: collections.Counter = collections.Counter(actions.values())
    total, issues, detail = summarize(overall)
    downgraded = issues + overall["KEEP_AS_NON_CORE"]
    print(f"- actions: {detail}")
    print(f"- downgraded or worse: **{downgraded}/{total} ({100 * downgraded / total:.0f}%)**")
    print(f"- issue rate ({'/'.join(ISSUE_ACTIONS)}): **{issues}/{total} ({100 * issues / total:.0f}%)**")

    by_term: dict = collections.defaultdict(collections.Counter)
    by_sl: dict = collections.defaultdict(collections.Counter)
    names = {u[2]: u[3] for u in unique}
    sl_of = {(u[0], u[1], u[2]): u[5] for u in unique}
    for key, action in actions.items():
        by_term[key[2]][action] += 1
        by_sl[sl_of[key]][action] += 1

    print(f"\n## By GO term (>= {args.min_n} reviewed)\n")
    print("| Term | Label | Reviewed | Issues | Rate |")
    print("|---|---|---|---|---|")
    for term, counter in sorted(by_term.items(), key=lambda kv: -sum(kv[1].values())):
        total, issues, _ = summarize(counter)
        if total < args.min_n:
            continue
        print(f"| {term} | {names[term]} | {total} | {issues} | {100 * issues / total:.0f}% |")

    sl_names = resolve_sl_names(
        [sl for sl, c in by_sl.items() if sum(c.values()) >= args.min_n and sl], args.offline
    )
    print(f"\n## By UniProt subcellular location (>= {args.min_n} reviewed)\n")
    print("| SL | Name | Reviewed | Issues | Rate |")
    print("|---|---|---|---|---|")
    for sl, counter in sorted(by_sl.items(), key=lambda kv: -sum(kv[1].values())):
        total, issues, _ = summarize(counter)
        if total < args.min_n or not sl:
            continue
        label = sl_names.get(sl, "?")
        print(f"| {sl.replace(SUBCELL_PREFIX, '')} | {label} | {total} | {issues} | {100 * issues / total:.0f}% |")


if __name__ == "__main__":
    main()
