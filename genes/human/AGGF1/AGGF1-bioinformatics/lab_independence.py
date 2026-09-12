"""How many independent groups have worked on AGGF1?

A review that collapses `NbExp` into independent experiments and catches a
bait-labelling artefact should not then assert laboratory independence it has not
checked. This reads the author list out of each cached publication and groups the
papers by senior (last) author, so "three laboratories" is a measurement rather
than an impression.

Surnames are normalised because the same person appears as both "Wang Q" and
"Wang QK" across records, and a first-author-turned-PI (Tian XL) heads a group
that is not independent of the one he trained in -- that lineage is reported
separately rather than folded into the count, because it is a judgement and the
author list is not.

Run: uv run python lab_independence.py
"""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

import yaml

HERE = Path(__file__).parent
PUBS = HERE.parents[3] / "publications"
REVIEW = HERE.parent / "AGGF1-ai-review.yaml"

# Papers whose provenance the review's independence claims rest on.
RELEVANT = [
    "14961121",  # discovery
    "33069768",  # nucleus / p53 / FHA
    "35608889",  # paraspeckles / NEAT1 RIP
    "33471274",  # NLS + FHA/14-3-3 nucleocytoplasmic transport
    "34551592",  # integrin alpha5beta1 receptor
    "27513923",  # autophagy
    "27522498",  # PI3K/AKT
    "40035560",  # splicing / SRSF6
    "23197652",  # zebrafish venous identity
    "24277077",  # zebrafish hemangioblast
    "39905000",  # retinal angiogenesis / TNFSF12-FN14
    "35202649",  # integrin alpha7 (mouse)
    "37081014",  # aortic aneurysm (mouse)
]


def surname_initials(name: str) -> tuple[str, str]:
    """('Wang QK') -> ('wang', 'qk'). Robust to 'Wang Q' vs 'Wang QK'."""
    parts = name.strip().split()
    if not parts:
        return ("", "")
    return (parts[0].lower(), "".join(parts[1:]).lower())


def authors(pmid: str) -> list[str]:
    p = PUBS / f"PMID_{pmid}.md"
    if not p.exists():
        raise SystemExit(f"missing {p}; run `just fetch-pmid {pmid}`")
    fm = p.read_text().split("---", 2)[1]
    meta = yaml.safe_load(fm)
    a = meta.get("authors") or []
    if not a:
        raise SystemExit(f"{p} frontmatter has no author list -- cannot measure independence")
    return a


def main() -> None:
    rows = []
    for pmid in RELEVANT:
        a = authors(pmid)
        rows.append((pmid, a[0], a[-1]))

    print(f"{'PMID':<10} {'first author':<16} {'senior (last) author'}")
    for pmid, first, last in rows:
        print(f"{pmid:<10} {first:<16} {last}")
    print()

    # Group by senior-author surname, merging initial variants of the same surname
    # only when one initial string is a prefix of the other (Wang Q / Wang QK).
    groups: dict[str, list[str]] = defaultdict(list)
    for pmid, _first, last in rows:
        sn, ini = surname_initials(last)
        key = None
        for existing in groups:
            esn, eini = existing.split("|")
            if esn == sn and (ini.startswith(eini) or eini.startswith(ini)):
                key = existing
                break
        groups[key or f"{sn}|{ini}"].append(pmid)

    print("papers grouped by senior author:")
    for key, pmids in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        sn, ini = key.split("|")
        print(f"  {sn.title()} {ini.upper():<4} : {len(pmids):>2} paper(s)  {', '.join(pmids)}")
    print()

    biggest = max(groups.values(), key=len)
    print(f"Largest single group accounts for {len(biggest)}/{len(rows)} of the papers "
          "this review relies on.")

    # Lineage note, kept separate from the count because it is a judgement.
    disc_first, disc_last = rows[0][1], rows[0][2]
    lineage = [pmid for pmid, _f, last in rows
               if surname_initials(last)[0] == surname_initials(disc_first)[0]]
    print(f"Papers whose senior author is the DISCOVERY paper's first author "
          f"({disc_first}): {lineage or 'none'} -- same lineage, not an independent group.")
    indep = [pmid for pmid, _f, last in rows
             if pmid not in biggest and pmid not in lineage]
    print(f"Papers from neither: {indep}")
    print()

    # The review must not claim more groups than this script finds.
    text = REVIEW.read_text()
    flat = re.sub(r"\s+", " ", text)
    for banned in ("three laboratories", "three later laboratories",
                   "three independent lines of evidence from three laboratories"):
        if banned in flat:
            raise SystemExit(
                f"AGGF1-ai-review.yaml still claims {banned!r}, which this author-list "
                "measurement contradicts."
            )
    print("review text carries no laboratory-count claim contradicted by the author lists.")


if __name__ == "__main__":
    main()
