# EMC8 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: O43402
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC8/EMC8-ai-review.yaml](EMC8-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC8/EMC8-ai-review.html
- Gene notes: present - [genes/human/EMC8/EMC8-notes.md](EMC8-notes.md)
- GOA TSV: present - [genes/human/EMC8/EMC8-goa.tsv](EMC8-goa.tsv)
- UniProt record: present - [genes/human/EMC8/EMC8-uniprot.txt](EMC8-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC8.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC8.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC8.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC8/EMC8-deep-research-falcon.md](EMC8-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC8 (ER membrane protein complex subunit 8; also known as C16orf2/C16orf4, COX4NB/NOC4 "Neighbor of COX4", FAM158B) is a small (210 aa) cytosolic, peripherally membrane-associated subunit of the endoplasmic reticulum membrane protein complex (EMC). The EMC is a conserved, nine-subunit ER transmembrane-domain insertase and membrane-protein chaperone that mediates energy-independent insertion of newly synthesized membrane proteins into the ER membrane, with a preference for transmembrane domains that are weakly hydrophobic or carry destabilizing charged/aromatic residues. The complex acts both co-translationally on multipass membrane proteins (where stop-transfer/membrane-anchor sequences become spanning helices, controlling N-exo topology of substrates such as G protein-coupled receptors) and post-translationally on tail-anchored proteins. Within EMC, EMC8 lies on the cytoplasmic face of the complex and is a non-catalytic accessory subunit; it contains an MPN domain (a JAMM/MPN-related fold) but lacks the catalytic metalloprotease residues, and the substrate-insertion vestibule is provided by the transmembrane subunits EMC3/EMC6 rather than by EMC8. EMC8 and its paralog EMC9 are mutually exclusive subunits that occupy the same position, defining alternative EMC variants. EMC8 docks onto the EMC2 scaffold subunit, its principal and well-documented protein interaction. EMC8 is broadly expressed across human tissues.
- Existing/core annotation action counts: ACCEPT: 14; KEEP_AS_NON_CORE: 14

## PN Consistency Summary

- **Consistency:** Deep research, review YAML, and PN annotation agree: EMC8 is a cytosolic, non-catalytic accessory subunit docking on the EMC2 scaffold; mutually exclusive with paralog EMC9 (PMID:32459176). Degenerate MPN domain, no catalytic metalloprotease residues. The review adds an EMC8-specific client-docking ("Cyto dock"/CaVbeta3) chaperone surface (PMID:37196677) beyond the dossier; no contradiction.
- **PN story / NEW pressure:** PN asserts only EMC membership + transmembrane import/insertion, already captured (GO:0072546 part_of; GO:0032977 contributes_to; GO:0045050, GO:0071816 involved_in). No NEW term warranted. The EMC8-specific CaVbeta3 chaperone/assembly surface could in principle motivate a chaperone MF, but the review (appropriately) leaves it as descriptive, not a new annotation — defensible.
- **Evidence alignment:** High overlap — review and PN both rest on the EMC insertase/structure papers (22119785, 29242231, 32439656, 30415835, 32459176, 35287476). PN process claim is fully evidenced in the review.
- **Verdict:** Consistent; thoroughly reviewed (incl. correct contributes_to for non-catalytic subunit). Only shared concern: group→GO:0044743 import mapping diverges from EMC insertion semantics.

## Full Consistency Review

- **UniProt:** O43402 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component` ; **PN-node mapping:** type → GO:0072546 (EMC complex); group → GO:0044743 (protein transmembrane import into intracellular organelle); class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research, review YAML, and PN annotation agree: EMC8 is a cytosolic, non-catalytic accessory subunit docking on the EMC2 scaffold; mutually exclusive with paralog EMC9 (PMID:32459176). Degenerate MPN domain, no catalytic metalloprotease residues. The review adds an EMC8-specific client-docking ("Cyto dock"/CaVbeta3) chaperone surface (PMID:37196677) beyond the dossier; no contradiction.
- **PN story / NEW pressure:** PN asserts only EMC membership + transmembrane import/insertion, already captured (GO:0072546 part_of; GO:0032977 contributes_to; GO:0045050, GO:0071816 involved_in). No NEW term warranted. The EMC8-specific CaVbeta3 chaperone/assembly surface could in principle motivate a chaperone MF, but the review (appropriately) leaves it as descriptive, not a new annotation — defensible.
- **Mapping strategy:** EMC8 does not change the shared node mapping; its EMC8/EMC9 mutual exclusivity makes both still "EMC complex" members, so GO:0072546 stands. Same group-level concern as EMC7: GO:0044743 (lumenal import) mismatches EMC membrane-protein *insertion* semantics (insertion terms are not subclasses of it).
- **Evidence alignment:** High overlap — review and PN both rest on the EMC insertase/structure papers (22119785, 29242231, 32439656, 30415835, 32459176, 35287476). PN process claim is fully evidenced in the review.
- **Verdict:** Consistent; thoroughly reviewed (incl. correct contributes_to for non-catalytic subunit). Only shared concern: group→GO:0044743 import mapping diverges from EMC insertion semantics.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC8/EMC8-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: O43402
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
