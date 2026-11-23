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
