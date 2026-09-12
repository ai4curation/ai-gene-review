# EMC2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q15006
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC2/EMC2-ai-review.yaml](EMC2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC2/EMC2-ai-review.html
- Gene notes: present - [genes/human/EMC2/EMC2-notes.md](EMC2-notes.md)
- GOA TSV: present - [genes/human/EMC2/EMC2-goa.tsv](EMC2-goa.tsv)
- UniProt record: present - [genes/human/EMC2/EMC2-uniprot.txt](EMC2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC2/EMC2-deep-research-falcon.md](EMC2-deep-research-falcon.md)
- [genes/human/EMC2/EMC2-deep-research-openscientist.md](EMC2-deep-research-openscientist.md)

## AIGR Review Snapshot

- Description: EMC2 (ER membrane protein complex subunit 2; also TTC35/tetratricopeptide repeat protein 35) is a 297-residue, all-alpha-helical tetratricopeptide-repeat (TPR) protein that is the soluble cytosolic scaffold subunit of the ER membrane protein complex (EMC), a conserved nine- to ten-subunit transmembrane-domain insertase and chaperone of the endoplasmic reticulum. Its superhelical TPR solenoid organizes the cytosolic face of the EMC, forming an extensive hydrophobic interface with the mutually exclusive paralogous subunits EMC8/EMC9 and contacting the cytosolic extensions of the membrane-spanning subunits EMC3 and EMC5; in this way EMC2 anchors and stabilizes both the cytosolic and the membrane-embedded portions of the complex. EMC2 itself is non-catalytic and contains no transmembrane domain; it is a peripheral membrane protein bound to the cytoplasmic side of the ER membrane via the other EMC subunits. As part of the EMC it contributes to the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, including post-translational insertion of tail-anchored proteins and cotranslational insertion and N-exo topogenesis of multipass membrane proteins such as G protein-coupled receptors; the catalytic insertion vestibule is formed by EMC3 and EMC6. Unassembled cytosolic EMC2 is recognized and degraded by the ubiquitin-proteasome system, and its assembly into the EMC is promoted by the kinase WNK1, which shields the EMC2-EMC8 interface. EMC2 is broadly expressed and resides at the ER membrane.
- Existing/core annotation action counts: ACCEPT: 17; KEEP_AS_NON_CORE: 14

## PN Consistency Summary

- **Consistency:** Strong agreement. Deep research, review YAML, and PN annotation concur: EMC2 (TTC35) is the cytosolic TPR scaffold subunit of the EMC. Review captures GO:0072546 (IBA/IPI/IDA), ER membrane + extrinsic-component-of-ER-membrane (GO:0042406), GO:0032977 (contributes_to), and insertion BPs. WNK1 assembly factor (PMID:33964204) well documented. No contradictions.
- **PN story / NEW pressure:** PN asserts nothing beyond GO coverage. EMC2's distinctive biology (WNK1-shielded assembly, ubiquitin-proteasome turnover of orphan EMC2) is recorded in description/core_functions but is correctly not forced into a new GO term. The "transmembrane protein import" role is captured by the specific insertion terms. Conclusion: already captured.
- **Evidence alignment:** Excellent overlap on core EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835). Review adds EMC2-specific PMID:33964204 (WNK1/scaffold) and the long roster of HuRI/BioPlex/OpenCell interactomes (all LOW relevance, correctly KEEP_AS_NON_CORE). PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## Full Consistency Review

- **UniProt:** Q15006 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (very thorough; ~36 annotations, many high-throughput protein-binding all adjudicated)
- **PN placement:** `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 EMC complex (already_in_goa_exact); group→GO:0044743, class→GO:0015031 (new_to_goa); branch=no_mapping.
- **Consistency:** Strong agreement. Deep research, review YAML, and PN annotation concur: EMC2 (TTC35) is the cytosolic TPR scaffold subunit of the EMC. Review captures GO:0072546 (IBA/IPI/IDA), ER membrane + extrinsic-component-of-ER-membrane (GO:0042406), GO:0032977 (contributes_to), and insertion BPs. WNK1 assembly factor (PMID:33964204) well documented. No contradictions.
- **PN story / NEW pressure:** PN asserts nothing beyond GO coverage. EMC2's distinctive biology (WNK1-shielded assembly, ubiquitin-proteasome turnover of orphan EMC2) is recorded in description/core_functions but is correctly not forced into a new GO term. The "transmembrane protein import" role is captured by the specific insertion terms. Conclusion: already captured.
- **Mapping strategy:** EMC2 does not change the node. type→GO:0072546 exact and correct. Projected group/class terms (GO:0044743, GO:0015031) are broader than the review's specific insertion terms (GO:0045050, GO:0071816, GO:0032977) — the broader-ancestor pattern rejected for TOMM20/HSPA8/RAB7A. No mapping change warranted.
- **Evidence alignment:** Excellent overlap on core EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835). Review adds EMC2-specific PMID:33964204 (WNK1/scaffold) and the long roster of HuRI/BioPlex/OpenCell interactomes (all LOW relevance, correctly KEEP_AS_NON_CORE). PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC2/EMC2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q15006
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
