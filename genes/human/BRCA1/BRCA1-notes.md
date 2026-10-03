# BRCA1 Gene Review Notes

## 2025-01-14 - Term Label Update

**Issue**: Validation failure due to 1 GO term having an outdated label.

**Root Cause**: GO:0006301 had the label "DNA damage tolerance" but the current ontology uses "postreplication repair".

**Action Taken**: Updated the term label from "DNA damage tolerance" to "postreplication repair" to match the current GO ontology.

**Validation Status**: After fixing the term label, the gene now passes validation with only warnings about PENDING annotations.

**Note**: This represents a routine ontology term label update. BRCA1 is a critical DNA repair protein associated with hereditary breast and ovarian cancer, and the term "postreplication repair" more accurately describes one of its DNA repair functions.

## 2026-07-22 - QA re-review pass

Conservative QA pass over the complete review (275 existing annotations). Changes made:

1. **GO:0045944 (positive regulation of transcription by RNA polymerase II) — action consistency.**
   The four annotations to this term disagreed: IBA, IEA, IDA were `KEEP_AS_NON_CORE` but
   the IMP annotation (PMID:20820192) was `ACCEPT`. Set the IMP annotation to
   `KEEP_AS_NON_CORE` so all four agree. The whole review consistently treats BRCA1
   transcriptional coactivation as peripheral to its core DNA-repair / E3-ligase roles, so
   non-core is the biologically correct choice. This IMP entry also had an **erroneous
   copy-paste summary/reason** ("BRCA1 nucleoplasm localization from Reactome pathway" /
   "Nucleoplasm localization is essential") that described a nucleoplasm CC annotation, not a
   transcription BP term — rewrote both to describe the actual transcriptional-coactivator
   function. supporting_text left unchanged.

