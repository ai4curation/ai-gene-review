# TRAPPC11 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q7Z392
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/TRAPPC11/TRAPPC11-ai-review.yaml](TRAPPC11-ai-review.yaml)
- AIGR review HTML: present - [genes/human/TRAPPC11/TRAPPC11-ai-review.html](TRAPPC11-ai-review.html)
- Gene notes: present - [genes/human/TRAPPC11/TRAPPC11-notes.md](TRAPPC11-notes.md)
- GOA TSV: present - [genes/human/TRAPPC11/TRAPPC11-goa.tsv](TRAPPC11-goa.tsv)
- UniProt record: present - [genes/human/TRAPPC11/TRAPPC11-uniprot.txt](TRAPPC11-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/TRAPPC11.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC11.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/TRAPPC11.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/TRAPPC11/TRAPPC11-deep-research-falcon.md](TRAPPC11-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: TRAPPC11 (C4orf41/Gryzun) is a metazoan TRAPP/TRAPPIII-associated subunit. It stabilizes mammalian TRAPP architecture and contributes to early secretory pathway trafficking between the ER, ERGIC, and Golgi. Patient-cell evidence also supports a TRAPPC11 role in starvation-induced autophagic flux and autophagosome sealing. As a TRAPPIII-associated subunit, TRAPPC11 is connected to TRAPP complex membership, complex-level RAB1 GEF activity, ER-to-Golgi transport, TRAPP complex stability, and autophagosome maturation.
- Existing/core annotation action counts: ACCEPT: 10; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 2; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent, with the review going beyond PN. Falcon deep research (the only one of the six that completed) plus notes and YAML agree on TRAPPIII membership + early-secretory ER/ERGIC/Golgi traffic + TRAPP-stability, AND add a direct autophagy role from PMID:31575891 (patient fibroblasts fail autophagic flux / fail to seal isolation membranes). No contradictions; the review supplements the PN complex-only mapping with a gene-specific autophagy BP.
- **PN story / NEW pressure:** PN restricts to GO:0030008 membership, but TRAPPC11 has direct human autophagy evidence the PN node does not project. Review adds GO:0097352 autophagosome maturation as `NEW` (verified real via OLS; absent from GOA, confirmed). **Caveat (verified):** GO:0097352's definition is "removal of PI3P/Atg8-LC3 after phagophore closure" (a disassembly step), whereas PMID:31575891 describes a failure to *seal/close* isolation membranes — which maps more naturally to GO:0000045 autophagosome assembly. The NEW term direction is defensible but slightly off the cited mechanism. Conclude: **ADD an autophagy BP (defensible), but reconsider GO:0097352 vs GO:0000045 for the sealing/closure phenotype.**
- **Evidence alignment:** Overlap on TRAPP: PN cites PMID:27066478 + Frontiers review = review core. Review enriches with PMID:21525244 (TRAPP identification), 19942856 (Golgi-exit screen), 27862579 (CDG), and 31575891 (autophagy, PN does not list).
- **Verdict:** Consistent; one substantive curation question. **Recommended edits:** in TRAPPC11-ai-review.yaml, reconsider the `NEW` GO:0097352 autophagosome maturation against GO:0000045 autophagosome assembly, since PMID:31575891 evidence concerns isolation-membrane sealing/closure, not the post-closure PI3P/LC3-removal step GO:0097352 defines.

## Full Consistency Review

- **UniProt:** Q7Z392 (C4orf41/Gryzun) · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `Autophagy-Lysosome Pathway → Autophagophore initiation and elongation → Autophagy component recruitment to autophagophore → TRAPP complex component` (1 row, ALP) ; **PN-node mapping:** leaf type=`mapped`/`ok_for_propagation`→GO:0030008 TRAPP complex; group=`no_mapping`; class=`context_only`/`too_broad`→GO:0016236 macroautophagy; branch=`no_mapping`. **Projects GO:0030008 (already_in_goa_exact).**
- **Consistency:** Consistent, with the review going beyond PN. Falcon deep research (the only one of the six that completed) plus notes and YAML agree on TRAPPIII membership + early-secretory ER/ERGIC/Golgi traffic + TRAPP-stability, AND add a direct autophagy role from PMID:31575891 (patient fibroblasts fail autophagic flux / fail to seal isolation membranes). No contradictions; the review supplements the PN complex-only mapping with a gene-specific autophagy BP.
- **PN story / NEW pressure:** PN restricts to GO:0030008 membership, but TRAPPC11 has direct human autophagy evidence the PN node does not project. Review adds GO:0097352 autophagosome maturation as `NEW` (verified real via OLS; absent from GOA, confirmed). **Caveat (verified):** GO:0097352's definition is "removal of PI3P/Atg8-LC3 after phagophore closure" (a disassembly step), whereas PMID:31575891 describes a failure to *seal/close* isolation membranes — which maps more naturally to GO:0000045 autophagosome assembly. The NEW term direction is defensible but slightly off the cited mechanism. Conclude: **ADD an autophagy BP (defensible), but reconsider GO:0097352 vs GO:0000045 for the sealing/closure phenotype.**
- **Mapping strategy:** Gene does not change the TRAPP node (GO:0030008 correct). The autophagy addition is gene-specific and correctly NOT propagated from the shared TRAPP bucket.
- **Evidence alignment:** Overlap on TRAPP: PN cites PMID:27066478 + Frontiers review = review core. Review enriches with PMID:21525244 (TRAPP identification), 19942856 (Golgi-exit screen), 27862579 (CDG), and 31575891 (autophagy, PN does not list).
- **Verdict:** Consistent; one substantive curation question. **Recommended edits:** in TRAPPC11-ai-review.yaml, reconsider the `NEW` GO:0097352 autophagosome maturation against GO:0000045 autophagosome assembly, since PMID:31575891 evidence concerns isolation-membrane sealing/closure, not the post-closure PI3P/LC3-removal step GO:0097352 defines.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/TRAPPC11/TRAPPC11-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Autophagy component recruitment to autophagophore | TRAPP complex component
- UniProt: Q7Z392
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
