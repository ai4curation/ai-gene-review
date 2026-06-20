# EMC1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8N766
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC1/EMC1-ai-review.yaml](EMC1-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC1/EMC1-ai-review.html
- Gene notes: present - [genes/human/EMC1/EMC1-notes.md](EMC1-notes.md)
- GOA TSV: present - [genes/human/EMC1/EMC1-goa.tsv](EMC1-goa.tsv)
- UniProt record: present - [genes/human/EMC1/EMC1-uniprot.txt](EMC1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC1/EMC1-deep-research-falcon.md](EMC1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC1 (ER membrane protein complex subunit 1) is the large lumenal scaffold subunit of the endoplasmic reticulum membrane protein complex (EMC), a conserved nine- to ten-subunit transmembrane-domain insertase and chaperone of the ER. The 993-residue protein has a cleaved N-terminal signal peptide, an extensive lumenal region (~residues 23-962) that folds into a GOLD-like/WD40-YVTN beta-propeller, a single C-terminal transmembrane helix, and a short cytoplasmic tail, making it a single-pass type I membrane protein. As part of the EMC it enables the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or carry destabilizing charged or aromatic residues. The complex inserts tail-anchored proteins post-translationally and inserts the first transmembrane domains of multipass proteins such as G protein-coupled receptors co-translationally, setting their N-exo topology in cooperation with the Sec61 translocon. The catalytic insertion vestibule of the complex is formed by the EMC3 and EMC6 subunits; EMC1 itself is non-catalytic and serves as a lumenal structural scaffold and assembly platform. EMC1 is broadly expressed and resides in the ER membrane, and biallelic or monoallelic variants cause CAVIPMR (cerebellar atrophy, visual impairment, and psychomotor retardation), an autosomal recessive neurodegenerative disorder.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 5

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research (notes + falcon), review YAML, and PN annotation all describe EMC1 as the large lumenal scaffold subunit of the EMC insertase/chaperone. The review captures EMC complex membership (GO:0072546, multiple IDA/IPI/IBA/IEA), ER membrane localization, membrane insertase activity (GO:0032977 contributes_to), and the specific insertion BPs (GO:0071816, GO:0045050). No contradictions.
- **PN story / NEW pressure:** PN asserts no role beyond what GO already captures. The "Transmembrane protein import" framing is already represented by the specific, experimentally-supported insertion terms (GO:0045050, GO:0071816) plus GO:0032977. No defensible new GO term is needed; the chaperone/holdase mode (PMID:40753078, PMID:37196677) is covered via GO:0051082 in core_functions. Conclusion: already captured.
- **Evidence alignment:** Excellent overlap. Both rest on PMID:22119785 (EMC discovery), PMID:29242231 (insertase), PMID:32439656 (structure). Review adds EMC1-specific depth (CAVIPMR genetics PMID:38784058; client engagement PMID:37196677, PMID:40753078). PN cites no row-1 reference titles, so no divergence to flag.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## Full Consistency Review

- **UniProt:** Q8N766 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; ~16 annotations all adjudicated)
- **PN placement:** `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 EMC complex (already_in_goa_exact); group→GO:0044743, class→GO:0015031 (both new_to_goa); branch=no_mapping.
- **Consistency:** Strong agreement. Deep research (notes + falcon), review YAML, and PN annotation all describe EMC1 as the large lumenal scaffold subunit of the EMC insertase/chaperone. The review captures EMC complex membership (GO:0072546, multiple IDA/IPI/IBA/IEA), ER membrane localization, membrane insertase activity (GO:0032977 contributes_to), and the specific insertion BPs (GO:0071816, GO:0045050). No contradictions.
- **PN story / NEW pressure:** PN asserts no role beyond what GO already captures. The "Transmembrane protein import" framing is already represented by the specific, experimentally-supported insertion terms (GO:0045050, GO:0071816) plus GO:0032977. No defensible new GO term is needed; the chaperone/holdase mode (PMID:40753078, PMID:37196677) is covered via GO:0051082 in core_functions. Conclusion: already captured.
- **Mapping strategy:** EMC1 does not change the node. type→GO:0072546 is correct and exact. The projected group/class terms (GO:0044743 protein transmembrane import into intracellular organelle; GO:0015031 protein transport) are BROADER than the review's specific insertion terms — same broader-ancestor pattern rejected for TOMM20/HSPA8/RAB7A. They are defensible as ancestor propagation but add no specificity over existing GOA.
- **Evidence alignment:** Excellent overlap. Both rest on PMID:22119785 (EMC discovery), PMID:29242231 (insertase), PMID:32439656 (structure). Review adds EMC1-specific depth (CAVIPMR genetics PMID:38784058; client engagement PMID:37196677, PMID:40753078). PN cites no row-1 reference titles, so no divergence to flag.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC1/EMC1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q8N766
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0072546 EMC complex]
        rationale: This PN type denotes ER membrane protein complex components. The GO EMC complex cellular-component term is the direct target.
    - [group] ER proteostasis|Protein transport|Transmembrane protein import
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0044743 protein transmembrane import into intracellular organelle]
        rationale: This PN group covers ER transmembrane-protein insertion/import systems such as EMC- and PAT-related pathways. The local GO cache does not expose an ER-specific matching term, so the broader intracellular-organelle transmembrane-import process is the best supported propagation target.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (3)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport
- GO:0044743 protein transmembrane import into intracellular organelle | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport|Transmembrane protein import
- GO:0072546 EMC complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
