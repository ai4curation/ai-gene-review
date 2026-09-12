# BECN2 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: A8MW95
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/BECN2/BECN2-ai-review.yaml](BECN2-ai-review.yaml)
- AIGR review HTML: present - [genes/human/BECN2/BECN2-ai-review.html](BECN2-ai-review.html)
- Gene notes: present - [genes/human/BECN2/BECN2-notes.md](BECN2-notes.md)
- GOA TSV: present - [genes/human/BECN2/BECN2-goa.tsv](BECN2-goa.tsv)
- UniProt record: present - [genes/human/BECN2/BECN2-uniprot.txt](BECN2-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/BECN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/BECN2.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BECN2.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/BECN2.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/BECN2/BECN2-deep-research-falcon.md](BECN2-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: BECN2/Beclin 2 is a mammalian Beclin-family autophagy and endolysosomal trafficking regulator. It interacts with class III PI3K complex components including PIK3C3/VPS34 and ATG14/UVRAG-associated partners to support autophagy/autophagosome assembly, and it also mediates GASP1/GPRASP1-dependent lysosomal degradation of GPCRs. Beclin-family PI3KC3/autophagy-complex participation is a shared core role, while GPCR catabolism is a BECN2-specific functional branch.
- Existing/core annotation action counts: ACCEPT: 15; KEEP_AS_NON_CORE: 1; MARK_AS_OVER_ANNOTATED: 1; MODIFY: 3; NEW: 1

## PN Consistency Summary

- **Consistency:** Consistent. The review ACCEPTs GO:0034271 (PI3KC3-C1, IBA) and adds a NEW IMP autophagosome-assembly row, matching the PN "C1 component" placement. The review goes beyond PN in flagging the BECN2-specific, non-shared GPCR/GASP1 endolysosomal-degradation branch (GO:1990172, GO:0008333) — PN's single ALP row does not capture that, but the PN Notes explicitly mention "lysosomal degradation of GPCRs," so the two are aligned in spirit, not contradictory.
- **PN story / NEW pressure:** Already captured (and exceeded). PN asserts only C1 membership = projected GO:0034271, already_in_goa_exact and ACCEPTed. The distinctive GPCR-catabolism role (the real "new" biology) is already minted by the review as core GO:1990172. No additional GO term warranted from the PN placement; PN under-represents BECN2 rather than over-reaching.
- **Evidence alignment:** Strong overlap. PN cites the single ScienceDirect "Beclin 2 Functions in Autophagy, Degradation of GPCRs, and Metabolism" = review's central PMID:23954414. Review adds PMID:28218432, 36719945, 37409929, 34152938, 32865519 (none in PN). Convergent on the founding paper; review is far richer.
- **Verdict:** Fully consistent; PN captures the shared C1 role, review additionally captures the BECN2-specific GPCR branch. No edits needed.

## Full Consistency Review

- **UniProt:** A8MW95 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 1 row, ALP — `Autophagophore initiation and elongation → Class 3 PI3K complex 1, direct → Class 3 PI3K complex 1 component`. **PN-node mapping:** component leaf=mapped→GO:0034271; ancestors context_only (GO:0035032, GO:0016236). **Projected:** GO:0034271 (goa_status=already_in_goa_exact).
- **Consistency:** Consistent. The review ACCEPTs GO:0034271 (PI3KC3-C1, IBA) and adds a NEW IMP autophagosome-assembly row, matching the PN "C1 component" placement. The review goes beyond PN in flagging the BECN2-specific, non-shared GPCR/GASP1 endolysosomal-degradation branch (GO:1990172, GO:0008333) — PN's single ALP row does not capture that, but the PN Notes explicitly mention "lysosomal degradation of GPCRs," so the two are aligned in spirit, not contradictory.
- **PN story / NEW pressure:** Already captured (and exceeded). PN asserts only C1 membership = projected GO:0034271, already_in_goa_exact and ACCEPTed. The distinctive GPCR-catabolism role (the real "new" biology) is already minted by the review as core GO:1990172. No additional GO term warranted from the PN placement; PN under-represents BECN2 rather than over-reaching.
- **Mapping strategy:** No change. GO:0034271 propagation is safe (already in GOA exact, supported by PMID:28218432 BECN2-ATG14 coiled-coil). Inclusion of BECN2 does not destabilize the node. The review's open question (curate C1/C2 membership as direct vs Beclin-family inference) is a curator nuance, not a mapping-strategy problem.
- **Evidence alignment:** Strong overlap. PN cites the single ScienceDirect "Beclin 2 Functions in Autophagy, Degradation of GPCRs, and Metabolism" = review's central PMID:23954414. Review adds PMID:28218432, 36719945, 37409929, 34152938, 32865519 (none in PN). Convergent on the founding paper; review is far richer.
- **Verdict:** Fully consistent; PN captures the shared C1 role, review additionally captures the BECN2-specific GPCR branch. No edits needed.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/BECN2/BECN2-ai-review.yaml
- PN workbook rows: 1

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: A8MW95
- In branches: ALP
- Notes: Paralog of BECN1 that can also be part of the class III PI3K complex 1. Also required for lysosomal degradation of GPCRs.
- PN references (titles):
    - Beclin 2 Functions in Autophagy, Degradation of G Protein-Coupled Receptors, and Metabolism - ScienceDirect
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I]
        rationale: This PN type is a curated component class for the direct autophagy- promoting class III PI3K complex 1. Propagation to the matching GO cellular-component term is appropriate, although the source is a component-role category rather than the complex term itself.
    - [group] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagophore initiation and elongation
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a real macroautophagy context, but its descendants include core factors, component buckets, upstream modulators, localization roles, and residual categories. Projecting generic macroautophagy from this ancestor creates TRAPP-like overpropagation, so candidate GO annotations must come from narrower curated nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (1)
- GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
