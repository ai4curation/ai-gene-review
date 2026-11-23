# alx-1 curation notes

**Correction (2026-11-23, issue #6783)**

A corpus scan found that this review asserted an obsolete GO term on an
`action: NEW` row. Validation does not catch this: `existing_annotations[].term.id`
is deliberately not hard-validated (GOA ids are trusted), and a `NEW` row's id is
author-supplied. The term still carried its pre-obsoletion label, so nothing looked
wrong.

- **Obsolete id:** `GO:0070676`, label used here "intralumenal vesicle formation".
  QuickGO now returns `isObsolete: true`, name "obsolete intralumenal vesicle
  formation", obsoleted 2026-10-20, reason "The reason for obsoletion is that the term
  is not clearly defined and usage has been inconsistent." No `replaced_by`; two
  `consider` targets only, `GO:0032509` (endosome transport via multivesicular body
  sorting pathway) and `GO:1990182` (exosomal secretion), both verified current in
  QuickGO.
- **Where it appeared:** one `NEW` row, evidence IMP, cited to PMID:17997305.
- **Chosen: the row was dropped, not re-pointed.** No replacement term was substituted.
- **Why:** re-reading the row against CLAUDE.md's `NEW` bar, it did not clear it, and
  GO's obsoletion reason is the reason to re-examine rather than to pick a `consider`
  target by default.
  1. The row argued from homology and from necessity, in its own words: ALX-1's
     "conserved function as an ESCRT accessory protein that recruits CHMP4/ESCRT-III
     *suggests* it promotes ILV formation", and the mutant phenotype of enlarged MVEs
     and delayed cargo degradation "is *consistent with* defective ILV formation".
     That is a plausibility argument plus a loss-of-function phenotype, which is
     exactly the necessity evidence CLAUDE.md says must not stand in for an answer to
     "which entity performs the step". The budding and scission are ESCRT-III/VPS4
     work; ALX-1/ALIX recruits CHMP4, which is a real contribution but is a claim about
     recruitment, not about ILV formation as a distinct process.
  2. Its PMID supporting quote, `"2007 Nov 8. A novel requirement for C."`, is a
     fragment of the citation line of PMID:17997305, not evidence of anything. (The
     same fragment is used on several other rows in this file; those rows are out of
     scope for this correction and were left alone.)
  3. Nothing is lost by dropping it. The substance is already asserted elsewhere in
     this review with better support: `GO:0007032` endosome organization (IMP,
     PMID:17997305, ACCEPT) covers the enlarged-MVE phenotype, and the `GO:0042176`
     MODIFY row proposes the MVB sorting pathway as the more informative term. Adding
     `GO:0032509` here would have duplicated that MODIFY replacement rather than
     adding coverage, and CLAUDE.md rejects a `NEW` term that is an ancestor or
     descendant of one already being asserted.
- **Divergence from SCAMP3:** the two genes deliberately landed differently. SCAMP3 has
  a dedicated paper placing it in the endosomal membrane with motif-level docking of
  ESCRT-0/ESCRT-I and an in vitro budding assay, so its row was re-pointed to
  `GO:0032509`; alx-1's row rested on homology plus a phenotype, so it was dropped.
- **Separate defect noticed, not fixed here (out of scope for issue #6783's
  `GO:0070676` sweep):** `core_functions[1].directly_involved_in` and the
  `GO:0042176` row's `proposed_replacement_terms` both use `GO:0071985`
  "multivesicular body sorting pathway", which QuickGO now reports as **obsolete**
  ("obsolete multivesicular body sorting pathway") with `replaced_by GO:0032509`.
  Unlike `GO:0070676` this one has a clean `replaced_by`, so it is a mechanical swap.
  `just validate worm alx-1` does **not** flag it, even though `core_functions` ids are
  hard-validated — confirming that the obsolete-id blind spot is not limited to `NEW`
  rows. Left for the owner of that sweep.
- **Validation:** `just validate worm alx-1` passes. The two remaining quote warnings
  are pre-existing entries in `conf/local_quote_baseline.yaml` (hash-keyed, so removing
  a row did not shift them) and are unrelated to this change.
