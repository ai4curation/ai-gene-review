# EMC9 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y3B6
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/EMC9/EMC9-ai-review.yaml](EMC9-ai-review.yaml)
- AIGR review HTML: missing - genes/human/EMC9/EMC9-ai-review.html
- Gene notes: present - [genes/human/EMC9/EMC9-notes.md](EMC9-notes.md)
- GOA TSV: present - [genes/human/EMC9/EMC9-goa.tsv](EMC9-goa.tsv)
- UniProt record: present - [genes/human/EMC9/EMC9-uniprot.txt](EMC9-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/EMC9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/EMC9.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC9.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/EMC9.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/EMC9/EMC9-deep-research-falcon.md](EMC9-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: EMC9 (ER membrane protein complex subunit 9; also FAM158A) is a 208 aa cytosolic, peripheral subunit of the ER membrane protein complex (EMC), associated with the cytoplasmic face of the ER membrane. It belongs to the EMC8/EMC9 family and contains an MPN (Mpr1/Pad1 N-terminal) domain that is degenerate and lacks the catalytic residues of active JAMM/MPN metalloproteases, so EMC9 is not predicted to have intrinsic enzymatic activity. EMC9 and its paralog EMC8 are mutually exclusive subunits of the EMC, defining alternative complex variants; EMC9 docks into the complex primarily through binding to EMC2. The EMC is a conserved transmembrane-domain insertase and membrane-protein chaperone that mediates energy-independent insertion of newly synthesized membrane proteins into the ER membrane, including post-translational insertion of tail-anchored proteins and cotranslational insertion and topogenesis of multipass membrane proteins. As a peripheral, non-catalytic subunit, EMC9 participates in these processes through complex membership rather than direct catalysis; the membrane insertase activity resides in the EMC3/EMC6 core. EMC9 is broadly expressed and remains relatively weakly characterized.
- Existing/core annotation action counts: ACCEPT: 5; KEEP_AS_NON_CORE: 18

## PN Consistency Summary

- **Consistency:** Deep research, review YAML, and PN annotation are consistent: EMC9 is the cytosolic, peripheral EMC8 paralog (mutually exclusive variant subunit), degenerate MPN domain, non-catalytic, docks via EMC2. The review carries the EMC9-specific developmental "foldopathy" evidence (PMID:37318954 — damaging EMC9 variants, neural-crest/WNT-Fzd7/β-catenin phenotype) not in the dossier; this is supporting, not contradictory.
- **PN story / NEW pressure:** PN asserts only EMC membership + import/insertion, already captured (GO:0072546 part_of; the insertion/insertase terms KEEP_AS_NON_CORE since EMC8/EMC9 are interchangeable). No NEW GO term needed. The WNT-dependent developmental role is disease context, not a new molecular/process annotation; review correctly does not elevate it.
- **Evidence alignment:** High overlap on the EMC insertase/structure core (22119785, 29242231, 32439656, 30415835, 32459176); review adds EMC9-specific PMID:37318954, 32332093 absent from the PN row but consistent with the membrane-protein-biogenesis framing.
- **Verdict:** Consistent; well-reviewed. Note EMC9's contribution is via membership only (paralog-redundant), and the shared group→GO:0044743 mapping diverges from EMC insertion semantics.

## Full Consistency Review

- **UniProt:** Q9Y3B6 · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Transmembrane protein import|EMC complex component` ; **PN-node mapping:** type → GO:0072546 (EMC complex); group → GO:0044743 (protein transmembrane import into intracellular organelle); class → GO:0015031 (protein transport); branch=no_mapping.
- **Consistency:** Deep research, review YAML, and PN annotation are consistent: EMC9 is the cytosolic, peripheral EMC8 paralog (mutually exclusive variant subunit), degenerate MPN domain, non-catalytic, docks via EMC2. The review carries the EMC9-specific developmental "foldopathy" evidence (PMID:37318954 — damaging EMC9 variants, neural-crest/WNT-Fzd7/β-catenin phenotype) not in the dossier; this is supporting, not contradictory.
- **PN story / NEW pressure:** PN asserts only EMC membership + import/insertion, already captured (GO:0072546 part_of; the insertion/insertase terms KEEP_AS_NON_CORE since EMC8/EMC9 are interchangeable). No NEW GO term needed. The WNT-dependent developmental role is disease context, not a new molecular/process annotation; review correctly does not elevate it.
- **Mapping strategy:** EMC9 does not change the shared node mapping (still an EMC complex member → GO:0072546). Same group-level issue as EMC7/EMC8: GO:0044743 (import into organelle interior) mismatches the EMC's membrane-protein insertion role; insertion terms are not subclasses of GO:0044743.
- **Evidence alignment:** High overlap on the EMC insertase/structure core (22119785, 29242231, 32439656, 30415835, 32459176); review adds EMC9-specific PMID:37318954, 32332093 absent from the PN row but consistent with the membrane-protein-biogenesis framing.
- **Verdict:** Consistent; well-reviewed. Note EMC9's contribution is via membership only (paralog-redundant), and the shared group→GO:0044743 mapping diverges from EMC insertion semantics.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/EMC9/EMC9-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Transmembrane protein import | EMC complex component
- UniProt: Q9Y3B6
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
