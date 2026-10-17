# ARATH organelle localization consistency audit

Scope: every `existing_annotations` row in `genes/ARATH/*/*-ai-review.yaml` (282 reviews)
on plastid (GO:0009536), mitochondrion (GO:0005739), or one of their `is_a`/`part_of`
descendant compartments (chloroplast, stroma, envelope, thylakoid, chromoplast,
plastoglobule, stromule, mitochondrial sub-compartments, ...). Protein-containing complexes
(descendants of GO:0032991) are excluded because they are complex-membership claims, not
organelle localization claims. Term ids come from the OAK GO SQLite build, not from memory.

- Script: [`scripts/organelle_audit.py`](scripts/organelle_audit.py)
  (`UV_NO_SYNC=1 uv run python projects/ARATH/scripts/organelle_audit.py`)
- Output: [`organelle-audit.yaml`](organelle-audit.yaml) (198 rows, 74 genes; per-row gene,
  term, evidence, reference, action, reason excerpt, with summary counts)

## Principle

Comparable evidence on comparable proteins gets a comparable action, judged against
what is known about the protein:

1. **Genuinely organellar proteins** (transit peptide, targeted localization, organellar
   pathway): ISM, IEA, IBA, HDA and IDA rows for the organelle are ACCEPT, or
   KEEP_AS_NON_CORE when they name a non-functional sub-compartment or a minor pool. A true
   but broad term (plastid under chloroplast) is never REMOVEd. It stays as ACCEPT, or is
   TOO_GENERAL when the review already accepts the specific term.
2. **ISM targeting prediction for a protein with experimental localization elsewhere**
   (nucleus, cytosol, plasma membrane, ER, secretory pathway): **REMOVE**. This is a
   demonstrably wrong electronic inference. The exception is **MARK_AS_OVER_ANNOTATED** when
   a genuine organellar targeting signal or an unresolved organellar-import report exists
   (CYP79B3: N-terminal GUS-fusion plastid report; MKK5: predicted transit sequence,
   paralog MKK4 is imported into the stroma). Rule 6 overrides this rule when another row
   carries the same term.
3. **A single high-throughput proteomics hit (HDA) for a protein localized elsewhere**:
   **MARK_AS_OVER_ANNOTATED**, not REMOVE. The detection is a real experimental observation
   and most likely contamination, but no targeted experiment excludes the organelle. This
   was already the majority practice (ERECTA, GSTF6, GSTU20, KCR1, PRR7, SUR1, TGG1/2,
   UVR8, VAL1, CUT1, FVE). Review reasons point to this page rather than repeating the
   precedent list, which would go stale.
4. **Experimental (IDA/HDA) rows are REMOVEd only** when the full text shows an attribution
   error (LHP1: the IDA chloroplast row comes from a RIBA1-3 paper that never mentions
   LHP1), or when the same review accepts an experimental NOT for that organelle (ABCG36:
   NOT chloroplast by IDA, which entails NOT for its sub-compartments). An experimental row
   whose supporting figures we cannot see is UNDECIDED, not removed or marked as
   over-annotated (EDS1: the cached full text lacks the results section).
5. **IBA** rows are judged on node placement. LCYB mitochondrion (IBA from a COQ6-clade
   placement of a plastid cyclase) stays REMOVE.
6. **Tie-break: one action per term group.** Rules 2 to 5 are indexed on evidence code, but
   a review judges the claim, not the code (`docs/action_consistency.md`): rows on the same
   term in one gene, with the same polarity and isoform, take one action. When the rules
   give different actions for rows on one term, the whole group takes the weaker one:
   - UNDECIDED, if any row is UNDECIDED because its evidence cannot be judged. A row we
     cannot judge cannot be overruled by a sibling's REMOVE (EDS1 chloroplast: IDA and ISM
     both UNDECIDED).
   - Otherwise MARK_AS_OVER_ANNOTATED, if any row takes it. This is the usual case: an ISM
     prediction (rule 2) shares a term with an HDA hit (rule 3), and the group is
     MARK_AS_OVER_ANNOTATED (AT5G02500 chloroplast, ABCG36 mitochondrion).
   - REMOVE for the whole group only when rule 4 applies to the claim itself: the review
     accepts an experimental NOT for that organelle, or the full text shows a wrong-gene
     attribution (ABCG36 chloroplast and chloroplast envelope: HDA rows REMOVE under an
     accepted NOT chloroplast).

   The sibling rows' reasons must agree. Each one names the other row and the shared
   action, instead of one calling the claim contradicted while the other leaves it open.
   After this rule, no gene in the audit has two different actions on the same organelle
   term.

Pre-existing UNDECIDED rows (F4JLB7 chloroplast ISM, RCA stromule IDA) were not touched.

## Counts (198 rows)

