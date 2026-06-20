# VPS37C PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: A5D8V6
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS37C/VPS37C-ai-review.yaml](VPS37C-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS37C/VPS37C-ai-review.html](VPS37C-ai-review.html)
- Gene notes: present - [genes/human/VPS37C/VPS37C-notes.md](VPS37C-notes.md)
- GOA TSV: present - [genes/human/VPS37C/VPS37C-goa.tsv](VPS37C-goa.tsv)
- UniProt record: present - [genes/human/VPS37C/VPS37C-uniprot.txt](VPS37C-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37C.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37C.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS37C is a VPS37-family ESCRT-I subunit that complexes with TSG101, VPS28, and MVB12/UBAP-family partners. The best-supported cellular function is ESCRT-I-dependent endosomal sorting of ubiquitinated cargo into multivesicular bodies, with late-endosome/endosome-membrane localization and a secondary viral budding context. Current local evidence does not support transferring the VPS37A-specific phagophore-closure role to VPS37C as a core annotation.
- Existing/core annotation action counts: ACCEPT: 19; KEEP_AS_NON_CORE: 7; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 2

## PN Consistency Summary

- **Consistency:** PARTIAL CONTRADICTION (same axis as VPS37B). ESCRT-I membership fully consistent: review ACCEPTs GO:0000813, with gene-specific support (ternary complex with TSG101/VPS28, PMID:15509564) and MVB sorting. Autophagy diverges: review MARK_AS_OVER_ANNOTATED both GO:0016236 macroautophagy rows and even MARK_AS_OVER_ANNOTATED a GO:0090148 membrane-fission row (noting the structural paper tested a VPS37B headpiece, not VPS37C), declining GO:0000045. PN still projects GO:0000045 to VPS37C.
- **PN story / NEW pressure:** Over-reaches for autophagy. PN's group GO:0000045 asserts autophagosome assembly the review finds unsupported for VPS37C (phagophore closure is VPS37A-specific; PMID:21757351 explicitly notes UBAP1 ESCRT-I "contains VPS37A but not VPS37C"). ESCRT-I already captured. No NEW term beyond GO:0000813.
- **Evidence alignment:** Partial. PN cites only PMID:32424346, which the review uses for general ESCRT-I mechanism but explicitly flags as not VPS37C-specific (VPS37B headpiece). Review adds VPS37C-specific PMID:15509564 and ALG-2 context PMID:23924735, absent from PN. PN omits the UBAP1 caveat (PMID:21757351) the review relies on.
- **Verdict:** Consistent on ESCRT-I; GO:0000045 projection over-reaches. **Recommended edits:** none to YAML (review correctly omits GO:0000045); flag PN sealing-group→GO:0000045 as non-propagating to VPS37C.

## Full Consistency Review

- **UniProt:** A5D8V6 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 1 row, ALP — `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-I complex component`. **PN-node mapping:** leaf=mapped→GO:0000813; sealing group=mapped→GO:0000045; class=context_only (GO:0016236). **Projected:** GO:0000045 (more_specific_than_existing_goa), GO:0000813 (already_in_goa_exact).
- **Consistency:** PARTIAL CONTRADICTION (same axis as VPS37B). ESCRT-I membership fully consistent: review ACCEPTs GO:0000813, with gene-specific support (ternary complex with TSG101/VPS28, PMID:15509564) and MVB sorting. Autophagy diverges: review MARK_AS_OVER_ANNOTATED both GO:0016236 macroautophagy rows and even MARK_AS_OVER_ANNOTATED a GO:0090148 membrane-fission row (noting the structural paper tested a VPS37B headpiece, not VPS37C), declining GO:0000045. PN still projects GO:0000045 to VPS37C.
- **PN story / NEW pressure:** Over-reaches for autophagy. PN's group GO:0000045 asserts autophagosome assembly the review finds unsupported for VPS37C (phagophore closure is VPS37A-specific; PMID:21757351 explicitly notes UBAP1 ESCRT-I "contains VPS37A but not VPS37C"). ESCRT-I already captured. No NEW term beyond GO:0000813.
- **Mapping strategy:** Flag. Leaf→GO:0000813 correct (already in GOA). Group→GO:0000045 over-reaches for VPS37C — same shared-node over-reach pattern as TOMM20/HSPA8/RAB7A; GO:0000045 should not propagate to VPS37C without gene-specific evidence.
- **Evidence alignment:** Partial. PN cites only PMID:32424346, which the review uses for general ESCRT-I mechanism but explicitly flags as not VPS37C-specific (VPS37B headpiece). Review adds VPS37C-specific PMID:15509564 and ALG-2 context PMID:23924735, absent from PN. PN omits the UBAP1 caveat (PMID:21757351) the review relies on.
- **Verdict:** Consistent on ESCRT-I; GO:0000045 projection over-reaches. **Recommended edits:** none to YAML (review correctly omits GO:0000045); flag PN sealing-group→GO:0000045 as non-propagating to VPS37C.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS37C/VPS37C-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: A5D8V6
- In branches: ALP
- Notes: Component of the ESCRT-I complex, involved in autophagosome closure
- PN references (titles):
    - A helical assembly of human ESCRT-I scaffolds reverse-topology membrane scission | Nature Structural & Molecular Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000813 ESCRT I complex]
        rationale: This leaf is restricted to ESCRT-I components used in autophagophore sealing. The shared GO assertion is ESCRT I complex membership.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
