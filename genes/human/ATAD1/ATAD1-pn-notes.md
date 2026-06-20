# ATAD1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NBU5
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-03 (PR 1372)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/ATAD1/ATAD1-ai-review.yaml](ATAD1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/ATAD1/ATAD1-ai-review.html](ATAD1-ai-review.html)
- Gene notes: present - [genes/human/ATAD1/ATAD1-notes.md](ATAD1-notes.md)
- GOA TSV: present - [genes/human/ATAD1/ATAD1-goa.tsv](ATAD1-goa.tsv)
- UniProt record: present - [genes/human/ATAD1/ATAD1-uniprot.txt](ATAD1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/ATAD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/ATAD1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATAD1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/ATAD1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/ATAD1/ATAD1-deep-research-falcon.md](ATAD1-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: ATAD1 is a conserved single-pass AAA+ ATPase anchored mainly in the mitochondrial outer membrane, with additional evidence for peroxisomal membrane localization. It functions as an ATP-dependent membrane protein dislocase that extracts mistargeted tail-anchored membrane proteins from the mitochondrial outer membrane so that they can be cleared, thereby protecting mitochondrial integrity. In neurons, ATAD1/Thorase has a separate disease-relevant role in AMPA receptor complex disassembly and postsynaptic receptor trafficking, but the conserved molecular activity remains ATP-driven membrane protein extraction.
- Existing/core annotation action counts: ACCEPT: 8; KEEP_AS_NON_CORE: 15; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 3; NEW: 1; REMOVE: 3

## PN Consistency Summary

- **Consistency:** Consistent. Deep research, notes, review YAML agree ATAD1/Msp1 is a hexameric OMM AAA+ extractase/dislocase that removes mislocalized tail-anchored proteins (PEX26/GOS28) and the BH3-only protein BIM, for rerouting or degradation. Review core = GO:0140567 (membrane protein dislocase) + GO:0140570 (extraction of mislocalized protein from mitochondrial OM). The PN class is degradation-centric; ATAD1's sharper mechanism is extraction, but degradation is a real downstream outcome.
- **PN story / NEW pressure:** PN projects GO:0035694 (mitochondrial protein catabolic process), absent from ATAD1 GOA. The review **accepted it as NEW (TAS)** — notably GO:0140570 is NOT a subclass of GO:0035694 (verified via OLS: GO:0140570 sits under establishment-of-protein-localization, not catabolic process), so the two are orthogonal, not redundant. Adding GO:0035694 is defensible (degradation outcome supported by PMID:24843043) though broader/less mechanistic than GO:0140570. **Conclude: ADD already done in-review** (accepted NEW); both terms real and complementary.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:24843043 (extraction/degradation of TA proteins) plus new human primaries (PMID:36409067 BIM; PMID:35550246 cryo-EM) — all reinforce the dislocase core. No citation conflicts.
- **Verdict:** Consistent; PN GO:0035694 is real, complementary to GO:0140570, and already added as NEW. No edits warranted.

## Full Consistency Review

- **UniProt:** Q8NBU5 · **batch:** proteostasis-batch-2026-06-03 · **review status:** COMPLETE (Falcon DR present)
- **PN placement:** `Mitochondrial proteostasis|Organelle-specific protein degradation|mitoCPR pathway` ; **PN-node mapping:** group(mitoCPR)=no_mapping; class(Organelle-specific protein degradation)=mapped/ok GO:0035694 (mitochondrial protein catabolic process, new_to_goa); branch=no_mapping.
- **Consistency:** Consistent. Deep research, notes, review YAML agree ATAD1/Msp1 is a hexameric OMM AAA+ extractase/dislocase that removes mislocalized tail-anchored proteins (PEX26/GOS28) and the BH3-only protein BIM, for rerouting or degradation. Review core = GO:0140567 (membrane protein dislocase) + GO:0140570 (extraction of mislocalized protein from mitochondrial OM). The PN class is degradation-centric; ATAD1's sharper mechanism is extraction, but degradation is a real downstream outcome.
- **PN story / NEW pressure:** PN projects GO:0035694 (mitochondrial protein catabolic process), absent from ATAD1 GOA. The review **accepted it as NEW (TAS)** — notably GO:0140570 is NOT a subclass of GO:0035694 (verified via OLS: GO:0140570 sits under establishment-of-protein-localization, not catabolic process), so the two are orthogonal, not redundant. Adding GO:0035694 is defensible (degradation outcome supported by PMID:24843043) though broader/less mechanistic than GO:0140570. **Conclude: ADD already done in-review** (accepted NEW); both terms real and complementary.
- **Mapping strategy:** ATAD1 mildly supports the class mapping. GO:0035694 is broader than the gene's specific GO:0140570 but, unlike TOMM20-type rejections, it is a distinct degradation axis the review judged worth a conservative NEW. mitoCPR leaf no_mapping is appropriate (human mitoCPR poorly defined). Node status/scope fine.
- **Evidence alignment:** PN row carries no reference titles. Review anchors on PMID:24843043 (extraction/degradation of TA proteins) plus new human primaries (PMID:36409067 BIM; PMID:35550246 cryo-EM) — all reinforce the dislocase core. No citation conflicts.
- **Verdict:** Consistent; PN GO:0035694 is real, complementary to GO:0140570, and already added as NEW. No edits warranted.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-03
- review_yaml: genes/human/ATAD1/ATAD1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Mitochondrial proteostasis | Organelle-specific protein degradation | mitoCPR pathway
- UniProt: Q8NBU5
- In branches: MI
- PN-node mapping records (path + ancestors):
    - [group] Mitochondrial proteostasis|Organelle-specific protein degradation|mitoCPR pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a narrower taxonomy bucket that is already covered by a curated parent mapping or by gene-level annotations. No additional direct GO mapping is appropriate from this node.
    - [class] Mitochondrial proteostasis|Organelle-specific protein degradation
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0035694 mitochondrial protein catabolic process]
        rationale: This PN class groups mitochondrial protein-degradation pathways. GO mitochondrial protein catabolic process is the conservative shared target.
    - [branch] Mitochondrial proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0035694 mitochondrial protein catabolic process | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=Mitochondrial proteostasis|Organelle-specific protein degradation

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