| Action | Before | After |
|---|---|---|
| ACCEPT | 111 | 111 |
| KEEP_AS_NON_CORE | 19 | 19 |
| MARK_AS_OVER_ANNOTATED | 21 | 28 |
| MODIFY | 1 | 1 |
| REMOVE | 44 | 34 |
| TOO_GENERAL | 0 | 1 |
| UNDECIDED | 2 | 4 |

By evidence, for the rows that moved:

| Evidence:action | Before | After |
|---|---|---|
| HDA:REMOVE | 7 | 2 |
| HDA:MARK_AS_OVER_ANNOTATED | 19 | 24 |
| IDA:REMOVE | 2 | 1 |
| IDA:UNDECIDED | 1 | 2 |
| IEA:REMOVE | 1 | 0 |
| IEA:TOO_GENERAL | 0 | 1 |
| ISM:REMOVE | 33 | 30 |
| ISM:MARK_AS_OVER_ANNOTATED | 2 | 4 |
| ISM:UNDECIDED | 1 | 2 |

`chloroplast` (GO:0009507) alone: 95 rows. REMOVE went from 26 to 22,
MARK_AS_OVER_ANNOTATED from 4 to 6 and UNDECIDED from 1 to 3. The 22 remaining REMOVEs
are ISM predictions on nuclear, cytosolic, ER or plasma-membrane proteins with no sibling
row on the term (rule 2), plus ABCG36 HDA (rule 4) and LHP1 IDA (attribution error). The
two remaining HDA REMOVEs are ABCG36 chloroplast and chloroplast envelope, both under an
accepted experimental NOT chloroplast.

## Changed rows

| Gene | Term | Evidence | Reference | Old | New | Rule |
|---|---|---|---|---|---|---|
| AT1G74310 (HSP101/CLPB1) | chloroplast stroma | HDA | PMID:20061580 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| AT1G74310 (HSP101/CLPB1) | chloroplast envelope | HDA | PMID:20061580 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| AT5G02500 (HSC70-1) | chloroplast | HDA | PMID:18431481 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| LYM2 | mitochondrion | HDA | PMID:28887381 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| RBOHD | plastid | HDA | PMID:28887381 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| SOS1 | chloroplast envelope | HDA | PMID:12938931 | REMOVE | MARK_AS_OVER_ANNOTATED | 3 |
| ABCG36 | chloroplast envelope | HDA | PMID:12938931 | MARK_AS_OVER_ANNOTATED | REMOVE | 4 |
| ABCG36 | mitochondrion | ISM | GO_REF:0000122 | REMOVE | MARK_AS_OVER_ANNOTATED | 6 (sibling HDA row is MARK_AS_OVER_ANNOTATED) |
| AT5G02500 (HSC70-1) | chloroplast | ISM | GO_REF:0000122 | REMOVE | MARK_AS_OVER_ANNOTATED | 6 (sibling HDA row is MARK_AS_OVER_ANNOTATED) |
| EDS1 | chloroplast | IDA | PMID:33751092 | REMOVE | UNDECIDED | 4 (figures not available to us) |
| EDS1 | chloroplast | ISM | GO_REF:0000122 | REMOVE | UNDECIDED | 6 (sibling IDA row is UNDECIDED; reason rewritten, it described the EIJ1 paper) |
| APO1 | plastid | IEA | GO_REF:0000043 | REMOVE | TOO_GENERAL | 1 |
| GIP1 | mitochondrion | ISM | GO_REF:0000122 | REMOVE | REMOVE (boilerplate reason replaced with localization evidence) | 2 |

The six rule-3 HDA reasons (AT1G74310 x2, AT5G02500, LYM2, RBOHD, SOS1) end with one
sentence pointing to this page instead of a hard-coded precedent gene list. LYM2's reason
no longer argues that the organelle is topologically impossible, which would be a case
for REMOVE.

## Left for a human

- **EDS1 chloroplast (IDA PMID:33751092 and ISM)**: the cached full text has no results
  section, so we cannot see whether a figure places EDS1 in chloroplasts (TAIR curated
  nucleus, cytoplasm and chloroplast from the paper). Both rows are UNDECIDED. Someone with
  the figures should decide: if no figure shows EDS1 in chloroplasts, both rows become
  REMOVE; if one does, the IDA row is kept and the ISM row follows it.
- **CYP79B3 ISM chloroplast** and **MKK5 ISM mitochondrion** stay MARK_AS_OVER_ANNOTATED
  rather than REMOVE because organellar targeting is genuinely predicted or reported but
  untested. A targeted localization experiment would settle them.
- **Plastid rows on chloroplast proteins** (ICS1, IIL1, SSU3, GA2) remain ACCEPT. APO1's row
  is now TOO_GENERAL. Both actions are valid; harmonizing them is a style choice.
- Pre-existing `supporting_text` quote errors (not introduced here) make `just validate`
  fail for AT1G74310 (13), AT5G02500 (5) and APO1 (3). They concern `file:` quotes from the
  deep-research/notes/goa files on other rows.
