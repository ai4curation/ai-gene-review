# TRAPPC12 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8WVT3
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC12/TRAPPC12-ai-review.yaml](TRAPPC12-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC12/TRAPPC12-ai-review.html](TRAPPC12-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC12/TRAPPC12-notes.md](TRAPPC12-notes.md)
- GOA TSV: present - [genes/human/TRAPPC12/TRAPPC12-goa.tsv](TRAPPC12-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC12/TRAPPC12-uniprot.txt](TRAPPC12-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC12.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC12.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC12.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: TRAPPC12/TRAMM/TTC-15 is a moonlighting metazoan TRAPP/TRAPPIII-associated protein. In interphase it participates in TRAPP-dependent early secretory traffic between ER, ERGIC, and Golgi. During mitosis it leaves the TRAPP context and supports chromosome congression, kinetochore stability, and CENP-E recruitment. Its shared cellular roles are TRAPP/TRAPPII/TRAPPIII complex membership and TRAPP/RAB1 trafficking; direct TRAPPC12-specific autophagy evidence is limited.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 3

## PN Consistency Summary

- **Consistency:** Consistent. Notes and YAML agree on two directly-supported tracks — interphase TRAPP/TRAPPIII early-secretory traffic, and a moonlighting mitotic kinetochore/CENP-E role (PMID:25918224) — and explicitly **decline** a TRAPPC12-specific autophagy annotation ("I am not adding a direct autophagy annotation… autophagy is represented by TRAPPIII/RAB1 context only"). This matches the PN complex-only mapping. No contradictions.
- **PN story / NEW pressure:** PN restricts to GO:0030008 membership; unlike TRAPPC11, TRAPPC12 has **no** direct gene-specific autophagy evidence, so the review correctly does not mint an autophagy BP (`proposed_new_terms: []`). GO:0030008 is verified real and already in GOA. The mitotic moonlighting functions (GO:0051310, GO:0090234, GO:1905342) are outside the PN scope and correctly flagged as non-PN-propagation targets. Conclude: **already captured; no NEW warranted — good asymmetry vs TRAPPC11.**
- **Evidence alignment:** Overlap on TRAPP: PN cites PMID:27066478 + Frontiers review = review core. Review enriches with PMID:21525244 (TRAPP ID), 28777934 (CDG/encephalopathy), 25918224 (mitosis) — none in PN, all consistent. (Notes flag a spurious PANTHER PTHR21581 "D-Ala-D-Ala carboxypeptidase" artifact, correctly not used.)
- **Verdict:** Fully consistent; correctly conservative on autophagy. No edits needed.

## Full Consistency Review

- **UniProt:** Q8WVT3 (TRAMM/TTC-15) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagophore initiation and elongation → Autophagy component recruitment to autophagophore → TRAPP complex component` (1 row, ALP) ; **PN-node mapping:** leaf type=`mapped`/`ok_for_propagation`→GO:0030008 TRAPP complex; group=`no_mapping`; class=`context_only`/`too_broad`→GO:0016236 macroautophagy; branch=`no_mapping`. **Projects GO:0030008 (already_in_goa_exact).**
- **Consistency:** Consistent. Notes and YAML agree on two directly-supported tracks — interphase TRAPP/TRAPPIII early-secretory traffic, and a moonlighting mitotic kinetochore/CENP-E role (PMID:25918224) — and explicitly **decline** a TRAPPC12-specific autophagy annotation ("I am not adding a direct autophagy annotation… autophagy is represented by TRAPPIII/RAB1 context only"). This matches the PN complex-only mapping. No contradictions.
- **PN story / NEW pressure:** PN restricts to GO:0030008 membership; unlike TRAPPC11, TRAPPC12 has **no** direct gene-specific autophagy evidence, so the review correctly does not mint an autophagy BP (`proposed_new_terms: []`). GO:0030008 is verified real and already in GOA. The mitotic moonlighting functions (GO:0051310, GO:0090234, GO:1905342) are outside the PN scope and correctly flagged as non-PN-propagation targets. Conclude: **already captured; no NEW warranted — good asymmetry vs TRAPPC11.**
- **Mapping strategy:** Gene does not change the node (GO:0030008 correct, macroautophagy correctly held at `context_only`). The mitotic functions are appropriately excluded from the shared TRAPP bucket.
- **Evidence alignment:** Overlap on TRAPP: PN cites PMID:27066478 + Frontiers review = review core. Review enriches with PMID:21525244 (TRAPP ID), 28777934 (CDG/encephalopathy), 25918224 (mitosis) — none in PN, all consistent. (Notes flag a spurious PANTHER PTHR21581 "D-Ala-D-Ala carboxypeptidase" artifact, correctly not used.)
- **Verdict:** Fully consistent; correctly conservative on autophagy. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC12/TRAPPC12-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q8WVT3
- In branches: ALP
- Notes: TRAPP III complex, specific subunit. The TRAPP complex serves as a GEF for RAB1. Involved in ATG9 and ATG2 trafficking
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
