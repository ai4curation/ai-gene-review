# NAP1 curation notes

## 2026-09-02 - Audit update: fixed misattributed evidence for GO:0051082 (unfolded protein binding)

While auditing the existing review, found that the annotation `GO:0051082 unfolded
protein binding` (evidence_type IDA, original_reference_id PMID:31062022) had been
reviewed with `action: MODIFY`, proposing to replace it with `GO:0000511 H2A-H2B
histone complex chaperone activity`.

This is a genuine oversight: PMID:31062022 (Rossler et al. 2019, "Tsr4 and Nap1, two
novel members of the ribosomal protein chaperOME") is specifically about Nap1 acting
as a dedicated chaperone for the ribosomal protein **Rps6/eS6**, not H2A-H2B:

> "We report the identification of Nap1 and Tsr4 as direct binding partners of Rps6
> and Rps2, respectively. Both factors promote the solubility of their r-protein
> clients in vitro." [PMID:31062022, Abstract, "Nap1 and Tsr4 as direct binding
> partners of Rps6 and Rps2"]

The MODIFY action's justification quoted a Falcon deep-research statement ("The
primary substrate of Nap1 is the H2A-H2B dimer") that is drawn from different papers
(Fung et al. 2024, PMID:39601790; Nagae et al. 2023) discussing Nap1's H2A-H2B
chaperone role in general - it does not describe PMID:31062022's finding and should
not have been used to justify re-terming this specific Rps6-linked annotation as an
H2A-H2B chaperone activity. Replacing GO:0051082 with GO:0000511 for this reference
would misattribute Rps6-chaperone evidence to the histone-chaperone function.

Fix: changed the action from MODIFY (proposed_replacement_terms: GO:0000511) to
KEEP_AS_NON_CORE, kept the term GO:0051082 as-is (a defensible generic description of
Nap1's Rps6-chaperoning activity), and replaced the review's justification/supported_by
with a verbatim quote directly from PMID:31062022. This is consistent with the
existing KEEP_AS_NON_CORE treatment already given to the other PMID:31062022-derived
annotation, GO:0042274 ribosomal small subunit biogenesis, both reflecting Nap1's
peripheral ribosome-biogenesis-chaperone role distinct from its core H2A-H2B chaperone
function (GO:0000511, GO:0042393), which remains correctly and independently
supported by PMID:39601790 and PMID:27225933.

## 2026-09-02 - Fixed two non-verbatim reference findings for PMID:39601790

While validating the above change, `ai-gene-review validate --terms` reported two
pre-existing ERROR-level failures unrelated to the GO:0051082 fix: the `findings`
entries under the top-level `references:` block for PMID:39601790 quoted
markdown-bolded text lifted from the Falcon deep-research summary (e.g. "Nap1 is
described as the **principal cytosolic H2A-H2B chaperone**...") rather than verbatim
text from the cached publication `publications/PMID_39601790.md`, so they failed the
verbatim-substring check.

Fixed both `supporting_text` values to genuine verbatim substrings of the cached full
text of PMID:39601790:
- "mostly localized to the yeast cytoplasm where it chaperones newly synthesized and
  folded H2A-H2B" [PMID:39601790, Introduction]
- "Nap12•H2A-H2B•Kap114•RanGTP complex explains how both Kap114 and Nap12 interact"
  [PMID:39601790, Introduction]

The `statement` summaries (which are not verbatim-checked) were left unchanged as they
accurately paraphrase these passages. Other `supported_by`/`supporting_text` entries
elsewhere in the file that cite `file:yeast/NAP1/NAP1-deep-research-falcon.md` (rather
than the PMID directly) using this same bolded phrasing are correct as-is, since that
phrasing is verbatim within the deep-research file itself.

Both `ai-gene-review validate --verbose --terms` and `ai-gene-review validate-goa`
pass after these changes (validate passes with pre-existing, unrelated warnings about
abstract-only PMIDs, which are out of scope for this fix).

## 2026-09-04 - Review follow-up: applied the GO:0051082 edit and finished the verbatim cleanup

PR review found that the GO:0051082 change described in the section above had been
written up in these notes but never applied to `NAP1-ai-review.yaml` - the YAML block
was still byte-identical to `main` (`action: MODIFY`, `proposed_replacement_terms:
GO:0000511`, Falcon deep-research `supporting_text`). The notes and the YAML therefore
contradicted each other. The diagnosis was re-checked and confirmed, and the edit has
now been applied:

- `GO:0051082 unfolded protein binding` (IDA, PMID:31062022): `MODIFY` ->
  `KEEP_AS_NON_CORE`, `proposed_replacement_terms` (GO:0000511) removed, and the
  Falcon deep-research justification replaced with two verbatim abstract quotes from
  PMID:31062022 itself:
  - "We report the identification of Nap1 and Tsr4 as direct binding partners of Rps6
    and Rps2, respectively. Both factors promote the solubility of their r-protein
    clients in vitro." [PMID:31062022, Abstract]
  - "Nap1 interacts with a large, mostly eukaryote-specific binding surface of Rps6"
    [PMID:31062022, Abstract]

  The core H2A-H2B chaperone activity is unaffected: `GO:0000511` is independently held
  by two IDA annotations (PMID:39601790 and PMID:27225933), so nothing is lost by not
  re-terming the Rps6-linked annotation.

The verbatim cleanup of the top-level `references:` block, which the earlier commit
only did for PMID:39601790, was also finished for PMID:37177996 (same defect class:
markdown-bolded deep-research paraphrase used as a publication quote). That cache is
`abstract_only`, so these were WARNINGs rather than ERRORs, but the quotes were not
publication text:

- finding 0: replaced with "partial unwrapping of a nucleosome by an RNA polymerase
  dramatically facilitates an H2A/H2B dimer dismantling from the nucleosome by
  Nucleosome Assembly Protein 1 (Nap1)" [PMID:37177996, Abstract]
- finding 1: replaced with "the highly acidic C-terminal flexible tails of Nap1
  contribute to the H2A/H2B binding by associating with the binding interface buried
  and not accessible to Nap1 globular domains, supporting the penetrating fuzzy binding
  mechanism seemingly shared across various histone chaperones" [PMID:37177996, Abstract]
- finding 2 (the "Nagae et al. describe Nap1 as a **~48 kDa monomer** ... **nanomolar
  affinity**" entry) was **removed** rather than re-quoted: that assertion appears
  nowhere in the cached abstract, and the text is a deep-research summary sentence
  ("Nagae et al. describe...") rather than anything the paper says. The same content is
  retained elsewhere in the file where it is correctly attributed to
  `file:yeast/NAP1/NAP1-deep-research-falcon.md` (supporting the `GO:0042393 histone
  binding` review), so no evidence is lost - only a mis-sourced quote.

Finally, the two PMID:39601790 findings were tagged `reference_section_type: RESULTS`
but come from the Introduction (`publications/PMID_39601790.md:78`) and the Abstract
(`:53`) respectively, as the section above itself notes; corrected to `INTRODUCTION`
and `ABSTRACT`.

`just validate yeast NAP1` passes; warnings dropped from 12 to 9 (the three removed
were exactly the PMID:37177996 abstract-only quote warnings). The remaining 9 are
pre-existing and unrelated (PMID:12788058 / PMID:38571760 abstract-only quotes,
nucleus locations not mirrored in `existing_annotations`, and three ACCEPT annotations
lacking `supported_by`).

## 2026-09-28 - IBA propagation re-review and generic binding policy cleanup

- Re-reviewed all five IBA annotations against the current `PTHR11875` PAINT slice. `PTN000221934` carries chromatin, nucleus, chromatin binding, and histone binding for the broad NAP-family node, while `PTN000221935` carries the eukaryotic nucleosome-assembly process; both placements are compatible with budding-yeast Nap1, and no target-specific loss or wrong-paralog propagation was found.
- Fetched `interpro/panther/PTHR11875/` because the NAP-family PAINT slice was not cached locally. The official family label is "TESTIS-SPECIFIC Y-ENCODED PROTEIN", but the fetched entries include *S. cerevisiae* NAP1 and VPS75 and the relevant PTN rows.
- Re-read the cached Nap1 primary publications that anchor the current core model: PMID:39601790 for the Nap1-Kap114-H2A-H2B-RanGTP handoff complex, PMID:37177996 for H2A-H2B eviction from partially unwrapped nucleosomes, and PMID:31062022 for the Rps6/eS6 chaperone activity.
- Searched PubMed/web hits for 2025-2026 `Saccharomyces` NAP1/YKR048C papers. The 2025-2026 hits were broad reviews, theses, database pages, or unrelated mentions; no newer primary paper superseded the 2024 Fung et al. Nap1-Kap114 structure or changed the H2A-H2B/Rps6/septin curation calls.
- Added structured `propagation_review` blocks for the IBA rows, using the PTN node rather than the extant WITH/FROM donor list as the IBA source entity.
- Updated all `GO:0005515 protein binding` IntAct rows from legacy `MARK_AS_OVER_ANNOTATED` to `REMOVE`, following the current policy that generic protein binding is uninformative rather than over-annotated. The specific H2A-H2B, histone, homodimerization, and cyclin-binding rows are retained separately.
- Cleaned two pre-existing abstract-only reference findings so PMID:12788058 and PMID:38571760 now quote exact cached abstract text.

## 2026-09-29 - PR #3439 follow-up

- Swapped the relative IBA weighting of `GO:0000785 chromatin` and `GO:0005634
  nucleus`. Both rows still trace to `PTN000221934`, but the chromatin IBD is
  seeded only by PomBase:SPBC36B7.08c and the budding-yeast VPS75 paralog
  (SGD:S000005190), whereas the nucleus IBD includes direct budding-yeast NAP1
  evidence (SGD:S000001756). Chromatin is now `KEEP_AS_NON_CORE` and nucleus is
  `ACCEPT`.
- Kept the IBA `GO:0042393 histone binding` row as core and explicitly recorded
  that its PTN000221934 descendant evidence includes NAP1 itself plus VPS75.
- Demoted the IBA `GO:0003682 chromatin binding` row to `KEEP_AS_NON_CORE` and
  recorded `TERM_SCOPING_PROBLEM` / `GRANULARITY_MISMATCH`: the current PAINT
  row is seeded by plant and mammalian entries rather than fungal evidence, and
  GO:0000511 is the more specific molecular-function description for Nap1.
- Clarified that Nap1 identical-protein-binding rows describe the stable
  homodimeric implementation of H2A-H2B chaperoning, not a separate core
  molecular output.
- Removed a duplicate bare `GO:0042393 histone binding` core function whose
  nucleosome-assembly biology is already covered by the specific GO:0000511
  H2A-H2B chaperone core function.
- Corrected the PMID:12788058 finding to the abstract-supported single
  microarray experiment and added a `reference_review` to PMID:38571760 noting
  that Lorton et al. 2024 is Xenopus/family-level acidic-IDR support rather than
  yeast TTLL4 pathway evidence.

## 2026-10-01 - Current GOA refresh for the IBA campaign

- Forced a current GOA/UniProt refresh for NAP1. The export now has 90 rows,
  representing 89 exact source assertions plus one duplicated cytoplasm row from
  SGD and UniProt.
- Rechecked the PTHR11875 PAINT slice. The current rows still place chromatin,
  nucleus, chromatin binding, and histone binding at PTN000221934 and
  nucleosome assembly at PTN000221935, so the September propagation reviews and
  actions remain aligned with current PAINT.
- Preserved seven no-longer-live historical rows with `retired: true`: the old
  UniProt `GO:0003677 DNA binding` keyword row, five former IntAct
  `GO:0005515 protein binding` exact sources from PMID:14645854, PMID:14759368,
  PMID:15045029, PMID:16554755, and PMID:19536198, and the older
  PMID:31062022 `GO:0051082 unfolded protein binding` row.
- Reviewed the 36 rows newly exposed by the current GOA export. The direct
  Bowman et al. H3-H4 row was kept as non-core, the D'Arcy et al. H2A-H2B row
  was accepted as core, all 26 newly split IntAct `GO:0005515 protein binding`
  rows were removed as uninformative generic interactions, the CK2 paper's
  nucleus/cytoplasm/bud-neck locations were reviewed, and the Rps6/eS6 and Gin4
  rows were retained as peripheral functions.
- Searched 2025-2026 PubMed/web results for newer Saccharomyces
  NAP1/Nap1/YKR048C literature. Fung et al. 2025 was already cached and cited;
  no newer yeast-specific primary paper changed the H2A-H2B, H3-H4, Rps6/eS6,
  or bud-neck calls.

## 2026-10-01 - PR #3771 follow-up

- Changed the retired UniProt keyword `GO:0003677 DNA binding` row from non-core
  retention to `REMOVE`: the keyword is gone from current UniProt and Nap1's
  defining chemistry is acidic DNA mimicry shielding H2A-H2B, not a standalone
  DNA-binding activity.
- Changed the retired PMID:31062022 `GO:0051082 unfolded protein binding` row to
  `MODIFY` with replacement `GO:0044183 protein folding chaperone`, matching
  GOA's current live Rps6/eS6 chaperone row.
- Replaced every remaining placeholder review reason with Nap1-specific support,
  using cached exact quotes for the bud-neck, septin/Gin4, nucleosome-assembly,
  Rps6/eS6, mitotic microtubule, bud-growth, and histone-binding rows.
- Marked the near-root `GO:0008047 enzyme activator activity` row as
  `UNDECIDED`, because the abstract-only RSC/Nap1 paper does not expose the
  enzyme-activation assay needed to decide whether the row should stay generic
  or be modified to a specific ATPase-activation term.
- Trimmed donor-composition language out of the chromatin and chromatin-binding
  IBA reviews, and removed the misleading nucleosome substrate from the core
  H2A-H2B deposition activity.
