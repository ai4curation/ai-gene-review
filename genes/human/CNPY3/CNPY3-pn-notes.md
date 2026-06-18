# CNPY3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BT09
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-07
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CNPY3/CNPY3-ai-review.yaml](CNPY3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CNPY3/CNPY3-ai-review.html](CNPY3-ai-review.html)
- Gene notes: present - [genes/human/CNPY3/CNPY3-notes.md](CNPY3-notes.md)
- GOA TSV: present - [genes/human/CNPY3/CNPY3-goa.tsv](CNPY3-goa.tsv)
- UniProt record: present - [genes/human/CNPY3/CNPY3-uniprot.txt](CNPY3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CNPY3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CNPY3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CNPY3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CNPY3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CNPY3 (Protein canopy homolog 3; also known as PRAT4A, Protein Associated with TLR4) is an endoplasmic reticulum (ER)-resident, glycosylated protein of the canopy family. It has a cleaved N-terminal signal peptide and a single saposin-like / MD-2-related lipid-recognition (ML) domain (a Saposin B-type fold stabilized by three intramolecular disulfide bonds). CNPY3 functions as a Toll-like receptor (TLR)-specific co-chaperone that works together with the ER HSP90 paralog HSP90B1 (gp96 / GRP94 / endoplasmin). The CNPY3-HSP90B1 module mediates the folding and ER-to-surface/endosome trafficking of multiple TLRs, including the cell-surface receptors TLR1, TLR2, TLR4 and TLR5 and the endosomal nucleic-acid-sensing receptors TLR7 and TLR9, but not TLR3, which is CNPY3-independent. CNPY3 is therefore required for TLR exit from the ER and for innate immune signaling downstream of these receptors. The interaction between CNPY3 and HSP90B1 is disrupted by ATP, consistent with a HSP90-co-chaperone client-handoff cycle. Biallelic loss-of-function variants in CNPY3 cause autosomal recessive developmental and epileptic encephalopathy 60 (DEE60).
- Existing/core annotation action counts: ACCEPT: 3; KEEP_AS_NON_CORE: 2; MARK_AS_OVER_ANNOTATED: 4; NEW: 5

## PN Consistency Summary

- **Consistency:** Strongly consistent. Notes, YAML, and PN all describe CNPY3 (PRAT4A) as an ER-luminal TLR-specific co-chaperone for HSP90B1/gp96 (ATP-sensitive interaction), required for TLR1/2/4/5/7/9 folding/ER exit (not TLR3), causal in DEE60. GO:0051879 verified real. The review independently proposes GO:0051879 (action NEW) for the gp96 interaction — directly matching the PN projection.
- **PN story / NEW pressure:** PN asserts Hsp90 binding (GO:0051879) — genuinely absent from GOA (the GOA file has NO Hsp90/Hsp90-binding row, only signaling receptor binding + bare protein binding + ER lumen). So the dossier's `more_specific_than_existing_goa` label is technically too weak: it is effectively `new_to_goa`. The review goes further and proposes a coherent NEW set (GO:0051082 unfolded protein binding, GO:0051879, GO:0034975 protein folding in ER, GO:0045087 innate immune response, GO:0034123 positive regulation of TLR signaling) — all defensible and well beyond the single PN term. ADD GO:0051879 confirmed.
- **Evidence alignment:** PN listed no reference titles for this row. Review evidence is UniProt (gp96/TLR interactions) + Reactome (R-HSA-1678923/1678944 TLR folding by GP96/CNPY3) + mouse PRAT4A mechanism (PMID:20865800, cited in notes); GOA IPI rows (SLITRK4 etc.) correctly dismissed as HT noise. No conflict.
- **Verdict:** Consistent; PN GO:0051879 is correct and already in the review's NEW set, but its goa_status should be `new_to_goa` (not "more_specific"). Review's broader NEW terms are well supported.

## Full Consistency Review

- **UniProt:** Q9BT09 · **batch:** proteostasis-batch-2026-06-07 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|Folding of TLRs` ; **PN-node mapping:** leaf `[subtype] Folding of TLRs` `no_mapping`; `[type] HSP90 cochaperone` → `mapped` GO:0051879 Hsp90 protein binding (`more_specific_than_existing_goa`); group/class/branch unmapped.
- **Consistency:** Strongly consistent. Notes, YAML, and PN all describe CNPY3 (PRAT4A) as an ER-luminal TLR-specific co-chaperone for HSP90B1/gp96 (ATP-sensitive interaction), required for TLR1/2/4/5/7/9 folding/ER exit (not TLR3), causal in DEE60. GO:0051879 verified real. The review independently proposes GO:0051879 (action NEW) for the gp96 interaction — directly matching the PN projection.
- **PN story / NEW pressure:** PN asserts Hsp90 binding (GO:0051879) — genuinely absent from GOA (the GOA file has NO Hsp90/Hsp90-binding row, only signaling receptor binding + bare protein binding + ER lumen). So the dossier's `more_specific_than_existing_goa` label is technically too weak: it is effectively `new_to_goa`. The review goes further and proposes a coherent NEW set (GO:0051082 unfolded protein binding, GO:0051879, GO:0034975 protein folding in ER, GO:0045087 innate immune response, GO:0034123 positive regulation of TLR signaling) — all defensible and well beyond the single PN term. ADD GO:0051879 confirmed.
- **Mapping strategy:** PN maps conservatively at `[type]` (cochaperone), leaving the "Folding of TLRs" leaf and HSP90-system containers unmapped — appropriate. Only refinement: the goa_status should be `new_to_goa` (no Hsp90-binding annotation exists in GOA), not `more_specific_than_existing_goa`.
- **Evidence alignment:** PN listed no reference titles for this row. Review evidence is UniProt (gp96/TLR interactions) + Reactome (R-HSA-1678923/1678944 TLR folding by GP96/CNPY3) + mouse PRAT4A mechanism (PMID:20865800, cited in notes); GOA IPI rows (SLITRK4 etc.) correctly dismissed as HT noise. No conflict.
- **Verdict:** Consistent; PN GO:0051879 is correct and already in the review's NEW set, but its goa_status should be `new_to_goa` (not "more_specific"). Review's broader NEW terms are well supported.

**Recommended edits:** [MAP] Correct goa_status for GO:0051879 on the CNPY3 row from `more_specific_than_existing_goa` to `new_to_goa` (no Hsp90-binding annotation exists in CNPY3 GOA). (Review already proposes GO:0051879 + the full chaperone/TLR NEW set; no YAML change needed.)

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-07
- review_yaml: genes/human/CNPY3/CNPY3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Chaperone | HSP90 system | HSP90 cochaperone | Folding of TLRs
- UniProt: Q9BT09
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [subtype] ER proteostasis|Chaperone|HSP90 system|HSP90 cochaperone|Folding of TLRs
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [type] ER proteostasis|Chaperone|HSP90 system|HSP90 cochaperone
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0051879 Hsp90 protein binding]
        rationale: This PN type groups ER HSP90/GRP94 cochaperones. Hsp90 protein binding is the shared mechanistic assertion.
    - [group] ER proteostasis|Chaperone|HSP90 system
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0051879 Hsp90 protein binding | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=ER proteostasis|Chaperone|HSP90 system|HSP90 cochaperone

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