2. **GO:0005737 (cytoplasm) — action consistency.**
   The IEA annotation was `ACCEPT` while the IDA annotation (PMID:20160719) was
   `KEEP_AS_NON_CORE`. BRCA1 is predominantly nuclear; cytoplasm is a minor, non-core pool
   (the IEA entry's own reason describes it as splice-variant / context-specific). Set the
   IEA annotation to `KEEP_AS_NON_CORE` to match.

Checked but deliberately left unchanged:
- All 70 `protein binding` (GO:0005515) annotations are already `REMOVE` — none were
  `ACCEPT`/`MODIFY`, so nothing to fix for the "avoid protein binding" guideline. (The
  aggressive blanket-REMOVE of experimental IPI annotations is the prior reviewer's
  consistent choice; not second-guessed here per the "don't overrule curators" guideline.)
- core_functions ids (GO:0004842, GO:0003684, GO:0002039) are all correctly in the
  molecular_function branch.
- No remaining terms have inconsistent actions across evidence types.

Validation after edits: `✓ Valid` (no warnings/errors).
## 2026-10-03 — source-specific reassessment

This assessment supersedes the 2026-07-22 endorsement of blanket protein-binding removal and the earlier core interpretation. All 275 machine-sourced annotation objects remain unchanged, including their term labels, evidence codes and original reference identifiers. The older file contains no structured product, isoform or NOT fields; this reassessment does not invent those fields or reinterpret their absence as proof that every experiment used the same protein product. The preserved UniProt record names eight alternative products. The current decisions are 148 ACCEPT, 88 KEEP_AS_NON_CORE, 12 MODIFY, one MARK_AS_OVER_ANNOTATED and 26 UNDECIDED, with no NEW rows. COMPLETE means every source assertion has been assessed; it does not resolve the 26 stated evidence gaps.

### Three distinct molecular mechanisms

The revised synthesis separates E3 ubiquitin ligase activity, BRCT phosphoprotein recognition and central-region DNA binding. They cooperate in repair but are not interchangeable evidence. BRCA1 engages E2 enzymes through its RING in the BRCA1–BARD1 heterodimer. [PMID:12890688](https://pubmed.ncbi.nlm.nih.gov/12890688/) reports preferential K6-linked autoubiquitination under its purified-protein conditions; [PMID:17873885](https://pubmed.ncbi.nlm.nih.gov/17873885/) explicitly shows different products with different E2 partners. K6 is therefore not asserted as a universal product, nor as the only molecular explanation of hereditary cancer predisposition.

The previous inline citation PMID:23007347 was erroneous: its protected cache and independently checked [official PubMed identity](https://pubmed.ncbi.nlm.nih.gov/23007347/) identify Erlend Hem's 2012 editorial, *Medicine is debate*. It is not the BRCA1 separation-of-function paper described in the old rationale. This was a reviewer-supplied inline error, not the machine GOA reference, and was removed without rewriting a source identifier. The appropriate modern paper is [PMID:37797621](https://pubmed.ncbi.nlm.nih.gov/37797621/) (Wang and colleagues, DOI 10.1016/j.molcel.2023.09.015). ROOT read its official indexed abstract and selected primary Results: previously used ligase-defective variants retain appreciable activity, and more stringent full-length separation-of-function variants support roles in homology-directed repair. Direct full-paper access was unsuccessful, and the one normal three-paper fetch failed DNS. That contextual reading does not create a normal cached reference or justify an unconditional claim about every tumor-suppressive mechanism.

[PMID:15125843](https://pubmed.ncbi.nlm.nih.gov/15125843/) is a BRCT–BACH1 phosphopeptide structure, not a direct DNA-binding experiment. Together with the CtIP phosphopeptide structure ([PMID:16101277](https://pubmed.ncbi.nlm.nih.gov/16101277/)) and Abraxas source evidence, it supports phosphoprotein recognition. Several original generic rows can specifically refine to phosphoserine-residue binding; the broad core describes the shared recognition mechanism without adding a redundant NEW assertion. Binding to these proteins does not confer their helicase or nuclease activity on BRCA1.

Direct DNA binding has separate support from the central BRCA1 fragments in [PMID:15571721](https://pubmed.ncbi.nlm.nih.gov/15571721/) and the already cached primary [PMID:39261729](https://pubmed.ncbi.nlm.nih.gov/39261729/) (Salunkhe and colleagues, DOI 10.1038/s41586-024-07910-2). The latter's unique main Introduction, Results and Discussion and selected purification, resection and binding Methods were read. Its reconstituted and single-molecule assays distinguish BRCA1 and BARD1 DNA-binding modules, stimulation of EXO1 and BLM–DNA2/WRN–DNA2 pathways, and BARD1-mutant cellular experiments. BRCA1 is not the helicase or nuclease. The BRCA1 fragment and intact-complex concentration responses differ; these assays are not represented as identical constructs or as proof of equivalent activity of all isoforms. Figure images and every supplementary experiment were not reanalyzed. Earlier direct-DNA and companion 2024 papers were identified by ROOT, but failed normal retrieval of those missing caches did not block use of this existing source.

### Partner identity and assay scope

The 70 original protein-binding rows were reassessed individually using exact GOA partner records: 47 remain non-core, seven are refined and 16 remain unresolved. The [published project curation instruction](../../../projects/CLINGEN_MENDELIAN.md#curation-instructions) retains supported, biologically correct generic binding when no evidence-backed specific replacement is established. This intentionally differs from the annotation-reviewer informational-exclusion recommendation; a generic term is not evidence that an interaction is false. The standing instruction does not establish unread target-pair experiments. Neither a paper title foregrounding a partner nor an absent target in an abstract is a basis for alleging curator misattribution.

Source partners matter. The generic-binding row from PMID:17873885 names BARD1, whereas the separately seeded enzyme-binding row names P61086/UBE2K. The latter supports E2 binding (GO:0031624), not E3-ligase binding. The PMID:19261748 row names Abraxas, not MERIT40. PMID:8944023 is the BARD1 discovery paper, not a BAP1 study. Nonhuman Q61188/Ezh2 and the Q96RL1-1 partner designation are preserved. Coimmunoprecipitation, proximity labeling, recruitment and purified direct binding remain distinct evidential categories.

The three self-binding removals were withdrawn to UNDECIDED. A dominant BRCA1–BARD1 heterodimer does not refute self-association. The PMID:29656893 and PMID:34591612 caches omit the target Results/tables despite their full-text flags; PMID:8944023's accessible abstract does not expose the separately curated self-assay. Within the collapsed PMID:34591612 generic row, the source explicitly reports spinophilin association, supporting non-core binding while leaving five other partner measurements unverified. This does not validate the self-binding row or certify every screen edge.

The binding consultation was authored by `/root/bloc_followup`, with a disclosed child consultation for its later 20 rows; the final author read and integrated every recommendation. Source-specific access statements are retained in reference assessments. No new quotation words came from the consultation.

### Histone reading, regulation and localization

[PMID:34321665](https://pubmed.ncbi.nlm.nih.gov/34321665/) places recognition of ubiquitin-modified histone surfaces in BARD1, while the BRCA1 RING contacts the nucleosome acidic patch and E2. Its unique main Results and Discussion were read. The unqualified BRCA1 `enables` histone-reader assertion is marked over-annotated, preserving the real reader/writer-complex biology and asking whether a qualified contribution is appropriate. This does not deny BRCA1 nucleosome contact or its catalytic role. The official [author correction](https://www.nature.com/articles/s41586-021-03881-w) adds an omitted Witus citation; its text does not retract the structural result. This correction was read as indexed official text after the direct page failed.

Non-core regulation is not automatically over-annotation. The ACCA source directly connects phosphorylated inactive ACCA binding to reduced fatty-acid synthesis ([PMID:16326698](https://pubmed.ncbi.nlm.nih.gov/16326698/)); broad electronic metabolic terms are refined to the already represented negative regulation. The endothelial paper ([PMID:23415688](https://pubmed.ncbi.nlm.nih.gov/23415688/)) supports angiogenic and ROS-related regulatory outcomes in its experimental context, while the specific TNF and death-domain-receptor assays remain uninspected. Cell-count/DNA-synthesis evidence is distinguished from individual-cell growth in PMID:10518542. Response to indole-3-methanol, stalled-fork resection and gamma-tubulin-ring-complex membership retain explicit source-specific uncertainty.

The complete primary localization passages in [PMID:21282464](https://pubmed.ncbi.nlm.nih.gov/21282464/) distinguish endogenous full-length plasma-membrane observations from EGFP-BRCT constructs, supporting a contextual membrane pool despite BRCA1's predominant nuclear role. All 55 cited Reactome summaries were read; their nucleoplasmic location assertions do not transfer another reaction participant's catalytic activity or mutant-specific defect to wild-type BRCA1. Broad inherited functions were not downgraded because of donor count, self-donation or incomplete reconstruction of a PAINT tree.

The [PMID:34552057 correction](https://www.nature.com/articles/s41420-022-01248-2) was read as indexed official publisher/PMC text. It replaces a Figure 5B flow-cytometry histogram for an irradiated knockout condition. It does not report a change to the Figure 1 coimmunoprecipitation evidence used for the ZGRF1 association. No retraction is inferred, and the corrected image was not independently reanalyzed.

### Evidence and verification limits

The audit read the cached abstracts across all 110 pre-existing PMID references, with targeted main-text reading where available; it does not claim to have read 110 complete papers. Several caches marked full text contain only Introduction/Discussion or incomplete Results. The historical Falcon document remains preserved as provenance and is not used as primary quotation evidence. All 176 existing reference identities are retained; the already available PMID:39261729 and the preserved UniProt record are added as directly used sources. No normal cache is overwritten, and the failed supplementary three-source request is not represented as a successful retrieval.

Eight short supporting quotations are exact substrings of preserved normal caches, totaling no more than 14 words from any one source. Other support is reference-only with source-specific reasons, rather than old title-only or unverifiable quotations. Normal focused schema, ontology-term, GOA and reference validation of the candidate passed with 47 generic-binding policy warnings and no errors. These warnings are the expected result of the documented task instruction. Application, rendering, append-only history and publication are separate steps and are not claimed by this scientific assessment.
