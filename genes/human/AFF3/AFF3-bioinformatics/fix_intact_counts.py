#!/usr/bin/env python3
"""One-shot repair: replace the HAND-COUNTED IntAct figures with the COMPUTED ones.

The hand-counted claim was "CDK9 in five records across four distinct publications and
four distinct methods with a MI score of 0.73". `intact_partners.py` computes 6 records,
5 publications, 3 methods, and MI in {0.35, 0.73}. Wrong on all four counts.

Every edit asserts its anchor is present BEFORE replacing and the result is re-grepped
AFTER, so a missed occurrence is an error rather than a silent no-op ("fixed in N places,
landed in N-1" has recurred repeatedly in this campaign). The invariant relating what was
found to what was changed is asserted explicitly: detected == changed.

The numbers are read from intact_partners.json rather than typed, so the script cannot
drift from the measurement it is repairing.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/fix_intact_counts.py
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
DATA = HERE / "intact_partners.json"

if not DATA.exists():
    raise SystemExit(
        f"FATAL: {DATA} missing. Run intact_partners.py first -- a missing input must "
        f"be a loud error, not a silently skipped section."
    )
d = json.loads(DATA.read_text())
cdk9 = d["partners"]["P50750"]
NREC, NPUB, NMETH = cdk9["records"], cdk9["n_publications"], cdk9["n_methods"]
assert (NREC, NPUB, NMETH) != (5, 4, 4), "the computed numbers equal the wrong ones"
METHODS = ", ".join(cdk9["methods"])
SCORES = " and ".join(str(s) for s in cdk9["mi_scores"])

RETRACTED = "four distinct publications and four"

EDITS: list[tuple[Path, str, str]] = [
    (GENE / "AFF3-ai-review.yaml",
     """      independently records CDK9 in five records across four distinct publications and four
      distinct methods with a MI score of 0.73, plus MLLT1 by anti-tag co-immunoprecipitation.
      Recorded as a curation recommendation rather than acted on, since the term itself needs no
      change.""",
     f"""      independently records CDK9 in {NREC} records across {NPUB} distinct publications and
      {NMETH} distinct methods, with MI scores of {SCORES}, plus MLLT1 in two records from one
      publication. These counts are computed in intact_partners.py rather than counted by eye,
      because the hand-counted version of them was wrong. Recorded as a curation recommendation
      rather than acted on, since the term itself needs no change."""),
    (GENE / "AFF3-ai-review.yaml",
     """      ENL/MLLT1 and AF9/MLLT3; and IntAct independently records CDK9 in five records across four
      distinct publications and four distinct methods with a MI score of 0.73, plus MLLT1 by
      anti-tag co-immunoprecipitation. What is not established for AFF3, in contrast to AFF1 and""",
     f"""      ENL/MLLT1 and AF9/MLLT3; and IntAct independently records CDK9 in {NREC} records across
      {NPUB} distinct publications and {NMETH} distinct methods ({METHODS}), with MI scores of
      {SCORES}, plus MLLT1 in two records from one publication. What is not established for AFF3,
      in contrast to AFF1 and"""),
    (GENE / "AFF3-ai-review.yaml",
     """    replicated across four independent studies and four methods for the CDK9 contact, rather than""",
     f"""    replicated across {NPUB} independent publications and {NMETH} detection methods for the
    CDK9 contact, rather than"""),
    # NOTE the non-ASCII characters in these two anchors -- the multiplication sign in
    # "TAP x2" and the em dashes. The first version of this script used "x" and "-" and
    # the anchor assertion caught it, which is exactly the hyphen/en-dash/em-dash trap
    # the campaign brief warns about for quote matching.
    (GENE / "AFF3-notes.md",
     # find-anchor: the retracted hand-counted figure, quoted here only to locate it.
     """- **CDK9 in 5 records across 4 distinct publications and 4 distinct methods** (anti-tag co-IP,
  pull down, TAP ×2; MI 0.73) — `PMID:23455922`, `PMID:23602568`, `PMID:32707033`,
  `PMID:33961781`.
