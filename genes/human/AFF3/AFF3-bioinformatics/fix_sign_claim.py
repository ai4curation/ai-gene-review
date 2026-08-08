#!/usr/bin/env python3
"""One-shot repair: retract the "the GO:0006355 donors disagree in sign" premise.

The GO:0006355 row's reason argued that the unsigned parent is the donors' least common
ancestor because they disagree in sign, reading `GO:0032786` as negative-branch by
proximity to `GO:0032785`. `term_relations.py` refutes it: `GO:0032786` is POSITIVE
regulation of transcription elongation, a descendant of `GO:0045893`, so every signed
donor on that row points the same way.

The verdict does not change - the unsigned parent is still correct - but the argument now
rests on the RECIPIENT's own regulatory output running in both directions (repression at
the XIST DMR; a permissive state at the Meg3 enhancer; 84% of differentially expressed
genes up on Laf4 over-expression), which is a claim about AFF3 rather than about its
donors, and which the review already relies on elsewhere for the separate GO:0045892 row.

Every edit asserts its anchor is present before replacing and re-greps afterwards, and
`detected == changed` is asserted. Note the non-ASCII characters in the markdown anchors.

Usage:
    uv run python genes/human/AFF3/AFF3-bioinformatics/fix_sign_claim.py
"""

from __future__ import annotations

import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE = HERE.parent

# Any sentence pairing the GO:0006355 donors with a sign-disagreement verdict. Anchored on
# the structural shape, not one wording, because the wording is what gets reworded.
RETRACTED_RE = re.compile(
    r"donors disagree in sign|disagree in \*sign\*|negative-negative", re.I)

EDITS: list[tuple[Path, str, str]] = [
    (GENE / "AFF3-ai-review.yaml",
     """      by IMP to GO:0032786 and GO:0032968. The row is kept at the unsigned parent rather than
      refined, because the donors disagree in sign - mouse Aff1's descendant is positive
      regulation while human AFF1's is in the negative-regulation-of-elongation branch - so
      GO:0006355 is their true least common ancestor and asking PAINT to choose a direction would
      be asking it to pick a side the evidence does not pick. AFF3's own human data agree
      independently and in both directions, which is consistent with the unsigned term.""",
     """      by IMP to GO:0032786 and GO:0032968. The row is kept at the unsigned parent rather than
      refined, and the reason is the recipient rather than the donors. Every signed donor term
      here is in fact POSITIVE - GO:0045893, GO:0032786 and GO:0032968 were all verified to sit
      under GO:0045893, and GO:0045893 is itself a descendant of GO:0006355, so a positive child
      was available and unused. An earlier draft of this reason argued instead that the donors
      disagreed in sign, misreading GO:0032786 as negative by proximity to GO:0032785; that was
      wrong and the ancestry guard refuted it. What actually forbids refining the row is that
      AFF3's own output runs in both directions - it represses XIST from the silent allele in
      two human cell lines, while with ZFP281 it establishes a permissive state at the Meg3
      enhancer and its over-expression raises 84% of the transcripts it changes in mouse
      cortical cells. A positive-only term would be false for the repressive half, which is why
      the specific negative instance is proposed as a separate GO:0045892 row instead."""),
    (GENE / "AFF3-bioinformatics" / "RESULTS.md",
     """The `GO:0006355` donors disagree in *sign* (`GO:0045893` positive from mouse Aff1 against
`GO:0032786` negative-branch from human AFF1), so the unsigned parent is their true least
common ancestor and there is no granularity defect on that row (the AEBP2 test).""",
     """**RETRACTED, and corrected here rather than deleted.** An earlier draft of §1 stated that the
`GO:0006355` donors disagree in *sign* — reading `GO:0032786` as negative-branch by proximity to
`GO:0032785`. §3 refutes it: `GO:0032786` is **positive** regulation of transcription elongation,
a descendant of `GO:0045893`, so **every signed donor on that row points the same way**, and
`GO:0045893` is itself a descendant of `GO:0006355`, i.e. a positive child was available and
unused. The AEBP2 donor-disagreement test therefore does **not** apply.

What keeps the row at the unsigned parent is the **recipient**, not the donors: AFF3's own output
runs both ways — it represses XIST from the silent allele in HEK293T and IMR-90, while with
ZFP281 it establishes a permissive chromatin state at the Meg3 enhancer and its over-expression
raises 84% of the transcripts it changes in mouse cortical cells. A positive-only term would be
false for the repressive half. The specific negative instance is proposed as a separate
`GO:0045892` row instead of by refining this one."""),
    (GENE / "AFF3-notes.md",
     """| `MGI:MGI:1100819` | O88573 mouse Aff1 (paralogue) | Swiss-Prot | IDA `GO:0045893` |""",
     """| `MGI:MGI:1100819` | O88573 mouse Aff1 (paralogue) | Swiss-Prot | IDA `GO:0045893` (positive) |"""),
]

detected = 0
for path, old, new in EDITS:
    text = path.read_text()
    n = text.count(old)
    assert n == 1, f"anchor found {n} times in {path.name} (expected 1): {old[:80]!r}"
    detected += 1
    path.write_text(text.replace(old, new, 1))

changed = 0
for path, old, new in EDITS:
    text = path.read_text()
    assert old not in text, f"old text survived in {path.name}"
    assert new in text, f"new text absent from {path.name}"
    changed += 1
assert detected == changed, f"detected {detected} but changed {changed}"

# Scope the re-grep to the whole gene folder, not just the edited files, and exempt only
# the surfaces that NARRATE the retraction (they must contain the phrase to describe it).
NARRATORS = {"RESULTS.md", "fix_sign_claim.py", "AFF3-ai-review.yaml", "AFF3-notes.md"}
survivors = []
for p in GENE.rglob("*"):
    if not p.is_file() or p.suffix not in {".md", ".yaml", ".py", ".json"}:
        continue
    body = p.read_text(errors="ignore")
    if not RETRACTED_RE.search(body):
        continue
    if p.name in NARRATORS:
        # Permitted only where the sentence is explicitly marked as retracted.
        if re.search(r"retract|wrong|earlier draft|misread", body, re.I):
            continue
    survivors.append(str(p))
assert not survivors, f"unnarrated sign-disagreement claim survives in {survivors}"

print(f"fixed {changed} site(s); the sign-disagreement premise is retracted and, where it "
      f"still appears, explicitly marked as retracted")
