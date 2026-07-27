#!/usr/bin/env python3
"""Apply review round 1 (ai4c-reviewer, PR #2351) to the staged review YAML.

Six suggestions, none blocking. Each premise was verified before conceding, and one is
pushed back on with evidence rather than accepted:

  1. GO:0030674 IPI has no WITH/FROM  -> ACCEPTED. IPI's WITH/FROM is the interactor, so
     the row was ill-formed. Added CDK9 (P50750) and CCNT1 (O60563), both confirmed human
     Swiss-Prot by primaryAccession. The reviewer's alternative (make it ISS on AFF1/AFF4)
     is declined with a reason: the assay is a co-IP of AFF3 itself in human cells, so IPI
     is the correct code; what was missing was the entity, not the code.
  2. GO:0050877 grounding in tension with the review's own ancestry finding -> PARTLY
     ACCEPTED. Verified: GO:0050890 cognition IS under GO:0050877 and GO:0007611 sits under
     cognition, while GO:0021795 is NOT under GO:0050877. So the human genetics splits -
     the cognitive half is on-branch, the migration half is not - and the reason lumped
     them. Restructured to rest on the donor IMPs, with the cognitive phenotypes as
     on-branch corroboration and the migration evidence explicitly assigned elsewhere.
  3. core_functions[2].molecular_function should perhaps be GO:0030674 or GO:0003712
     -> DECLINED, with evidence. Both would over-claim: the paper leaves the AID-recruitment
     mechanism open and offers cohesin and P-TEFb as alternatives, so no AFF3-AID bridge is
     demonstrated (GO:0030674), and CSR is recombination rather than transcription
     regulation (GO:0003712). The demonstrated activity is switch-region occupancy.
  4. GO:0003711 reason should acknowledge the kinase-to-elongation inference, and the
     sibling claim was only half-checked -> ACCEPTED both. term_relations.py gains
     ("GO:0003711", "GO:0140110", True).
  5. GO:0001822's human quote is urogenital, not renal-specific -> ACCEPTED.
  6. Two follow-ups not filed -> ACCEPTED both.

Anchor-assert before, re-grep after, assert detected == changed.

Usage (operates on the STAGED copy, which is then moved into place):
    uv run python genes/human/AFF3/AFF3-bioinformatics/apply_review_round1.py
"""

from __future__ import annotations

from pathlib import Path

HERE = Path(__file__).resolve().parent
STAGED = HERE / "staged-review.yaml"
if not STAGED.exists():
    raise SystemExit(
        f"FATAL: {STAGED} missing. Copy AFF3-ai-review.yaml to it first -- the pre-write "
        f"hook resolves file: paths against the wrong root in a sibling worktree, so the "
        f"review is edited under a non-matching filename and moved into place."
    )

EDITS: list[tuple[str, str]] = [
    # --- 1. GO:0030674: IPI needs its interactor in WITH/FROM -----------------------
    ("""- term:
    id: GO:0030674
    label: protein-macromolecule adaptor activity
  evidence_type: IPI
  original_reference_id: PMID:26214578
  qualifier: enables
""",
     """- term:
    id: GO:0030674
    label: protein-macromolecule adaptor activity
  evidence_type: IPI
  original_reference_id: PMID:26214578
  qualifier: enables
  supporting_entities:
  - UniProtKB:P50750
  - UniProtKB:O60563
"""),
    ("""      modules it bridges and GOA has curated neither.""",
     """      modules it bridges and GOA has curated neither. For IPI the WITH/FROM field takes the
      interacting partners, so it names CDK9 (UniProtKB:P50750) and cyclin T1
      (UniProtKB:O60563), the two proteins the co-immunoprecipitation actually brought down;
      both were confirmed to be reviewed human entries by asserting primaryAccession on the
      fetch. Making the row ISS on AFF1 and AFF4 instead, whose bridging interfaces are
      structurally mapped, was considered and declined - the assay here is a
      co-immunoprecipitation of AFF3 itself from human cells, so IPI is the correct code and
      what was missing was the entity rather than the code. The unmapped-interface caveat
      belongs in this reason and in the knowledge gap, which is where it is, not in a weaker
      evidence code."""),
    # --- 4. GO:0003711: name the inference from a kinase measurement ------------------
    ("""      substitutes for SEC. Both the AFF1 and AFF4 reviews reached GO:0003711 as the complex-level
      contribution for their genes, from independent evidence.""",
     """      substitutes for SEC. One step in this is an interpretation rather than a measurement and
      is flagged as such - what was measured is polymerase II C-terminal domain kinase activity
      of the purified complexes, and reading that as elongation-factor activity relies on the
      established role of CTD Ser2 phosphorylation in releasing paused polymerase rather than on
      an elongation assay performed on SEC-L3. The contributes_to qualifier already keeps the
      claim off AFF3 itself; the experiment that would convert the inference into a measurement
      is set out in suggested_experiments. Both the AFF1 and AFF4 reviews reached GO:0003711 as
      the complex-level contribution for their genes, from independent evidence, and the sibling
      relation is now checked on both legs - GO:0003711 and GO:0003712 were each verified to sit
      under GO:0140110 with neither containing the other."""),
    # --- 5. GO:0001822: the human quote is urogenital, not renal-specific -------------
    # NOTE the anchor starts mid-line in the source ("entity; independently, ..."); the
    # first version of this anchor began at "independently" and matched 0 times, which the
    # assertion caught. A block-scalar reflow means line boundaries are not claim
    # boundaries -- anchor on what is actually there, not on how the sentence reads.
    ("""      entity; independently, the deletion patient had urogenital tract malformations and KINSSHIP
      is named partly for horseshoe kidney. As with the limb row, nothing is inferred about a new
      molecular activity of the variant protein - the degron substitutions confer resistance to
      degradation. Proposed with restraint, as the weakest of the developmental rows here, and
      explicitly non-core.""",
     """      entity;
      independently, KINSSHIP is named partly for horseshoe or hypoplastic kidney. The second
      supporting quote is weaker than it looks and is flagged rather than leaned on - the deletion
      patient's finding is recorded as urogenital tract malformation, which is broader than the
      kidney, so the mouse null's explicit kidney defect is doing the work and the human quote is
      corroboration of organ system rather than of organ. As with the limb row, nothing is
      inferred about a new molecular activity of the variant protein - the degron substitutions
      confer resistance to degradation. Proposed with restraint, as the weakest of the
      developmental rows here, and explicitly non-core."""),
    # --- 3. CF3: keep GO:0003690 and say why the alternatives over-claim --------------
    ("""      the deaminase that initiates the reaction, which is mechanism-level participation. ISS with
      mouse Aff3 as the supporting entity, since the knockout and the switch-region binding were
      done in mouse; the human arm of the same study is an expression association in B cells and
      is not sufficient on its own.""",
     """      the deaminase that initiates the reaction, which is mechanism-level participation. ISS with
      mouse Aff3 as the supporting entity, since the knockout and the switch-region binding were
      done in mouse; the human arm of the same study is an expression association in B cells and
      is not sufficient on its own. On the molecular function this process pairs with, an adaptor
      or coregulator term was considered and declined as over-claiming. GO:0030674 would assert a
      bridge between the switch-region DNA and the deaminase, and the paper explicitly leaves
      that mechanism open, offering cohesin and P-TEFb as alternative routes; GO:0003712 belongs
      to transcription regulation whereas class switch recombination is a DNA recombination
      reaction. What was measured is occupancy of the switch regions, so double-stranded DNA
      binding is the activity this function rests on.""",),
]

