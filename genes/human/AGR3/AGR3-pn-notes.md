# AGR3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8TD06
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1349)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/AGR3/AGR3-ai-review.yaml](AGR3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AGR3/AGR3-ai-review.html](AGR3-ai-review.html)
- Gene notes: present - [genes/human/AGR3/AGR3-notes.md](AGR3-notes.md)
- GOA TSV: present - [genes/human/AGR3/AGR3-goa.tsv](AGR3-goa.tsv)
- UniProt record: present - [genes/human/AGR3/AGR3-uniprot.txt](AGR3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AGR3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AGR3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGR3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AGR3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AGR3/AGR3-deep-research-falcon.md](AGR3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AGR3 encodes anterior gradient protein 3, a small secretory-pathway AGR/thioredoxin-like protein with an N-terminal signal peptide and C-terminal ER retrieval motif. AGR3 is enriched in ciliated airway epithelial cells and other epithelia, and loss-of-function evidence supports a role in calcium-dependent control of ciliary beat frequency and mucociliary clearance. AGR3 also has reported cancer-associated extracellular interactions with alpha-dystroglycan and LYPD3/C4.4a, but its precise molecular catalytic activity and physiological client proteins remain unresolved.
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 1; NEW: 2

## PN Consistency Summary

- **Consistency:** Major, well-supported divergence. PN places AGR3 in the PDI folding-enzyme group and projects GO:0003756 PDI activity as new-to-GOA. Deep research (falcon, citing Nguyen 2018 crystal structure) and the review both reject canonical PDI activity: AGR3 lacks the CXXC catalytic motif (has DCYQS, only one cysteine; Cys71 solvent-exposed, reduced state), so classical thiol-disulfide exchange is unlikely. The review's core_function explicitly says "current evidence does not justify a canonical protein disulfide isomerase activity annotation." Review YAML, notes, and deep research are internally consistent; they jointly contradict the PN projection (intentionally).
- **PN story / NEW pressure:** PN asserts a PDI MF not in GOA. GO:0003756 is real/non-obsolete, but the gene-level evidence over-reaches for AGR3. Instead the review proposes two NEW process annotations from the mouse-knockout/airway physiology: GO:0003351 epithelial cilium movement involved in extracellular fluid movement and GO:0019722 calcium-mediated signaling (ISS from PMID:25751668). Verdict on PN PDI: **over-reaches** (family-fold inference, not catalytically supported). Verdict on review NEW cilium/Ca terms: defensible ADD (already in review).
- **Evidence alignment:** PN dossier has no reference titles. Review/notes anchor on Nguyen 2018 (structure, DCYQS), Bonser/PMID:25751668 (Agr3-KO ciliary beat frequency, mucociliary clearance), PMID:12592373 (dystroglycan/C4.4a), PMID:18086916 (ER retrieval). PMID:25751668 is abstract-only (full_text_unavailable) — ISS NEW terms appropriately conservative.
- **Verdict:** PN PDI projection (GO:0003756) over-reaches for AGR3; correctly overruled — best-supported role is Ca-dependent ciliary beat regulation. **Recommended edits:** none to YAML. [MAP]: flag ER-proteostasis "Protein disulfide isomerases" group GO:0003756 as requiring gene-level catalytic gating; AGR3 (DCYQS, no CXXC) should be excluded/`no_mapping`.

## Full Consistency Review

- **UniProt:** Q8TD06 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Folding enzyme|Protein disulfide isomerases` ; **PN-node mapping:** group `mapped` ok_for_propagation GO:0003756 protein disulfide isomerase activity (goa_status=new_to_goa); class/branch `no_mapping`.
- **Consistency:** Major, well-supported divergence. PN places AGR3 in the PDI folding-enzyme group and projects GO:0003756 PDI activity as new-to-GOA. Deep research (falcon, citing Nguyen 2018 crystal structure) and the review both reject canonical PDI activity: AGR3 lacks the CXXC catalytic motif (has DCYQS, only one cysteine; Cys71 solvent-exposed, reduced state), so classical thiol-disulfide exchange is unlikely. The review's core_function explicitly says "current evidence does not justify a canonical protein disulfide isomerase activity annotation." Review YAML, notes, and deep research are internally consistent; they jointly contradict the PN projection (intentionally).
- **PN story / NEW pressure:** PN asserts a PDI MF not in GOA. GO:0003756 is real/non-obsolete, but the gene-level evidence over-reaches for AGR3. Instead the review proposes two NEW process annotations from the mouse-knockout/airway physiology: GO:0003351 epithelial cilium movement involved in extracellular fluid movement and GO:0019722 calcium-mediated signaling (ISS from PMID:25751668). Verdict on PN PDI: **over-reaches** (family-fold inference, not catalytically supported). Verdict on review NEW cilium/Ca terms: defensible ADD (already in review).
- **Mapping strategy:** This gene should NOT propagate the node's GO:0003756 mapping. The PDI group mapping is correct for catalytically active members but AGR3 is a divergent, likely-inactive member — a clear case for gene-level gating against the group projection (analogous to AIP vs PPIase group).
- **Evidence alignment:** PN dossier has no reference titles. Review/notes anchor on Nguyen 2018 (structure, DCYQS), Bonser/PMID:25751668 (Agr3-KO ciliary beat frequency, mucociliary clearance), PMID:12592373 (dystroglycan/C4.4a), PMID:18086916 (ER retrieval). PMID:25751668 is abstract-only (full_text_unavailable) — ISS NEW terms appropriately conservative.
- **Verdict:** PN PDI projection (GO:0003756) over-reaches for AGR3; correctly overruled — best-supported role is Ca-dependent ciliary beat regulation. **Recommended edits:** none to YAML. [MAP]: flag ER-proteostasis "Protein disulfide isomerases" group GO:0003756 as requiring gene-level catalytic gating; AGR3 (DCYQS, no CXXC) should be excluded/`no_mapping`.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AGR3/AGR3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Folding enzyme | Protein disulfide isomerases
- UniProt: Q8TD06
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Folding enzyme|Protein disulfide isomerases
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0003756 protein disulfide isomerase activity]
        rationale: This PN group captures the canonical ER protein-disulfide-isomerase folding enzymes. GO protein disulfide isomerase activity is the cleanest propagation target for the catalytically active family members.
    - [class] ER proteostasis|Folding enzyme
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0003756 protein disulfide isomerase activity | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Folding enzyme|Protein disulfide isomerases

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
