# VPS37D PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q86XT2
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/VPS37D/VPS37D-ai-review.yaml](VPS37D-ai-review.yaml)
- AIGR review HTML: present - [genes/human/VPS37D/VPS37D-ai-review.html](VPS37D-ai-review.html)
- Gene notes: present - [genes/human/VPS37D/VPS37D-notes.md](VPS37D-notes.md)
- GOA TSV: present - [genes/human/VPS37D/VPS37D-goa.tsv](VPS37D-goa.tsv)
- UniProt record: present - [genes/human/VPS37D/VPS37D-uniprot.txt](VPS37D-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/VPS37D.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37D.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/VPS37D.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: VPS37D is a VPS37-family ESCRT-I subunit in TSG101-VPS28-VPS37-MVB12/UBAP-family complexes. The best-supported cellular function is ESCRT-I-dependent endosomal sorting of ubiquitinated cargo into multivesicular bodies, with late-endosome/endosome-membrane localization. Current local evidence does not support transferring VPS37A-specific phagophore-closure or VPS37B/VPS28 structural membrane-fission assays to VPS37D as core annotations.
- Existing/core annotation action counts: ACCEPT: 18; KEEP_AS_NON_CORE: 3; MARK_AS_OVER_ANNOTATED: 3; MODIFY: 2

## PN Consistency Summary

- **Consistency:** PARTIAL CONTRADICTION (same axis as VPS37B/C), with the weakest gene-specific evidence of the family. ESCRT-I membership consistent: review ACCEPTs GO:0000813, but notes VPS37D family assignment is largely by sequence similarity (PMID:15218037 studied VPS37B; only UniProt/ComplexPortal + PMID:18005716/22405001 support membership). Autophagy diverges: review MARK_AS_OVER_ANNOTATED GO:0016236 and GO:0090148 (membrane fission), declining GO:0000045. PN still projects GO:0000045 to VPS37D.
- **PN story / NEW pressure:** Over-reaches for autophagy. PN's group GO:0000045 asserts an autophagosome-assembly role with no VPS37D-specific support at all (no phagophore-closure, membrane-scission, or even direct MVB assay for this paralog). ESCRT-I already captured; review even cautions against overstating VPS37D experimental testing. No NEW term beyond GO:0000813.
- **Evidence alignment:** Partial. PN cites only PMID:32424346 (VPS37B headpiece), which the review explicitly says should not transfer membrane-fission/autophagy to VPS37D. Review adds PMID:22405001 (UBAP1 coassembly) not in PN.
- **Verdict:** Consistent on ESCRT-I; GO:0000045 projection over-reaches most strongly here. **Recommended edits:** none to YAML (review correctly omits GO:0000045); flag PN sealing-group→GO:0000045 as non-propagating to VPS37D.

## Full Consistency Review

- **UniProt:** Q86XT2 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 1 row, ALP — `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-I complex component`. **PN-node mapping:** leaf=mapped→GO:0000813; sealing group=mapped→GO:0000045; class=context_only (GO:0016236). **Projected:** GO:0000045 (more_specific_than_existing_goa), GO:0000813 (already_in_goa_exact).
- **Consistency:** PARTIAL CONTRADICTION (same axis as VPS37B/C), with the weakest gene-specific evidence of the family. ESCRT-I membership consistent: review ACCEPTs GO:0000813, but notes VPS37D family assignment is largely by sequence similarity (PMID:15218037 studied VPS37B; only UniProt/ComplexPortal + PMID:18005716/22405001 support membership). Autophagy diverges: review MARK_AS_OVER_ANNOTATED GO:0016236 and GO:0090148 (membrane fission), declining GO:0000045. PN still projects GO:0000045 to VPS37D.
- **PN story / NEW pressure:** Over-reaches for autophagy. PN's group GO:0000045 asserts an autophagosome-assembly role with no VPS37D-specific support at all (no phagophore-closure, membrane-scission, or even direct MVB assay for this paralog). ESCRT-I already captured; review even cautions against overstating VPS37D experimental testing. No NEW term beyond GO:0000813.
- **Mapping strategy:** Flag (strongest case in family). Leaf→GO:0000813 acceptable (in GOA, defensible by homology). Group→GO:0000045 clearly over-reaches — VPS37D is the least-characterized paralog; this is exactly the shared-node over-propagation the TOMM20/HSPA8/RAB7A precedent rejects. GO:0000045 must not propagate to VPS37D.
- **Evidence alignment:** Partial. PN cites only PMID:32424346 (VPS37B headpiece), which the review explicitly says should not transfer membrane-fission/autophagy to VPS37D. Review adds PMID:22405001 (UBAP1 coassembly) not in PN.
- **Verdict:** Consistent on ESCRT-I; GO:0000045 projection over-reaches most strongly here. **Recommended edits:** none to YAML (review correctly omits GO:0000045); flag PN sealing-group→GO:0000045 as non-propagating to VPS37D.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/VPS37D/VPS37D-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q86XT2
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
