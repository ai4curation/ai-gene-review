# TRAPPC1 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9Y5R8
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC1/TRAPPC1-ai-review.yaml](TRAPPC1-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC1/TRAPPC1-ai-review.html](TRAPPC1-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC1/TRAPPC1-notes.md](TRAPPC1-notes.md)
- GOA TSV: present - [genes/human/TRAPPC1/TRAPPC1-goa.tsv](TRAPPC1-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC1/TRAPPC1-uniprot.txt](TRAPPC1-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC1.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC1.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC1.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC1 is a small core subunit of the transport protein particle (TRAPP) complex. It contributes to TRAPP complex architecture and complex-level RAB1 guanine-nucleotide exchange/vesicle-trafficking functions, especially ER-to-Golgi vesicle-mediated transport. Autophagy component recruitment is best understood through TRAPP/TRAPPII/TRAPPIII complex membership rather than independent TRAPPC1 activity.
- Existing/core annotation action counts: ACCEPT: 15; MARK_AS_OVER_ANNOTATED: 6; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Fully consistent. Notes, review YAML and PN converge on TRAPP-complex membership as the strongest gene-level annotation; review ACCEPTs GO:0030008 (IBA+IEA) and TRAPPII/TRAPPIII memberships, and explicitly declines a broad autophagy BP ("avoid adding a broad autophagy BP for TRAPPC1"). No contradictions.
- **PN story / NEW pressure:** PN's autophagophore-recruitment story is deliberately resolved to **complex membership only** (GO:0030008, verified real, already in GOA). Review concurs and routes autophagy to TRAPPIII context (GO:1990072) rather than a BP, citing PMID:27066478 "the connection of the mammalian TRAPP III complex to autophagy is currently not clear." `proposed_new_terms: []`. Conclude: **already captured; no NEW warranted.**
- **Evidence alignment:** Overlap. PN cites the Frontiers "TRAPP Complexes in Secretion and Autophagy" review = review's PMID:27066478 (core). Review enriches with structural (PMID:16828797) and Reactome RAB1-GEF/ER-Golgi evidence PN does not list.
- **Verdict:** Fully consistent, conservative, well-curated. No edits needed.

## Full Consistency Review

- **UniProt:** Q9Y5R8 (TRAPP subunit 1 / Mum2) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagophore initiation and elongation → Autophagy component recruitment to autophagophore → TRAPP complex component` (1 row, ALP) ; **PN-node mapping:** leaf type=`mapped`/`ok_for_propagation`→GO:0030008 TRAPP complex; group=`no_mapping`; class=`context_only`/`too_broad`→GO:0016236 macroautophagy; branch=`no_mapping`. **Projects GO:0030008 (already_in_goa_exact).**
- **Consistency:** Fully consistent. Notes, review YAML and PN converge on TRAPP-complex membership as the strongest gene-level annotation; review ACCEPTs GO:0030008 (IBA+IEA) and TRAPPII/TRAPPIII memberships, and explicitly declines a broad autophagy BP ("avoid adding a broad autophagy BP for TRAPPC1"). No contradictions.
- **PN story / NEW pressure:** PN's autophagophore-recruitment story is deliberately resolved to **complex membership only** (GO:0030008, verified real, already in GOA). Review concurs and routes autophagy to TRAPPIII context (GO:1990072) rather than a BP, citing PMID:27066478 "the connection of the mammalian TRAPP III complex to autophagy is currently not clear." `proposed_new_terms: []`. Conclude: **already captured; no NEW warranted.**
- **Mapping strategy:** Gene does not change the node. The PN node correctly avoids projecting macroautophagy (the documented "TRAPP-like overpropagation" precedent the rationale itself names) and restricts to the CC GO:0030008. Status/scope right; not broader than the review.
- **Evidence alignment:** Overlap. PN cites the Frontiers "TRAPP Complexes in Secretion and Autophagy" review = review's PMID:27066478 (core). Review enriches with structural (PMID:16828797) and Reactome RAB1-GEF/ER-Golgi evidence PN does not list.
- **Verdict:** Fully consistent, conservative, well-curated. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC1/TRAPPC1-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q9Y5R8
- In branches: ALP
- Notes: TRAPP complex, core subunit. The TRAPP complex serves as a GEF for RAB1. Involved in ATG9 and ATG2 trafficking
- PN references (titles):
    - Membrane Trafficking in Autophagy - ScienceDirect
    - Frontiers | TRAPP Complexes in Secretion and Autophagy | Cell and Developmental Biology (frontiersin.org)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0030008 TRAPP complex]
        rationale: This PN leaf is a curated component bucket for TRAPP subunits used in autophagophore recruitment. The matching GO cellular-component term is TRAPP complex, and the member genes already converge strongly on that assignment in existing GOA.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0030008 TRAPP complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Autophagy component recruitment to autophagophore|TRAPP complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
