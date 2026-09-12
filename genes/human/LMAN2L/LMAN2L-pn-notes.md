# LMAN2L PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H0V9
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LMAN2L/LMAN2L-ai-review.yaml](LMAN2L-ai-review.yaml)
- AIGR review HTML: missing - genes/human/LMAN2L/LMAN2L-ai-review.html
- Gene notes: present - [genes/human/LMAN2L/LMAN2L-notes.md](LMAN2L-notes.md)
- GOA TSV: present - [genes/human/LMAN2L/LMAN2L-goa.tsv](LMAN2L-goa.tsv)
- UniProt record: present - [genes/human/LMAN2L/LMAN2L-uniprot.txt](LMAN2L-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN2L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN2L.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN2L.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN2L.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/LMAN2L/LMAN2L-deep-research-falcon.md](LMAN2L-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: LMAN2L (VIPL, "VIP36-like protein") is an ER-resident L-type (leguminous/ConA-like) lectin and a paralog of VIP36/LMAN2 and ERGIC-53/LMAN1. It is a single-pass type I membrane glycoprotein whose N-terminal luminal L-type lectin carbohydrate-recognition domain binds high-mannose glycans (D-mannose) and whose short cytoplasmic tail carries an RKR di-arginine ER-retention signal. Unlike the cycling lectins VIP36 and ERGIC-53, LMAN2L is predominantly a non-cycling resident of the endoplasmic reticulum, with a minor Golgi pool. It is not a glycosidase and has no catalytic activity; rather it is proposed to regulate ER export of a subset of glycoproteins and to act as a regulator of ERGIC-53, with overexpression redistributing ERGIC-53 to the ER and knockdown slowing glycoprotein secretion. LMAN2L is a neurodevelopmental disease gene: variants cause autosomal recessive (MRT52) and autosomal dominant (MRD69) intellectual developmental disorders.
- Existing/core annotation action counts: ACCEPT: 9; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation consistent. VIPL is an L-type lectin, NOT a glycosidase — matching the "Lectin chaperone" type. Distinctive vs its cycling paralogs: it is a *non-cycling ER-resident* (RKR retention) regulator of ER export / regulator of ERGIC-53 (core BP GO:0006888, GO:0015031). D-mannose binding accepted as a homology/CRD-based MF (no direct binding assay for VIPL itself — review states this clearly). No contradictions.
- **PN story / NEW pressure:** No NEW GO pressure. ER-export-receptor / ERGIC-53-regulator role is captured by transport terms; a candidate physiological client (ITGA6, via PMID:38687323) is noted but single-paper/candidate-stage and the review correctly did not mint a term. Conclude: already captured.
- **Evidence alignment:** PN dossier is mapping-only. Review evidence centers on PMID:12609988 and PMID:12878160 (PubMed-verified primary papers) plus disease PMIDs (26566883, 31020005, 37667433) and HCMV/TRC8 (38687323). No bibliographic conflict; divergence is conceptual (group biosynthesis term vs. lectin/ER-export function).
- **Verdict:** Review strong and PN-consistent (ER-resident lectin/export regulator, not a mannosidase). Inherited group→GO:0006487 projection is an over-reach.

## Full Consistency Review

- **UniProt:** Q9H0V9 (VIP36-like protein / VIPL) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE, thorough (two primary characterizations + disease + Falcon).
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type "Lectin chaperone" no_mapping; group "N-glycosylation system" mapped→GO:0006487 (protein N-linked glycosylation, ok_for_propagation, new_to_goa); class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation consistent. VIPL is an L-type lectin, NOT a glycosidase — matching the "Lectin chaperone" type. Distinctive vs its cycling paralogs: it is a *non-cycling ER-resident* (RKR retention) regulator of ER export / regulator of ERGIC-53 (core BP GO:0006888, GO:0015031). D-mannose binding accepted as a homology/CRD-based MF (no direct binding assay for VIPL itself — review states this clearly). No contradictions.
- **PN story / NEW pressure:** No NEW GO pressure. ER-export-receptor / ERGIC-53-regulator role is captured by transport terms; a candidate physiological client (ITGA6, via PMID:38687323) is noted but single-paper/candidate-stage and the review correctly did not mint a term. Conclude: already captured.
- **Mapping strategy:** **Group→GO:0006487 (new_to_goa) over-reaches** as for the other lectins — VIPL reads/exports high-mannose glycoproteins; it does not perform N-linked glycosylation. Additionally, VIPL is predominantly ER-resident (not a classic ERGIC cycler), so even the family-level "N-glycosylation system" framing fits it least well. PN node correct to leave "Lectin chaperone" unmapped; projected term should not propagate.
- **Evidence alignment:** PN dossier is mapping-only. Review evidence centers on PMID:12609988 and PMID:12878160 (PubMed-verified primary papers) plus disease PMIDs (26566883, 31020005, 37667433) and HCMV/TRC8 (38687323). No bibliographic conflict; divergence is conceptual (group biosynthesis term vs. lectin/ER-export function).
- **Verdict:** Review strong and PN-consistent (ER-resident lectin/export regulator, not a mannosidase). Inherited group→GO:0006487 projection is an over-reach.
**Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN2L/VIPL — it is an ER-resident high-mannose lectin / ER-export regulator, not an N-glycosylation enzyme; flag the "N-glycosylation system" group node as over-broad (and a poor fit for a non-cycling ER resident).

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/LMAN2L/LMAN2L-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: Q9H0V9
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
