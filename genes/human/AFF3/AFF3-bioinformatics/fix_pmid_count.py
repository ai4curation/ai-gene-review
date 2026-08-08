#!/usr/bin/env python3
"""Bring the reported corrections-check PMID count into line with the last run.

`corrections_check.py` scans the review YAML, the notes and the affinage record, so its
denominator grows every time the notes gain a citation. It has been 17, then 29, and is now
31. The number is read from `corrections.json` rather than typed, so this cannot drift from
the measurement, and a re-grep afterwards asserts no stale denominator survives anywhere in
the gene folder.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/fix_pmid_count.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
DATA = HERE / "corrections.json"
if not DATA.exists():
    raise SystemExit(f"FATAL: {DATA} missing -- run corrections_check.py first")
d = json.loads(DATA.read_text())
N = d["n_pmids"]
FLAGGED = len(d["flagged"])
assert N > 0 and FLAGGED >= 0

EDITS = [
    (GENE / "AFF3-notes.md",
     """That check ran over all **29** PMIDs cited anywhere in the review YAML, these notes, or the
affinage record (`corrections.json` records the list): **1 of 29 flagged, and no retractions and
no expressions of concern.** The count rose from 17 to 29 as these notes accumulated the donor
and IntAct references; the number in the committed artifacts is the one the script last
produced, not a remembered constant.""",
     f"""That check ran over all **{N}** PMIDs cited anywhere in the review YAML, these notes, or the
affinage record (`corrections.json` records the list): **{FLAGGED} of {N} flagged, and no
retractions and no expressions of concern.** The denominator has been 17, then 29, and is now
{N} as these notes accumulated the donor, IntAct and review-round references; every number in
the committed artifacts is read from `corrections.json` rather than remembered, which is the
only reason it has stayed correct through three changes."""),
    (GENE / "AFF3-bioinformatics" / "RESULTS.md",
     "29 PMIDs cited anywhere in the review, the notes or the affinage record, checked by two routes:",
     f"{N} PMIDs cited anywhere in the review, the notes or the affinage record, checked by two routes:"),
    (GENE / "AFF3-bioinformatics" / "RESULTS.md",
     "**1 of 29 flagged; no retractions and no expressions of concern.**",
     f"**{FLAGGED} of {N} flagged; no retractions and no expressions of concern.**"),
]

    # A one-shot repair re-run after it has landed must say "already applied" rather than
    # crash on a consumed anchor -- otherwise the reproduce block in RESULTS.md invites a
    # traceback that looks like a defect. Detect the applied state explicitly, and require
    # that ALL targets are in the same state so a half-applied file still fails loudly.
already = [new in path.read_text() for path, _old, new in EDITS]
if all(already):
    print(f"already applied: every target already reads {FLAGGED} of {N}")
    raise SystemExit(0)
assert not any(already), (
    f"HALF-APPLIED: {sum(already)} of {len(EDITS)} targets already updated. Inspect before "
    f"re-running -- a partially applied repair is exactly the 'landed in N-1' failure."
)

detected = 0
for path, old, new in EDITS:
    t = path.read_text()
    n = t.count(old)
    assert n == 1, f"anchor found {n} times in {path.name}: {old[:60]!r}"
    path.write_text(t.replace(old, new, 1))
    detected += 1

changed = 0
for path, old, new in EDITS:
    t = path.read_text()
    assert t.count(old) == new.count(old), f"old text survived in {path.name}"
    assert new in t, f"new text absent from {path.name}"
    changed += 1
assert detected == changed, f"detected {detected} but changed {changed}"

stale = re.compile(rf"\b(?:\d+) of (?!{N}\b)\d+ flagged")
survivors = [
    str(p) for p in GENE.rglob("*")
    if p.is_file() and p.suffix in {".md", ".yaml"}
    and stale.search(p.read_text(errors="ignore"))
]
assert not survivors, f"stale flagged-count denominator survives in {survivors}"
print(f"updated {changed} site(s) to {FLAGGED} of {N}; no stale denominator survives")