# Two suggested_questions folded in (reviewer point 6).
Q_ANCHOR = """- question: >-
    Mouse Aff3 holds GO:0016604 nuclear body and GO:0005829 cytosol by ISO GO_REF:0000119 with
    UniProtKB:P51826, while human AFF3 currently carries neither term. These look like reflections
    of human annotations that have since been withdrawn. Should ISO projections be re-checked
    against their current source, and does the pipeline retract a projection when its source
    annotation disappears?
  experts:
  - MGI
  - GO Central"""
Q_NEW = """- question: >-
    Mouse Aff3 holds GO:0016604 nuclear body and GO:0005829 cytosol by ISO GO_REF:0000119 with
    UniProtKB:P51826, while human AFF3 currently carries neither term. These look like reflections
    of human annotations that have since been withdrawn. The same projection route has a live
    consequence for the GO:0034612 removal proposed here - mouse Aff3 holds response to tumor
    necrosis factor solely by ISO from the human row, so retracting the human row should retract
    the mouse one, and there is no other support for it in either species. Should ISO projections
    be re-checked against their current source, does the pipeline retract a projection when its
    source annotation disappears, and can the GO:0034612 pair be withdrawn together?
  experts:
  - MGI
  - GO Central
  - BHF-UCL
- question: >-
    AFF4's merged review asks whether GO:0032783 should reach AFF3 at all, on the premise that
    AFF3 has not been shown to be a subunit of the super elongation complex. That premise is
    refuted by AFF3's own literature - PMID:22547686 reports the biochemical isolation of
    AFF3-containing SEC-L3 together with P-TEFb, ENL/MLLT1 and AF9/MLLT3, and PMID:26214578
    immunoprecipitates endogenous AFF3 from human nuclear extracts and recovers CDK9 and cyclin
    T1, with the reciprocal pull-down also on endogenous protein. GO:0032783's definition
    explicitly admits an AFF family protein, so SEC-L3 falls inside the term as written. Should
    that question be withdrawn for AFF3, and should the complex-membership row be upgraded from
    IBA to a direct experimental annotation rather than restricted to an AFF1/AFF4 node? The
    same correction does not obviously extend to AFF2, which was not examined here."""

detected = 0
text = STAGED.read_text()
for old, new in EDITS:
    n = text.count(old)
    assert n == 1, f"anchor found {n} times (expected 1): {old[:90]!r}"
    detected += 1
    text = text.replace(old, new, 1)

n = text.count(Q_ANCHOR)
assert n == 1, f"question anchor found {n} times (expected 1)"
detected += 1
text = text.replace(Q_ANCHOR, Q_NEW, 1)

STAGED.write_text(text)

changed = 0
after = STAGED.read_text()
for old, new in EDITS:
    # `assert old not in after` is UNSATISFIABLE whenever old is a substring of new -- true
    # for the first edit here, which appends supporting_entities after the anchor. The
    # first version of this check used it and reported a failed edit that had in fact
    # succeeded. Count instead: after one replacement, `old` may survive only as many times
    # as `new` itself contains it.
    expected = new.count(old)
    got = after.count(old)
    assert got == expected, (
        f"old text count is {got}, expected {expected} (it survives inside new "
        f"{expected} time(s)): {old[:70]!r}"
    )
    assert new in after, f"new text absent: {new[:70]!r}"
    changed += 1
assert Q_ANCHOR not in after and Q_NEW in after, "question replacement did not land"
changed += 1
assert detected == changed, f"detected {detected} but changed {changed}"

print(f"applied {changed} edit group(s) to {STAGED.name}")
