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
- **Separate defect noticed:** `core_functions[1].directly_involved_in` and the
  `GO:0042176` row's `proposed_replacement_terms` both used `GO:0071985`
  "multivesicular body sorting pathway", which QuickGO reports as **obsolete**
  ("obsolete multivesicular body sorting pathway") with `replaced_by GO:0032509`.
  Unlike `GO:0070676` this one has a clean `replaced_by`, so it is a mechanical swap.
  `just validate worm alx-1` does **not** flag it, even though `core_functions` ids are
  hard-validated — confirming that the obsolete-id blind spot is not limited to `NEW`
  rows. This was initially left for the owner of that sweep; it was fixed in round 2 of
  the PR review instead (see the note below).
- **Validation:** `just validate worm alx-1` passes. The two remaining quote warnings
  are pre-existing entries in `conf/local_quote_baseline.yaml` (hash-keyed, so removing
  a row did not shift them) and are unrelated to this change.

## Review follow-up (2026-11-23, PR #6790 round 2)

The `GO:0071985` obsoletion noted above is fixed here rather than deferred. Verified
against QuickGO on 2026-11-23: `GO:0071985` returns `name: "obsolete multivesicular body
sorting pathway"`, `isObsolete: true`, comment "The reason for obsoletion is that this
term was an unnecessary grouping term", and `replacements: [{id: GO:0032509, type:
replaced_by}]`. `GO:0032509 endosome transport via multivesicular body sorting pathway`
is live and its definition — "The directed movement of substances from endosomes to
lysosomes or vacuoles by a pathway in which molecules are sorted into multivesicular
bodies, which then fuse with the target compartment" — is the claim the review was
making about ALX-1.

Swapped in both author-supplied slots:

- the `proposed_replacement_terms` of the `GO:0042176` regulation-of-protein-catabolic-process
  MODIFY row, whose `reason` prose was updated to name the new term and record the
  obsoletion; and
- `core_functions[1].directly_involved_in`.

No evidence, quote, qualifier or reference was changed; the claim is identical.

This also repairs the round-1 argument for dropping the `GO:0070676` `NEW` row. That
drop was justified partly on the ground that asserting `GO:0032509` there would have
duplicated the `GO:0042176` MODIFY replacement — which was only true in substance, not
on the page, while that replacement still read the obsolete `GO:0071985`. It now reads
`GO:0032509`, so the duplication is visible.
