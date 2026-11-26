# SCAMP3 curation notes

**Correction (2026-11-23, issue #6783)**

A corpus scan found that this review asserted an obsolete GO term on an
`action: NEW` row. Validation does not catch this: `existing_annotations[].term.id`
is deliberately not hard-validated (GOA ids are trusted), and a `NEW` row's id is
author-supplied. The term still carried its pre-obsoletion label, so nothing looked
wrong.

- **Obsolete id:** `GO:0070676`, label used here "intralumenal vesicle formation".
  QuickGO now returns `isObsolete: true`, name "obsolete intralumenal vesicle
  formation", obsoleted 2026-10-20. Stated reason: "The reason for obsoletion is that
  the term is not clearly defined and usage has been inconsistent." There is **no**
  `replaced_by`; GO offers two `consider` targets only — `GO:0032509` (endosome
  transport via multivesicular body sorting pathway) and `GO:1990182` (exosomal
  secretion). Both of those were checked against QuickGO and are current.
- **Where it appeared:** the `NEW` row (evidence IDA, cited to
  `file:human/SCAMP3/SCAMP3-deep-research-falcon.md`) and `core_functions[0].directly_involved_in`.
- **Chosen:** `GO:0032509` endosome transport via multivesicular body sorting pathway,
  in both places. Evidence type changed IDA → IMP, which is what the cited evidence
  actually is (RNAi depletion).
- **Why:** the underlying work is Falguières, Castle & Gruenberg, *Regulation of the
  MVB pathway by SCAMP3*, Traffic 2012;13:131-42 (PMID:21951651, abstract checked at
  PubMed; the paper is **not** in `publications/` and was not read in full, so it is
  cited here as prose only and the row continues to cite the deep-research file, which
  CLAUDE.md treats as an uncited and possibly out-of-date source). Its abstract states
  SCAMP3 "plays a role in EGF receptor sorting into multivesicular endosomes and in the
  formation of intralumenal vesicles within these endosomes in vitro and thus also
  controls EGF receptor targeting to lysosomes". Applying CLAUDE.md's `NEW` bar — does
  the gene product itself do work of the process, or is it merely required for it? —
  SCAMP3 is not simply a knockout-necessity factor: it is a tetraspanning protein
  resident in the endosomal membrane where the sorting happens, and its PSAP and PY
  motifs are the docking sites that bring ESCRT-I (TSG101) and NEDD4-family ligases to
  that membrane (PMID:19158374). That is a structural, adaptor-like contribution to the
  sorting step, so the claim clears the bar — but the claim that survives is about
  cargo moving through the MVB route to the lysosome, which is `GO:0032509`, not about
  the membrane-deformation event, which is what the obsoleted term named and what GO
  judged ill-defined. The budding itself is ESCRT-III/VPS4 work, and the 2009 paper
  explicitly places SCAMP3 "in parallel with the ESCRTs".
- **Not chosen:** `GO:1990182` exosomal secretion. Nothing in the evidence shows
  SCAMP3-dependent release of vesicles into the extracellular space. SCAMP3's presence
  in the exosome proteome (`GO:0070062`, HDA, PMID:20458337) is already handled
  elsewhere in this review as `KEEP_AS_NON_CORE`, and presence in exosomes is not a
  role in their secretion.
- **Collateral tidy-up:** `GO:0016197` endosomal transport was removed from
  `core_functions[0].directly_involved_in`, because `GO:0032509` is a descendant of it
  and CLAUDE.md rejects asserting a term that is an ancestor or descendant of another
  being asserted. `GO:0016197` remains where it was already used, as the
  `proposed_replacement_terms` entry on the `GO:0006887` exocytosis MODIFY row.
- **Validation behaviour (reported for issue #6783):** `core_functions` ids *are*
  hard-validated, but the obsolete `GO:0070676` in `directly_involved_in` did **not**
  fail before this change. Re-running the validator against the pre-change file
  (`git show HEAD:...`) produced no obsolete-term error — the dynamic-enum check is
  branch reachability, and an obsolete term still resolves. So the blind spot found on
  `NEW` rows extends to `core_functions` as well. After the change,
  `just validate human SCAMP3` is clean (one pre-existing warning about missing
  `propagation_review` on the IBA MODIFY row).

## Review follow-up (2026-11-23, PR #6790 round 2)

**The GO:0032509 NEW row now cites the paper, not the deep-research file.** CLAUDE.md:
"Your notes and deep-research files are not literature. Cite the paper or record they
point to." The row's `original_reference_id` was
`file:human/SCAMP3/SCAMP3-deep-research-falcon.md` and its primary `supporting_text` was a
cell from a machine-generated table in that file.

`uv run ai-gene-review fetch-pmid 21951651` was run on 2026-11-23 and cached
`publications/PMID_21951651.md`. It is the right paper: Falguieres T, Castle D, Gruenberg
J, "Regulation of the MVB pathway by SCAMP3", Traffic 13(1):131-42, 2012,
doi:10.1111/j.1600-0854.2011.01291.x — the work the notes had already identified. It is
abstract-only (`full_text_available: false`; no PMC record), and the abstract states the
annotated claim directly: "We find that SCAMP3 plays a role in EGF receptor sorting into
multivesicular endosomes and in the formation of intralumenal vesicles within these
endosomes in vitro and thus also controls EGF receptor targeting to lysosomes."

Changes: `original_reference_id: PMID:21951651`; that verbatim abstract sentence is the
row's first `supported_by` quote; the Falcon file moved to `additional_reference_ids` as
the route by which the paper was found, not as support; a `references` entry for
PMID:21951651 was added with two findings and a `reference_review`
(`relevance: HIGH`, `correctness: VERIFIED`) recording the verification and the
abstract-only limitation; and the `reason` now says what depth the claim rests on (the
abstract, not the figures). Evidence code stays `IMP` — the abstract's result is a
SCAMP3-perturbation result.

Also removed from the `GO:0006887` exocytosis MODIFY row: a `supported_by` entry quoting
`model: Edison Scientific Literature` from the Falcon file. That is a table header, not a
quotation of anything that supports the claim, and CLAUDE.md requires `supporting_text` to
be actual source text asserting support. The row keeps its PMID:19158374 support.

**GO:0006887 MODIFY replacement (reviewer suggestion 8).** The replacement was
`GO:0016197 endosomal transport`; it is now `GO:0032509 endosome transport via
multivesicular body sorting pathway`, which this review already asserts as a NEW row on
PMID:21951651. CLAUDE.md prefers a replacement term the gene already carries, and
GO:0032509 is the more specific of the two (GO:0032509 is a descendant of GO:0016197,
which is why GO:0016197 had already been dropped from `core_functions`). The `reason`
prose was updated to say so.

**Not changed:** the `GO:0005770` late-endosome NEW row still carries
`original_reference_id: file:human/SCAMP3/SCAMP3-deep-research-falcon.md` and a summary
attributing a "~30% of late endosomes" quantification to the same 2012 paper. That figure
is not in the cached abstract and cannot be checked without the full text, so the row was
left alone rather than re-pointed on an unverifiable basis; it is flagged here for a
follow-up that has the full text.
