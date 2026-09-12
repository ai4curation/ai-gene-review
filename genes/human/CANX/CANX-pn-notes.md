# CANX PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: P27824
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-06
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CANX/CANX-ai-review.yaml](CANX-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CANX/CANX-ai-review.html](CANX-ai-review.html)
- Gene notes: present - [genes/human/CANX/CANX-notes.md](CANX-notes.md)
- GOA TSV: present - [genes/human/CANX/CANX-goa.tsv](CANX-goa.tsv)
- UniProt record: present - [genes/human/CANX/CANX-uniprot.txt](CANX-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CANX.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CANX.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CANX.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CANX.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: Calnexin (CANX) is a type I single-pass integral membrane lectin chaperone of the endoplasmic reticulum and, together with the soluble paralog calreticulin, forms the central calnexin/calreticulin cycle of ER glycoprotein quality control. Its luminal globular lectin domain binds monoglucosylated N-glycans (Glc1Man9GlcNAc2) on nascent glycoproteins, while its extended proline-rich P domain (arm) recruits the oxidoreductase ERp57 (PDIA3) and the peptidyl-prolyl isomerase cyclophilin B (PPIB) to assist oxidative folding and assembly. Calnexin retains incompletely or incorrectly folded glycoproteins in the ER and triages terminally misfolded clients toward ER-associated degradation. It is a calcium-binding protein that contributes to ER calcium homeostasis. Calnexin is palmitoylated by ZDHHC6 on its cytoplasmic cysteines, which targets it to the perinuclear rough ER and couples it to the ribosome-translocon complex for co-translational capture of newly synthesized glycoproteins. It participates in MHC class I heavy-chain folding/assembly and in the maturation of many specific clients (e.g. ion channels, receptors, serpins).
- Existing/core annotation action counts: ACCEPT: 42; KEEP_AS_NON_CORE: 5; MARK_AS_OVER_ANNOTATED: 42

## PN Consistency Summary

- **Consistency:** Internally consistent on biology — review, notes, and PN all describe calnexin as the membrane-bound lectin chaperone of the CNX/CRT cycle binding monoglucosylated N-glycans. BUT the PROJECTED GO term is inconsistent with calnexin's molecular role (see below).
- **PN story / NEW pressure:** GO:0006487 is VERIFIED real but its definition is "a process in which a carbohydrate unit is ADDED to a protein via the N4 atom of asparagine" — i.e. the catalytic glycan-transfer step (OST machinery). Calnexin RECOGNIZES/BINDS the already-installed glycan; it does not perform N-glycosylation. The review correctly captures the true function as GO:0030246 carbohydrate binding, GO:0044183 protein folding chaperone, GO:0034975 protein folding in ER, GO:0036503 ERAD. GO:0006487 is absent from CANX GOA (confirmed). Conclude: OVER-REACHES — projecting GO:0006487 to a lectin chaperone is a category error from a mixed "N-glycosylation system" container node; do NOT add.
- **Evidence alignment:** PN node carries no reference titles; review is heavily evidenced (PMID:22314232 palmitoyl-translocon, PMID:8136357 cloning/Ca2+, PMID:35948544/Reactome MHC-I, many IDA ER-localization). No citation conflict, but no shared evidence supports the N-glycosylation-process claim.
- **Verdict:** OVER-REACHES — projected GO:0006487 mis-assigns an enzymatic process to a lectin chaperone; reject for CANX (true function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CANX; re-map the "Lectin chaperone" type node to a binding/chaperone term (e.g. GO:0030246 carbohydrate binding / GO:0036503 ERAD pathway).

## Full Consistency Review

- **UniProt:** P27824 · **batch:** proteostasis-batch-2026-06-06 · **review status:** COMPLETE (exhaustive; ~90 annotations reviewed, notes present)
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type (Lectin chaperone)→no_mapping; group (N-glycosylation system)→GO:0006487 protein N-linked glycosylation (mapped/ok_for_propagation); class/branch→no_mapping.
- **Consistency:** Internally consistent on biology — review, notes, and PN all describe calnexin as the membrane-bound lectin chaperone of the CNX/CRT cycle binding monoglucosylated N-glycans. BUT the PROJECTED GO term is inconsistent with calnexin's molecular role (see below).
- **PN story / NEW pressure:** GO:0006487 is VERIFIED real but its definition is "a process in which a carbohydrate unit is ADDED to a protein via the N4 atom of asparagine" — i.e. the catalytic glycan-transfer step (OST machinery). Calnexin RECOGNIZES/BINDS the already-installed glycan; it does not perform N-glycosylation. The review correctly captures the true function as GO:0030246 carbohydrate binding, GO:0044183 protein folding chaperone, GO:0034975 protein folding in ER, GO:0036503 ERAD. GO:0006487 is absent from CANX GOA (confirmed). Conclude: OVER-REACHES — projecting GO:0006487 to a lectin chaperone is a category error from a mixed "N-glycosylation system" container node; do NOT add.
- **Mapping strategy:** The group node "N-glycosylation system" lumps the OST/glycan-installing/processing enzymes with the lectin chaperones that read the glycan; a single GO:0006487 mapping over-annotates the lectin-chaperone members (CANX, CALR). Recommend the lectin-chaperone TYPE node carry a binding/chaperone mapping (e.g. GO:0030246 carbohydrate binding or GO:0006457/GO:0036503) rather than inheriting the enzymatic process term.
- **Evidence alignment:** PN node carries no reference titles; review is heavily evidenced (PMID:22314232 palmitoyl-translocon, PMID:8136357 cloning/Ca2+, PMID:35948544/Reactome MHC-I, many IDA ER-localization). No citation conflict, but no shared evidence supports the N-glycosylation-process claim.
- **Verdict:** OVER-REACHES — projected GO:0006487 mis-assigns an enzymatic process to a lectin chaperone; reject for CANX (true function already captured). **Recommended edits:** [MAP] do not propagate GO:0006487 to CANX; re-map the "Lectin chaperone" type node to a binding/chaperone term (e.g. GO:0030246 carbohydrate binding / GO:0036503 ERAD pathway).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-06
- review_yaml: genes/human/CANX/CANX-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: P27824
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
