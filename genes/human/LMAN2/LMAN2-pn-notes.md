# LMAN2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q12907
- AIGR review status: COMPLETE
- Review batch: proteostasis-batch-2026-06-11
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/LMAN2/LMAN2-ai-review.yaml](LMAN2-ai-review.yaml)
- AIGR review HTML: missing - genes/human/LMAN2/LMAN2-ai-review.html
- Gene notes: present - [genes/human/LMAN2/LMAN2-notes.md](LMAN2-notes.md)
- GOA TSV: present - [genes/human/LMAN2/LMAN2-goa.tsv](LMAN2-goa.tsv)
- UniProt record: present - [genes/human/LMAN2/LMAN2-uniprot.txt](LMAN2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/LMAN2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/LMAN2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/LMAN2/LMAN2-deep-research-falcon.md](LMAN2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: LMAN2 (Vesicular integral-membrane protein VIP36; also GP36b, Lectin mannose-binding 2) is a type-I single-pass transmembrane leguminous-type (L-type) lectin of the early secretory pathway. Its lumenal L-type lectin-like (ConA-like) domain binds high-mannose N-glycans in a Ca2+-dependent manner; VIP36 is a carbohydrate-binding sorting receptor, not a glycosidase. It cycles between the endoplasmic reticulum, the ER-Golgi intermediate compartment (ERGIC) and the Golgi apparatus, where it participates in the transport, sorting and quality control of glycoproteins carrying high-mannose glycans. A characterized cargo is alpha1-antitrypsin, whose high-mannose form VIP36 binds and recycles from the Golgi back to the ER, consistent with a role in post-ER quality control. A minor pool of mature VIP36 reaches the plasma membrane, where it can be released by ectodomain shedding; in macrophages this cell-surface/shed VIP36 contributes to the regulation of phagocytosis, a secondary role distinct from its core ER-Golgi lectin function.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 3

## PN Consistency Summary

- **Consistency:** Deep research ↔ review ↔ PN annotation consistent. LMAN2/VIP36 is correctly an L-type (ConA-like) lectin cargo/sorting receptor (D-mannose binding GO:0005537, carbohydrate binding GO:0030246) — NOT a mannosidase, matching the PN "Lectin chaperone" type. Distinctive feature well captured: retrograde Golgi→ER recycling (GO:0006890) in post-ER QC of alpha1-antitrypsin, plus a secondary shed-ectodomain/phagocytosis role kept non-core.
- **PN story / NEW pressure:** No NEW GO pressure; functions are captured (IMP D-mannose binding, retrograde transport, ER-Golgi cycling). Falcon shedding cleavage-site detail (PMID:33796845) refines the already-non-core shedding role only. Conclude: already captured.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence PubMed-verified and centered on PMID:20477988 (the key functional paper), 23701871, 22016386, 15308636. No bibliographic conflict; divergence is conceptual (group term vs. lectin function).
- **Verdict:** Review strong and PN-consistent (lectin, not mannosidase; distinct retrograde-QC angle). Inherited group→GO:0006487 projection is an over-reach for VIP36.

## Full Consistency Review

- **UniProt:** Q12907 (Vesicular integral-membrane protein VIP36) · **batch:** proteostasis-batch-2026-06-11 · **review status:** COMPLETE, thorough (detailed notes + Falcon).
- **PN placement:** `ER proteostasis|Glycoproteostasis|N-glycosylation system|Lectin chaperone` ; **PN-node mapping:** type "Lectin chaperone" no_mapping; group "N-glycosylation system" mapped→GO:0006487 (protein N-linked glycosylation, ok_for_propagation, new_to_goa); class/branch no_mapping.
- **Consistency:** Deep research ↔ review ↔ PN annotation consistent. LMAN2/VIP36 is correctly an L-type (ConA-like) lectin cargo/sorting receptor (D-mannose binding GO:0005537, carbohydrate binding GO:0030246) — NOT a mannosidase, matching the PN "Lectin chaperone" type. Distinctive feature well captured: retrograde Golgi→ER recycling (GO:0006890) in post-ER QC of alpha1-antitrypsin, plus a secondary shed-ectodomain/phagocytosis role kept non-core.
- **PN story / NEW pressure:** No NEW GO pressure; functions are captured (IMP D-mannose binding, retrograde transport, ER-Golgi cycling). Falcon shedding cleavage-site detail (PMID:33796845) refines the already-non-core shedding role only. Conclude: already captured.
- **Mapping strategy:** Same over-reach as LMAN1 — **group→GO:0006487 over-reaches for VIP36**, a glycan-reader/sorter that neither installs nor trims N-glycans. `new_to_goa` would introduce an unsupported biosynthesis assertion. The review's own BP terms (GO:0006888, GO:0006890) are transport/QC, conceptually disjoint from GO:0006487. PN node correctly leaves "Lectin chaperone" unmapped; the inherited group term should not propagate.
- **Evidence alignment:** PN dossier is mapping-only (no titles). Review evidence PubMed-verified and centered on PMID:20477988 (the key functional paper), 23701871, 22016386, 15308636. No bibliographic conflict; divergence is conceptual (group term vs. lectin function).
- **Verdict:** Review strong and PN-consistent (lectin, not mannosidase; distinct retrograde-QC angle). Inherited group→GO:0006487 projection is an over-reach for VIP36.
**Recommended edits:** [MAP] Do not propagate GO:0006487 (protein N-linked glycosylation) to LMAN2/VIP36 — it is a high-mannose glycan-reading sorting receptor (transport/retrograde QC), not an N-linked-glycosylation enzyme; flag the "N-glycosylation system" group node as over-broad.

## PN Dossier Context

- review_batch: proteostasis-batch-2026-06-11
- review_yaml: genes/human/LMAN2/LMAN2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: ER proteostasis | Glycoproteostasis | N-glycosylation system | Lectin chaperone
- UniProt: Q12907
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
