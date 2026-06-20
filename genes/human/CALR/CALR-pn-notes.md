# CALR PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P27797
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CALR/CALR-ai-review.yaml](CALR-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CALR/CALR-ai-review.html](CALR-ai-review.html)
- Gene notes: present - [genes/human/CALR/CALR-notes.md](CALR-notes.md)
- GOA TSV: present - [genes/human/CALR/CALR-goa.tsv](CALR-goa.tsv)
- UniProt record: present - [genes/human/CALR/CALR-uniprot.txt](CALR-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CALR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CALR.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALR.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CALR.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/CALR/CALR-deep-research-falcon.md](CALR-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: Calreticulin (CALR) is the soluble endoplasmic reticulum-luminal lectin chaperone that, together with the membrane-bound paralog calnexin, constitutes the central calnexin/calreticulin cycle of ER glycoprotein quality control. Its globular lectin domain binds monoglucosylated N-glycans (Glc1Man9GlcNAc2) on nearly all nascent glycoproteins, while its extended proline-rich P domain recruits the oxidoreductase ERp57 (PDIA3) and the peptidyl-prolyl isomerase cyclophilin B to promote folding, oligomeric assembly, and retention of incorrectly folded glycoproteins, triaging terminally misfolded clients toward degradation. Calreticulin is a major high-capacity, low-affinity calcium-binding protein that regulates ER calcium storage and homeostasis. It is a key chaperone in the major histocompatibility complex (MHC) class I peptide loading complex, where it stabilizes peptide-receptive MHC I and couples optimal epitope selection to glycan processing. Beyond the ER, calreticulin has well-documented secondary roles: a cell-surface and extracellular "eat-me" signal that promotes phagocytic clearance of apoptotic and stressed cells (immunogenic cell death), C1q/complement interactions, and additional context-specific cytosolic and nuclear activities.
- Existing/core annotation action counts: ACCEPT: 43; KEEP_AS_NON_CORE: 69; MARK_AS_OVER_ANNOTATED: 53

## PN Consistency Summary

- **Consistency:** Biology consistent across review, notes, deep-research, and PN — calreticulin is the soluble ER-luminal lectin chaperone of the CNX/CRT cycle binding monoglucosylated N-glycans, also the major ER Ca2+ buffer and an MHC-I PLC component. As with CANX, the PROJECTED GO term conflicts with this role.
- **PN story / NEW pressure:** GO:0006487 (VERIFIED real) = the process of ADDING the N-glycan; calreticulin binds the pre-formed glycan, it is not a glycosyltransferase. The review correctly represents function as GO:0030246 carbohydrate binding (ACCEPT), GO:0044183 protein folding chaperone, GO:0006457 protein folding, GO:0036503 ERAD, plus Ca2+ binding and MHC-I PLC roles. GO:0006487 absent from CALR GOA (confirmed). Conclude: OVER-REACHES — same category error as CANX; do NOT add.
- **Evidence alignment:** PN node carries no reference titles; review well-evidenced (PMID:15474971 review, PMID:35948544 PLC structure, PMID:17563366 insulin-receptor chaperoning, PMID:10358038 surface CALR). Review also flags two wrong-gene reference mis-assignments at source (PMID:21705382→Bcl2l10; PMID:21590275→CALR3) — unrelated to the PN mapping but worth noting for REF hygiene. No shared evidence supports an N-glycosylation-process claim.
- **Verdict:** OVER-REACHES — reject projected GO:0006487 for CALR (true lectin-chaperone function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CALR; re-map the shared "Lectin chaperone" type node to a binding/chaperone term (GO:0030246 / GO:0036503), covering CALR+CANX together.

## Full Consistency Review

- **UniProt:** P27797 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (exhaustive; ~80 annotations, notes + falcon deep-research present)
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type (Lectin chaperone)→no_mapping; group (N-glycosylation system)→GO:0006487 protein N-linked glycosylation (mapped/ok_for_propagation); class/branch→no_mapping. (Identical node + mapping to CANX, its membrane-bound paralog.)
- **Consistency:** Biology consistent across review, notes, deep-research, and PN — calreticulin is the soluble ER-luminal lectin chaperone of the CNX/CRT cycle binding monoglucosylated N-glycans, also the major ER Ca2+ buffer and an MHC-I PLC component. As with CANX, the PROJECTED GO term conflicts with this role.
- **PN story / NEW pressure:** GO:0006487 (VERIFIED real) = the process of ADDING the N-glycan; calreticulin binds the pre-formed glycan, it is not a glycosyltransferase. The review correctly represents function as GO:0030246 carbohydrate binding (ACCEPT), GO:0044183 protein folding chaperone, GO:0006457 protein folding, GO:0036503 ERAD, plus Ca2+ binding and MHC-I PLC roles. GO:0006487 absent from CALR GOA (confirmed). Conclude: OVER-REACHES — same category error as CANX; do NOT add.
- **Mapping strategy:** Same fix as CANX — the lectin-chaperone members of the "N-glycosylation system" group should not inherit the enzymatic GO:0006487; the "Lectin chaperone" type node should carry a binding/chaperone mapping instead. This is one shared correction covering both CALR and CANX.
- **Evidence alignment:** PN node carries no reference titles; review well-evidenced (PMID:15474971 review, PMID:35948544 PLC structure, PMID:17563366 insulin-receptor chaperoning, PMID:10358038 surface CALR). Review also flags two wrong-gene reference mis-assignments at source (PMID:21705382→Bcl2l10; PMID:21590275→CALR3) — unrelated to the PN mapping but worth noting for REF hygiene. No shared evidence supports an N-glycosylation-process claim.
- **Verdict:** OVER-REACHES — reject projected GO:0006487 for CALR (true lectin-chaperone function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CALR; re-map the shared "Lectin chaperone" type node to a binding/chaperone term (GO:0030246 / GO:0036503), covering CALR+CANX together.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CALR/CALR-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: P27797
- In branches: ER
- PN-node mapping records (path + ancestors):
    - [type] ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [group] ER proteostasis|Glycoproteostasis|N-glycosylation system
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0006487 protein N-linked glycosylation]
        rationale: This PN group captures the ER N-glycosylation machinery that installs and processes N-linked glycans during proteostasis. GO protein N-linked glycosylation is the best current propagation target in the local cache.
    - [class] ER proteostasis|Glycoproteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN category rather than a single GO class. The member genes span multiple activities, complexes, or contexts, so direct propagation from this node would overstate the shared biology.
    - [branch] ER proteostasis
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a top-level PN branch. This is a systems/taxonomy umbrella, not a direct GO assertion; narrower child curations carry any propagating GO mappings.

## Projected GO annotations (1)
- GO:0006487 protein N-linked glycosylation | scope=ok_for_propagation_to_go | goa_status=new_to_goa | from=ER proteostasis|Glycoproteostasis|N-glycosylation system

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