- **MLLT1 (ENL)** by anti-tag co-IP (`PMID:33961781`) — a SEC module component.""",
     f"""- **CDK9 in {NREC} records across {NPUB} distinct publications and {NMETH} distinct methods**
  ({METHODS}), MI scores {SCORES} - `PMID:23455922`, `PMID:23602568`, `PMID:28514442`,
  `PMID:32707033`, `PMID:33961781`. **These figures are computed** by
  `intact_partners.py`; the first, hand-counted version of this bullet said "5 records across 4
  publications and 4 methods with MI 0.73" and was wrong on every one of the four numbers,
  which is why the script exists.
- **MLLT1 (ENL)** in 2 records from 1 publication by anti-tag co-IP (`PMID:33961781`), MI 0.35 -
  a SEC module component."""),
    (GENE / "AFF3-bioinformatics" / "RESULTS.md",
     # find-anchor: the retracted hand-counted figure, quoted here only to locate it.
     """  is nothing to adjudicate. IntAct nonetheless returns 14 records (all retrieved), with **CDK9
  in 5 records across 4 distinct publications and 4 distinct methods** (anti-tag co-IP, pull
  down, TAP x2; MI 0.73) and **MLLT1/ENL** by anti-tag co-IP. The two SEC modules AFF3 bridges
  are replicated across independent studies and GOA has curated neither — an under-curation
  datum, not an over-annotation one.""",
     f"""  is nothing to adjudicate. IntAct nonetheless returns {d['n_records']} records (all
  retrieved) over {d['n_partners']} distinct partners. Computed per-partner counts, from
  `intact_partners.py` / `intact_partners.json`:

  | partner | records | publications | methods | MI scores |
  |---|---|---|---|---|
  | CDK9 (P50750) | {NREC} | {NPUB} | {NMETH} | {SCORES} |
  | PIP4K2A (P48426) | 2 | 2 | 1 | 0.35 |
  | MLLT1 (Q03111) | 2 | 1 | 1 | 0.35 |
  | TFRC (P02786) | 1 | 1 | 1 | 0.4 |
  | ERP29 (P30040) | 1 | 1 | 1 | 0.4 |
  | SYT2 (Q8N9I0) | 1 | 1 | 1 | 0.35 |
  | DISC1 (Q9NRI5) | 1 | 1 | 1 | 0.37 |

  The two SEC modules AFF3 bridges, CDK9 and MLLT1/ENL, are both present and GOA has curated
  neither - an under-curation datum, not an over-annotation one. **The first version of this
  section was hand-counted and said "5 records across 4 distinct publications and 4 distinct
  methods with MI 0.73" for CDK9. All four numbers were wrong.** That is why the counts are now
  derived from a committed script and quoted from its output table rather than written in prose."""),
]

detected = 0
for path, old, new in EDITS:
    text = path.read_text()
    n = text.count(old)
    assert n == 1, f"anchor found {n} times in {path.name} (expected 1): {old[:70]!r}"
    detected += 1
    path.write_text(text.replace(old, new, 1))

changed = 0
for path, old, new in EDITS:
    text = path.read_text()
    assert old not in text, f"old text survived in {path.name}"
    assert new in text, f"new text absent from {path.name}"
    changed += 1

assert detected == changed, f"detected {detected} but changed {changed}"

# The detector and the mutator must share a scope, so re-grep the WHOLE gene folder for
# the retracted phrasing rather than only the files edited above.
survivors = [
    str(p) for p in GENE.rglob("*")
    if p.is_file() and p.suffix in {".md", ".yaml", ".py", ".json"}
    and p.name != Path(__file__).name and RETRACTED in p.read_text(errors="ignore")
]
assert not survivors, f"retracted phrasing survives in {survivors}"

print(f"fixed {changed} site(s); computed CDK9 = {NREC} records / {NPUB} publications / "
      f"{NMETH} methods / MI {SCORES}")
print(f"re-grep over {GENE}: no surviving instance of {RETRACTED!r}")
