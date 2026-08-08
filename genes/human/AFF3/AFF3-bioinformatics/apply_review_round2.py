#!/usr/bin/env python3
"""Apply review round 2 (ai4c-reviewer, PR #2351). One new issue plus five carried over.

The carried-over five are all the same failure: the round-1 commit fixed each claim on the
surface the reviewer had named and left it standing on a low-salience surface — a
propagation_review comment, a source_entities comment, a script docstring, a notes bullet,
and the top-level description. That is "fixed in N places, landed in N-1" again, and my own
`fix_sign_claim.py` could not catch two of them because its NARRATORS exemption is
FILE-scoped: exempting `AFF3-ai-review.yaml` wholesale made the re-grep blind to every
unnarrated instance inside it. The exemption is now per-occurrence, and the check moved into
`audit_claims.py` so it runs on every audit rather than once.

Items:
  1. NEW: "horseshoe or hypoplastic kidney" -- PARTLY DECLINED. The reviewer is right that
     PMID:33961779 spells the acronym "KI for horseshoe kidney" and never says hypoplastic,
     but the phrase is not unsourced: UniProt's DISEASE line for KINSSHIP reads
     "horseshoe or hypoplastic kidney" (AFF3-uniprot.txt:149). The defect was ATTRIBUTION,
     not fabrication -- the phrase sat next to a PMID quote. Now attributed to UniProt
     explicitly, with the file: quote added so it is checkable.
  2. ":263"/":459" still assert "donors disagree in sign" as fact -> ACCEPTED, both fixed.
  3. ":414" "all verified" was vacuous for GO:0045893 and unchecked for GO:0032968
     -> ACCEPTED; the prose is corrected and term_relations.py gains the missing claim.
  4. ":25"/":1269" state the speckle P-TEFb co-concentration without the over-expression
     qualifier -> ACCEPTED. The paper's baseline observation is AFF3 with SC35; the
     redistribution of CDK9/cyclin T1 to AFF3 sites required strong over-production.
  5. intact_partners.py docstring said "5 records" where the JSON computes 6 -> ACCEPTED.
  6. AFF3-notes.md listed PIP4K2A as a singleton; it has 2 records / 2 publications
     -> ACCEPTED.

Every edit anchor-asserted before, re-grepped after, with detected == changed.

Usage:
    cp genes/human/AFF3/AFF3-ai-review.yaml genes/human/AFF3/AFF3-bioinformatics/staged-review.yaml
    uv run python genes/human/AFF3/AFF3-bioinformatics/apply_review_round2.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
GENE = HERE.parent
STAGED = HERE / "staged-review.yaml"
if not STAGED.exists():
    raise SystemExit(f"FATAL: {STAGED} missing -- copy AFF3-ai-review.yaml to it first")

cdk9 = json.loads((HERE / "intact_partners.json").read_text())["partners"]["P50750"]
pip4k = json.loads((HERE / "intact_partners.json").read_text())["partners"]["P48426"]

EDITS: list[tuple[Path, str, str]] = [
    # --- 2. the two surviving "disagree in sign" assertions -------------------------
    (STAGED,
     """      Not about AFF3. Source of mouse Aff1's GO:0045893 IDA, one of the four donors on AFF3's
      GO:0006355 row, and the reason that row's donors disagree in sign.""",
     """      Not about AFF3. Source of mouse Aff1's GO:0045893 IDA, one of the four donors on AFF3's
      GO:0006355 row. An earlier draft of this review cited it as evidence that the row's donors
      disagree in sign; that was wrong - GO:0045893 is positive and so are the other two signed
      donor terms - and the reason for keeping the row unsigned rests on the recipient instead."""),
    (STAGED,
     """        comment: Holds the descendant GO:0045893 by IDA from PMID:9365243. A paralogue, and the
          reason the donor set disagrees in sign.""",
     """        comment: Holds the descendant GO:0045893 by IDA from PMID:9365243. A paralogue. Its
          term is POSITIVE regulation, as are human AFF1's GO:0032786 and GO:0032968, so the
          donor set agrees in sign - an earlier draft of this review asserted the opposite and
          was refuted by the ancestry guard."""),
    # --- 3. the vacuous and the unchecked leg of "all verified" ----------------------
    (STAGED,
     """      here is in fact POSITIVE - GO:0045893, GO:0032786 and GO:0032968 were all verified to sit
      under GO:0045893, and GO:0045893 is itself a descendant of GO:0006355, so a positive child
      was available and unused.""",
     """      here is in fact POSITIVE - mouse Aff1's term IS GO:0045893, and human AFF1's GO:0032786 and
      GO:0032968 were each verified to sit under it - and GO:0045893 is itself a descendant of
      GO:0006355, so a positive child was available and unused. The earlier wording claimed all
      three were verified under GO:0045893, which was vacuous for GO:0045893 itself and untrue of
      GO:0032968, whose claim was missing from the guard until round 2 added it."""),
    # --- 4. the speckle co-concentration, both surfaces ------------------------------
    (STAGED,
     """  expression monoallelic. It concentrates in nuclear speckles together with CDK9 and cyclin T1.""",
     """  expression monoallelic. It concentrates in nuclear speckles, the compartment in which CDK9 and
  cyclin T1 also form foci."""),
    (STAGED,
     """    In human cells the protein and both P-TEFb subunits concentrate together in nuclear speckles,
    which is where the assembled complex is seen.
""",
     """    In human cells AFF3 localises to nuclear speckles, the compartment where CDK9 and cyclin T1
    independently form foci; their redistribution to AFF3-occupied sites was seen only under
    strong AFF3 over-production and is not treated here as a native co-concentration.
"""),
    # --- 1. attribute the hypoplastic-kidney phrase to UniProt ----------------------
    (STAGED,
     """      independently, KINSSHIP is named partly for horseshoe or hypoplastic kidney. The second""",
     """      independently, KINSSHIP is named partly for the kidney phenotype - PMID:33961779 spells the
      acronym out as KI for horseshoe kidney, while UniProt's DISEASE line for the syndrome records
      horseshoe or hypoplastic kidney, and the broader wording is UniProt's rather than the
      paper's. The second"""),
    (STAGED,
     """      Proposed, as a non-core developmental role. Homozygous Aff3 knockout mice have kidney
      defects, and human patients show horseshoe or hypoplastic kidney from stabilising degron
      variants and urogenital malformations from deletion.""",
     """      Proposed, as a non-core developmental role. Homozygous Aff3 knockout mice have kidney
      defects, and human patients show horseshoe kidney from stabilising degron variants -
      hypoplastic kidney too, per UniProt's DISEASE line - and urogenital malformations from
      deletion."""),
    # --- 5. the script docstring --------------------------------------------------
    (HERE / "intact_partners.py",
     """Written because the hand-counted version of this table was WRONG: "5 records across 4
publications and 4 methods with MI 0.73" for CDK9 is actually 5 records across 5
publications and 3 methods, with 4 of the 5 at MI 0.73 and one isoform-2 record at 0.35.
Per the campaign rule, anything computable is computed and then compared against what
was written.""",
     f"""Written because the hand-counted version of this table was WRONG: "5 records across 4
publications and 4 methods with MI 0.73" for CDK9 is actually {cdk9['records']} records across
{cdk9['n_publications']} publications and {cdk9['n_methods']} methods, with MI scores of
{" and ".join(str(s) for s in cdk9['mi_scores'])} (the lower one is an isoform-2 pairing).
Per the campaign rule, anything computable is computed and then compared against what was
written -- and note that this docstring itself said "5 records" for a whole round after the
prose had been fixed, which is why low-salience surfaces need the same sweep as prose."""),
    # --- 6. the notes bullet -------------------------------------------------------
    (GENE / "AFF3-notes.md",
     """- Singletons of unclear relevance: PIP4K2A, SYT2, DISC1 (2-hybrid fragment pooling), and
  ERP29/TFRC by crosslinking (`PMID:30021884`).""",
     f"""- PIP4K2A in {pip4k['records']} records across {pip4k['n_publications']} publications
  (`PMID:28514442`, `PMID:33961781`), MI 0.35 - not a singleton, as an earlier version of this
  bullet said.
- Genuine singletons, of unclear relevance: SYT2, DISC1 (2-hybrid fragment pooling), and
  ERP29/TFRC by crosslinking (`PMID:30021884`)."""),
]

