# EMC4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q5J8M3
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC4/EMC4-ai-review.yaml](EMC4-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC4/EMC4-ai-review.html
- Gene notes: present - [genes/human/EMC4/EMC4-notes.md](EMC4-notes.md)
- GOA TSV: present - [genes/human/EMC4/EMC4-goa.tsv](EMC4-goa.tsv)
- UniProt record: present - [genes/human/EMC4/EMC4-uniprot.txt](EMC4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC4/EMC4-deep-research-falcon.md](EMC4-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC4 (ER membrane protein complex subunit 4; also TMEM85) is a small (~183-residue, ~20 kDa) polytopic ER membrane protein and a constitutive structural subunit of the ER membrane protein complex (EMC), a conserved nine- to ten-subunit transmembrane-domain insertase and membrane-protein chaperone of the endoplasmic reticulum. Cryo-EM structures resolve EMC4 with a cytoplasmic N-terminus, transmembrane segments, and a lumenal C-terminus, packing against the other membrane subunits to help form and stabilize the complex. EMC4 is not part of the catalytic insertase core, which is formed by the EMC3 and EMC6 subunits that build the membrane-embedded hydrophilic substrate vestibule; instead EMC4 is an accessory/scaffold subunit. As part of the EMC it contributes to the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or carry destabilizing charged or aromatic residues. The complex mediates post-translational insertion of tail-anchored proteins and cotranslational insertion and N-exo topogenesis of multipass membrane proteins, including transporters and G protein-coupled receptors, in cooperation with the Sec61 translocon. EMC4 is broadly expressed and resides in the ER membrane.
- Existing/core annotation action counts: ACCEPT: 13; KEEP_AS_NON_CORE: 5

## PN Consistency Summary

- **Consistency:** Strong agreement. EMC4 (TMEM85) is an accessory/structural membrane subunit (three-TMD vestibule sidewall, not catalytic). Deep research, review, and PN annotation concur. Review captures GO:0072546, ER membrane, GO:0032977 (contributes_to, correctly NOT elevated to catalytic), and insertion BPs. No contradictions.
- **PN story / NEW pressure:** PN asserts nothing beyond GO coverage. EMC4 has additional distinctive non-core biology in the review (flavivirus host factor PMID:31273220/PMID:31067454; SV40 late-endosome-ER tethering via Rab7/syntaxin18 PMID:32111841; putative EMC3/EMC4 lipid-scramblase PMID:38621120) — all correctly kept as context/non-core, none rising to a defensible NEW GO term (scramblase is computational/not demonstrated for human EMC4 in vivo). Conclusion: already captured.
- **Evidence alignment:** Excellent overlap on core EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835, PMID:37199759, PMID:37196677, PMID:38517390). Review adds EMC4-specific functional-genetics references absent from PN. PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## Full Consistency Review

- **UniProt:** Q5J8M3 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; all annotations adjudicated)
- **PN placement:** `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 EMC complex (already_in_goa_exact); group→GO:0044743, class→GO:0015031 (new_to_goa); branch=no_mapping.
- **Consistency:** Strong agreement. EMC4 (TMEM85) is an accessory/structural membrane subunit (three-TMD vestibule sidewall, not catalytic). Deep research, review, and PN annotation concur. Review captures GO:0072546, ER membrane, GO:0032977 (contributes_to, correctly NOT elevated to catalytic), and insertion BPs. No contradictions.
- **PN story / NEW pressure:** PN asserts nothing beyond GO coverage. EMC4 has additional distinctive non-core biology in the review (flavivirus host factor PMID:31273220/PMID:31067454; SV40 late-endosome-ER tethering via Rab7/syntaxin18 PMID:32111841; putative EMC3/EMC4 lipid-scramblase PMID:38621120) — all correctly kept as context/non-core, none rising to a defensible NEW GO term (scramblase is computational/not demonstrated for human EMC4 in vivo). Conclusion: already captured.
- **Mapping strategy:** EMC4 does not change the node. type→GO:0072546 exact/correct. Projected group/class terms (GO:0044743, GO:0015031) are broader than the review's specific insertion terms — broader-ancestor pattern (cf. TOMM20/HSPA8/RAB7A). The tethering/scramblase roles are EMC4-specific but are not part of the PN "transmembrane protein import" node and should not alter it. No mapping change warranted.
- **Evidence alignment:** Excellent overlap on core EMC papers (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835, PMID:37199759, PMID:37196677, PMID:38517390). Review adds EMC4-specific functional-genetics references absent from PN. PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent; PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC4/EMC4-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q5J8M3
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
