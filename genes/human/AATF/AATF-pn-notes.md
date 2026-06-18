# AATF PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9NY61
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1322)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/AATF/AATF-ai-review.yaml](AATF-ai-review.yaml)
- AIGR review HTML: present - [genes/human/AATF/AATF-ai-review.html](AATF-ai-review.html)
- Gene notes: present - [genes/human/AATF/AATF-notes.md](AATF-notes.md)
- GOA TSV: present - [genes/human/AATF/AATF-goa.tsv](AATF-goa.tsv)
- UniProt record: present - [genes/human/AATF/AATF-uniprot.txt](AATF-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/AATF.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/AATF.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AATF.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/AATF.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/AATF/AATF-deep-research-falcon.md](AATF-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: AATF (Apoptosis-Antagonizing Transcription Factor, also known as Che-1) is a multifunctional nuclear/nucleolar protein that serves as a structural component of the small subunit (SSU) processome involved in ribosome biogenesis and as a transcriptional cofactor for RNA polymerase II. AATF interacts with POLR2J and Rb family members (RB1, RBL1, RBL2) to modulate E2F target gene expression, and displaces HDAC1 from SP1-bound promoters to activate p21/CDKN1A transcription. In the DNA damage response, AATF is phosphorylated by ATM/ATR, Chk2, and MK2 kinases, leading to modulation of p53-dependent transcriptional programs. AATF also interacts with SAGA/ATAC complex HAT module subunits (ADA2A, ADA2B, GCN5/KAT2A) and binds RNA. It antagonizes apoptosis induced by Dlk/ZIP kinase and PAWR/Par-4. Recent work shows AATF cooperates with NRF-1 to maintain nuclear OXPHOS gene transcription in glioblastoma.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 10; MODIFY: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** **CONTRADICTION (subunit mismatch).** PN places AATF in a **pre-60S / large-subunit** bucket ("pre-60S complex|ANN complex") and projects GO:0030687, which OLS confirms is the **large (66S/pre-60S) subunit precursor**. The review, deep research, and cryo-EM evidence (PMID:34516797) place AATF in the **small-subunit (SSU) processome / pre-40S** (GO:0032040, GO:0042274, GO:0030490). The review explicitly states: "Available structural and GOA evidence places AATF in SSU/pre-40S maturation, not in pre-60S large-subunit precursor particles." So the PN-projected GO:0030687 is wrong for AATF. The group-level GO:0042254 ribosome biogenesis is consistent (entailed). Transcription-coactivator role (Che-1) is well captured but outside the PN's translation framing.
- **PN story / NEW pressure:** PN's biogenesis story is right at the group level (ribosome biogenesis) but mis-specified at the type level (LSU vs SSU). GO:0030687 verified real but biologically incorrect for AATF; the correct complex term (GO:0032040 SSU processome) is **already captured**. No defensible NEW term to add. Conclusion: **PN over-reaches** at the pre-60S type node.
- **Evidence alignment:** PN dossier lists no reference titles. Review centers on PMID:34516797 (cryo-EM SSU processome) and NGDN co-membership — none of which support a pre-60S placement. Divergence is conceptual (LSU vs SSU), not citation-level.
- **Verdict:** Subunit contradiction — PN over-reaches (LSU projection on an SSU factor); review correctly rejects pre-60S. **Recommended edits:** [MAP] Do not project GO:0030687 to AATF; re-bucket AATF under an SSU-processome/pre-40S PN node or suppress the pre-60S type mapping for this gene.

## Full Consistency Review

- **UniProt:** Q9NY61 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex|ANN complex` ; **PN-node mapping:** subtype (ANN complex)=no_mapping; type `pre-60S complex`=mapped→**GO:0030687 preribosome, large subunit precursor** (new_to_goa); group `Ribosome biogenesis factor`=mapped→GO:0042254 (entailed_by_goa_closure); class/branch context_only.
- **Consistency:** **CONTRADICTION (subunit mismatch).** PN places AATF in a **pre-60S / large-subunit** bucket ("pre-60S complex|ANN complex") and projects GO:0030687, which OLS confirms is the **large (66S/pre-60S) subunit precursor**. The review, deep research, and cryo-EM evidence (PMID:34516797) place AATF in the **small-subunit (SSU) processome / pre-40S** (GO:0032040, GO:0042274, GO:0030490). The review explicitly states: "Available structural and GOA evidence places AATF in SSU/pre-40S maturation, not in pre-60S large-subunit precursor particles." So the PN-projected GO:0030687 is wrong for AATF. The group-level GO:0042254 ribosome biogenesis is consistent (entailed). Transcription-coactivator role (Che-1) is well captured but outside the PN's translation framing.
- **PN story / NEW pressure:** PN's biogenesis story is right at the group level (ribosome biogenesis) but mis-specified at the type level (LSU vs SSU). GO:0030687 verified real but biologically incorrect for AATF; the correct complex term (GO:0032040 SSU processome) is **already captured**. No defensible NEW term to add. Conclusion: **PN over-reaches** at the pre-60S type node.
- **Mapping strategy:** The PN type-node `pre-60S complex` mapping should NOT propagate GO:0030687 to AATF. Either AATF is mis-bucketed (belongs under an SSU-processome node) or the projection must be suppressed for this gene. Like the TOMM20/HSPA8/RAB7A precedent, the projected term is rejected — here not merely as broader but as the wrong subunit.
- **Evidence alignment:** PN dossier lists no reference titles. Review centers on PMID:34516797 (cryo-EM SSU processome) and NGDN co-membership — none of which support a pre-60S placement. Divergence is conceptual (LSU vs SSU), not citation-level.
- **Verdict:** Subunit contradiction — PN over-reaches (LSU projection on an SSU factor); review correctly rejects pre-60S. **Recommended edits:** [MAP] Do not project GO:0030687 to AATF; re-bucket AATF under an SSU-processome/pre-40S PN node or suppress the pre-60S type mapping for this gene.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/AATF/AATF-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Translation | Cytosolic translation | Ribosome biogenesis factor | pre-60S complex | ANN complex
- UniProt: Q9NY61
- In branches: TR
- PN-node mapping records (path + ancestors):
    - [subtype] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex|ANN complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [type] Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030687 preribosome, large subunit precursor]
        rationale: This PN type denotes pre-60S particles. The GO preribosome large-subunit precursor term is the direct complex target.
    - [group] Translation|Cytosolic translation|Ribosome biogenesis factor
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0042254 ribosome biogenesis]
        rationale: This PN group collects factors assigned through cytosolic ribosome biogenesis, including SSU-processosome and pre-60S maturation machinery. The full PN path resolves the earlier over-annotation problem: these genes are not being placed by core translational elongation or decoding, but by assembly and maturation of ribosomal subunits. GO ribosome biogenesis is therefore the appropriate propagation target.
    - [class] Translation|Cytosolic translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0002181 cytoplasmic translation]
        rationale: The PN class Cytosolic translation is centered on the cytoplasmic translation apparatus and process, but it also houses supporting machinery such as ribosome biogenesis factors. The GO process term is a useful high-level label for the class, but propagating it to all members would over-annotate genes whose PN placement is through assembly or maturation context rather than core cytoplasmic translation.
    - [branch] Translation
        status=context_only scope=too_broad_to_propagate GO=[GO:0006412 translation]
        rationale: The PN Translation branch is organized around the translation apparatus and immediately associated cotranslational quality-control systems. GO translation is the closest high-level process label, but the PN branch also contains adjacent machinery such as ribosome biogenesis and nascent-chain handling. Keeping this relationship is useful for interpretation, but it is too broad to project safely onto every member.

## Projected GO annotations (2)
- GO:0042254 ribosome biogenesis | scope=ok_for_propagation_to_go | goa_status=entailed_by_goa_closure | from=Translation|Cytosolic translation|Ribosome biogenesis factor
- GO:0030687 preribosome, large subunit precursor | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Translation|Cytosolic translation|Ribosome biogenesis factor|pre-60S complex

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
