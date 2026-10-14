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
   paralog MKK4 is imported into the stroma).
3. **A single high-throughput proteomics hit (HDA) for a protein localized elsewhere**:
   **MARK_AS_OVER_ANNOTATED**, not REMOVE. The detection is a real experimental observation
   and most likely contamination, but no targeted experiment excludes the organelle. This
   was already the majority practice (ERECTA, GSTF6, GSTU20, KCR1, PRR7, SUR1, TGG1/2,
   UVR8, VAL1, CUT1, FVE).
4. **Experimental (IDA/HDA) rows are REMOVEd only** when the full text shows an attribution
   error (LHP1: the IDA chloroplast row comes from a RIBA1-3 paper that never mentions
   LHP1), or when the same review accepts an experimental NOT for that organelle (ABCG36:
   NOT chloroplast by IDA, which entails NOT for its sub-compartments). An IDA row is not
   removed on abstract-only or incomplete cached text (EDS1).
5. **IBA** rows are judged on node placement. LCYB mitochondrion (IBA from a COQ6-clade
   placement of a plastid cyclase) stays REMOVE.

UNDECIDED rows (F4JLB7 chloroplast ISM, RCA stromule IDA) were not touched.

## Counts (198 rows)

| Action | Before | After |
|---|---|---|
| ACCEPT | 111 | 111 |
| KEEP_AS_NON_CORE | 19 | 19 |
| MARK_AS_OVER_ANNOTATED | 21 | 27 |
| MODIFY | 1 | 1 |
| REMOVE | 44 | 37 |
| TOO_GENERAL | 0 | 1 |
| UNDECIDED | 2 | 2 |

By evidence, for the rows that moved:

| Evidence:action | Before | After |
|---|---|---|
| HDA:REMOVE | 7 | 2 |
| HDA:MARK_AS_OVER_ANNOTATED | 19 | 24 |
| IDA:REMOVE | 2 | 1 |
| IDA:MARK_AS_OVER_ANNOTATED | 0 | 1 |
| IEA:REMOVE | 1 | 0 |
| IEA:TOO_GENERAL | 0 | 1 |

`chloroplast` (GO:0009507) alone: 95 rows. REMOVE went from 26 to 24 and
MARK_AS_OVER_ANNOTATED from 4 to 6. The 24 remaining REMOVEs are ISM predictions on
nuclear, cytosolic, ER or plasma-membrane proteins (rule 2), plus ABCG36 HDA (rule 4) and
LHP1 IDA (attribution error). The two remaining HDA REMOVEs are ABCG36 chloroplast and
chloroplast envelope, both under an accepted experimental NOT chloroplast.

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
| EDS1 | chloroplast | IDA | PMID:33751092 | REMOVE | MARK_AS_OVER_ANNOTATED | 4 |
| APO1 | plastid | IEA | GO_REF:0000043 | REMOVE | TOO_GENERAL | 1 |
| EDS1 | chloroplast | ISM | GO_REF:0000122 | REMOVE | REMOVE (summary and reason rewritten; they described the EIJ1 paper) | 2 |
| GIP1 | mitochondrion | ISM | GO_REF:0000122 | REMOVE | REMOVE (boilerplate reason replaced with localization evidence) | 2 |

## Left for a human

- **EDS1 chloroplast IDA (PMID:33751092)**: the cached full text has no results section, so
  we cannot see whether a figure places EDS1 in chloroplasts (TAIR curated nucleus,
  cytoplasm and chloroplast from the paper). Marked as over-annotated, not removed. Someone
  with the figures should confirm.
- **CYP79B3 ISM chloroplast** and **MKK5 ISM mitochondrion** stay MARK_AS_OVER_ANNOTATED
  rather than REMOVE because organellar targeting is genuinely predicted or reported but
  untested. A targeted localization experiment would settle them.
- **Plastid rows on chloroplast proteins** (ICS1, IIL1, SSU3, GA2) remain ACCEPT. APO1's row
  is now TOO_GENERAL. Both actions are valid; harmonizing them is a style choice.
- Pre-existing `supporting_text` quote errors (not introduced here) make `just validate`
  fail for AT1G74310 (13), AT5G02500 (5) and APO1 (3). They concern `file:` quotes from the
  deep-research/notes/goa files on other rows.
