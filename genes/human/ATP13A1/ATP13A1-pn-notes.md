# ATP13A1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9HD20
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1382)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATP13A1/ATP13A1-ai-review.yaml](ATP13A1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATP13A1/ATP13A1-ai-review.html](ATP13A1-ai-review.html)
- Gene notes: present - [genes/human/ATP13A1/ATP13A1-notes.md](ATP13A1-notes.md)
- GOA TSV: present - [genes/human/ATP13A1/ATP13A1-goa.tsv](ATP13A1-goa.tsv)
- UniProt record: present - [genes/human/ATP13A1/ATP13A1-uniprot.txt](ATP13A1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATP13A1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATP13A1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP13A1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATP13A1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATP13A1/ATP13A1-deep-research-falcon.md](ATP13A1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATP13A1 is a multi-pass endoplasmic-reticulum membrane P5A-type P-type ATPase that functions as an ATP-dependent transmembrane-helix dislocase. It recognizes moderately hydrophobic terminal transmembrane segments, especially mistargeted mitochondrial tail-anchored proteins and related terminal helices, and extracts them from the ER membrane to help maintain organelle protein localization and ER membrane protein quality control. Early work connected the yeast ortholog Spf1 and human ATP13A1 to manganese-dependent ER phenotypes, but later biochemical and structural studies support transmembrane-helix dislocation rather than direct cation transport as the principal molecular function.
- Existing/core annotation action counts: ACCEPT: 14; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 7; REMOVE: 5

## PN Consistency Summary

- **Consistency:** Deep research (falcon), review YAML, and PN are mutually consistent on the modern model: ATP13A1 is a P5A-ATPase **transmembrane-helix dislocase** (GO:0140567 / GO:0140569), not a cation pump. The review aggressively (and defensibly) REMOVEs the legacy Mn2+/cation-transport annotations (GO:0071421, GO:0098655, GO:0034220, GO:0015410, GO:0006874) and MODIFYs the P-type-transporter terms to dislocase. No internal contradictions.
- **PN story / NEW pressure:** The PN leaf names exactly the gene's core role ("removal of misinserted TM proteins") and is left no_mapping (correct — too heterogeneous). No NEW GO pressure: the specific role is already fully captured by existing GO:0140567 + GO:0140569 (both ACCEPTed, with IDA support). proposed_new_terms is empty. **Already captured.**
- **Evidence alignment:** PN dossier carries no reference titles for this gene; review anchors on PMID:32973005 (P5A dislocase), PMID:36264797 (MTCH2/ER dislocase), PMID:24392018 (ER localization). No divergence to reconcile.
- **Verdict:** CONSISTENT — no NEW term warranted; PN class projection (protein transport) is broader-but-harmless. No edits required.

## Full Consistency Review

- **UniProt:** Q9HD20 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE
- **PN placement:** `ER proteostasis|Protein transport|Removal of misinserted transmembrane proteins` (group, no_mapping); **PN-node mapping:** propagating term comes from the parent *class* `ER proteostasis|Protein transport` = mapped, ok_for_propagation_to_go, GO:0015031 protein transport (new_to_goa, confirmed absent from goa.tsv).
- **Consistency:** Deep research (falcon), review YAML, and PN are mutually consistent on the modern model: ATP13A1 is a P5A-ATPase **transmembrane-helix dislocase** (GO:0140567 / GO:0140569), not a cation pump. The review aggressively (and defensibly) REMOVEs the legacy Mn2+/cation-transport annotations (GO:0071421, GO:0098655, GO:0034220, GO:0015410, GO:0006874) and MODIFYs the P-type-transporter terms to dislocase. No internal contradictions.
- **PN story / NEW pressure:** The PN leaf names exactly the gene's core role ("removal of misinserted TM proteins") and is left no_mapping (correct — too heterogeneous). No NEW GO pressure: the specific role is already fully captured by existing GO:0140567 + GO:0140569 (both ACCEPTed, with IDA support). proposed_new_terms is empty. **Already captured.**
- **Mapping strategy:** Gene does not change the node. The only projected term, GO:0015031 protein transport, derives from the broad *class* node and is far broader than the gene's dislocase function — it is a generic umbrella, not a claim about ATP13A1's specific activity. Acceptable as a class-level propagation but uninformative for this gene; the gene-specific terms live in the review, not the projection.
- **Evidence alignment:** PN dossier carries no reference titles for this gene; review anchors on PMID:32973005 (P5A dislocase), PMID:36264797 (MTCH2/ER dislocase), PMID:24392018 (ER localization). No divergence to reconcile.
- **Verdict:** CONSISTENT — no NEW term warranted; PN class projection (protein transport) is broader-but-harmless. No edits required.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATP13A1/ATP13A1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Protein transport | Removal of misinserted transmembrane proteins
- UniProt: Q9HD20
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [group] ER proteostasis|Protein transport|Removal of misinserted transmembrane proteins
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [class] ER proteostasis|Protein transport
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0015031 protein transport]
        rationale: The PN ER Protein transport class groups ER-targeting and ER-insertion pathways. GO protein transport is the appropriate propagation target, while the source class remains ER-specific and broader than any single GO transport subtype.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0015031 protein transport | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Protein transport

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
