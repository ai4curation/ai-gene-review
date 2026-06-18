# EMC3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9P0I2
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC3/EMC3-ai-review.yaml](EMC3-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC3/EMC3-ai-review.html
- Gene notes: present - [genes/human/EMC3/EMC3-notes.md](EMC3-notes.md)
- GOA TSV: present - [genes/human/EMC3/EMC3-goa.tsv](EMC3-goa.tsv)
- UniProt record: present - [genes/human/EMC3/EMC3-uniprot.txt](EMC3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC3/EMC3-deep-research-falcon.md](EMC3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC3 (ER membrane protein complex subunit 3; also TMEM111) is a 261-residue polytopic ER membrane protein with three transmembrane helices and a lumenal N-terminus, and is the catalytic insertase subunit of the ER membrane protein complex (EMC), a conserved nine- to ten-subunit transmembrane-domain insertase and membrane-protein chaperone of the endoplasmic reticulum. EMC3 belongs to the Oxa1/YidC/Get1 insertase superfamily and is a distant homolog of the tail-anchored-protein insertase Get1; together with the small subunit EMC6 it forms the membrane-embedded hydrophilic vestibule through which substrate transmembrane domains are inserted. A methionine-rich cytosolic loop of EMC3 is required for substrate engagement, and structure-guided mutations of EMC3 residues lining the vestibule (e.g. Arg-31, the Met-rich loop, Arg-180) reduce client insertion without disrupting complex assembly, demonstrating that EMC3 provides the substrate-conducting active site. As part of the EMC, EMC3 enables the energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or carry destabilizing charged or aromatic residues. It mediates post-translational insertion of tail-anchored proteins and cotranslational insertion and N-exo topogenesis of multipass membrane proteins, including the first transmembrane domain of G protein-coupled receptors, in cooperation with the Sec61 translocon. EMC3 is broadly expressed and resides in the ER membrane.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 7

## PN Consistency Summary

- **Consistency:** Strong agreement, and notably EMC3 is the catalytic insertase subunit (Oxa1/YidC/Get1 superfamily) forming the EMC3/EMC6 vestibule. Deep research, review, and PN annotation are aligned. Review correctly elevates GO:0032977 membrane insertase activity to core (contributes_to, but distinguished from accessory subunits by vestibule mutagenesis R31/R180, Met-rich loop). GO:0072546, ER membrane, and insertion BPs all captured. No contradictions.
- **PN story / NEW pressure:** PN ("transmembrane protein import" / "EMC complex component") asserts nothing beyond GO coverage. EMC3's catalytic/selectivity-filter role (PMID:37199759) is captured by GO:0032977 + insertion BPs. No new GO term warranted. Conclusion: already captured.
- **Evidence alignment:** Excellent overlap (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835). Review adds EMC3-specific mechanistic depth: selectivity filter PMID:37199759, topology rectification PMID:37957425, in vivo rhodopsin/photoreceptor requirement PMID:31263175. PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent (EMC3 = catalytic core, correctly handled); PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## Full Consistency Review

- **UniProt:** Q9P0I2 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE (thorough; all annotations adjudicated)
- **PN placement:** `ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component`; **PN-node mapping:** type=mapped/ok_for_propagation → GO:0072546 EMC complex (already_in_goa_exact); group→GO:0044743, class→GO:0015031 (new_to_goa); branch=no_mapping.
- **Consistency:** Strong agreement, and notably EMC3 is the catalytic insertase subunit (Oxa1/YidC/Get1 superfamily) forming the EMC3/EMC6 vestibule. Deep research, review, and PN annotation are aligned. Review correctly elevates GO:0032977 membrane insertase activity to core (contributes_to, but distinguished from accessory subunits by vestibule mutagenesis R31/R180, Met-rich loop). GO:0072546, ER membrane, and insertion BPs all captured. No contradictions.
- **PN story / NEW pressure:** PN ("transmembrane protein import" / "EMC complex component") asserts nothing beyond GO coverage. EMC3's catalytic/selectivity-filter role (PMID:37199759) is captured by GO:0032977 + insertion BPs. No new GO term warranted. Conclusion: already captured.
- **Mapping strategy:** EMC3 does not change the node. type→GO:0072546 is correct/exact for complex membership; importantly the EMC complex CC term (membership) is correctly distinguished from EMC3's catalytic insertase MF — the PN node maps only membership, which is right. Projected group/class terms (GO:0044743, GO:0015031) are broader than the review's specific terms — broader-ancestor pattern (cf. TOMM20/HSPA8/RAB7A). No mapping change warranted.
- **Evidence alignment:** Excellent overlap (PMID:22119785, PMID:29242231, PMID:32439656, PMID:30415835). Review adds EMC3-specific mechanistic depth: selectivity filter PMID:37199759, topology rectification PMID:37957425, in vivo rhodopsin/photoreceptor requirement PMID:31263175. PN cites no row-1 titles; no divergence.
- **Verdict:** Consistent (EMC3 = catalytic core, correctly handled); PN adds no NEW pressure; projected group/class terms broader than review (no mapping change warranted).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC3/EMC3-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q9P0I2
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