detected = 0
for path, old, new in EDITS:
    t = path.read_text()
    n = t.count(old)
    assert n == 1, f"anchor found {n} times in {path.name} (expected 1): {old[:80]!r}"
    path.write_text(t.replace(old, new, 1))
    detected += 1

changed = 0
for path, old, new in EDITS:
    t = path.read_text()
    expected = new.count(old)
    got = t.count(old)
    assert got == expected, (
        f"old text count is {got}, expected {expected} in {path.name}: {old[:70]!r}")
    assert new in t, f"new text absent from {path.name}"
    changed += 1
assert detected == changed, f"detected {detected} but changed {changed}"

# PER-OCCURRENCE re-grep, not per-file. The round-1 script exempted whole files, which is
# precisely why two instances survived inside AFF3-ai-review.yaml.
SIGN_RE = re.compile(r"[^.]*disagree[sd]? in \*?sign\*?[^.]*\.", re.I)
RETRACT_RE = re.compile(r"retract|wrong|earlier draft|earlier version|earlier wording|"
                        r"misread|misreading|refuted|was false", re.I)
#
# SCOPE NOTE, and the first version of this scan got it wrong: while `staged-review.yaml`
# exists it is the authority and `AFF3-ai-review.yaml` is the superseded copy that has not
# yet been moved into place, so scanning both makes the guard fire on the file it is about
# to replace. The live copy is skipped here and re-checked by `audit_claims.py`, which now
# carries this same check and runs over the live file on every audit -- so the check exists
# permanently rather than only inside a one-shot script.
assert STAGED.exists(), "staged copy must exist for the scope rule below to hold"
SUPERSEDED = {GENE / "AFF3-ai-review.yaml"}
survivors = []
for p in list(GENE.rglob("*")):
    if not p.is_file() or p.suffix not in {".md", ".yaml", ".py", ".json"}:
        continue
    if p.name == Path(__file__).name or p in SUPERSEDED:
        continue
    body = " ".join(p.read_text(errors="ignore").split())
    for m in SIGN_RE.finditer(body):
        sentence = m.group(0)
        # Widen to the sentence before as well: a retraction is often signalled one
        # sentence earlier ("An earlier draft argued X. That was wrong.").
        window = body[max(0, m.start() - 260): m.end() + 260]
        if not RETRACT_RE.search(window):
            survivors.append((p.name, sentence[:130]))
assert not survivors, f"unnarrated sign-disagreement claim survives: {survivors}"

print(f"applied {changed} edit(s); per-occurrence re-grep finds no unnarrated "
      f"sign-disagreement claim in {GENE.name}")
