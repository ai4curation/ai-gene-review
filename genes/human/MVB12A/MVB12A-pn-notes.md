# MVB12A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96EY5
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/MVB12A/MVB12A-ai-review.yaml](MVB12A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/MVB12A/MVB12A-ai-review.html](MVB12A-ai-review.html)
- Gene notes: present - [genes/human/MVB12A/MVB12A-notes.md](MVB12A-notes.md)
- GOA TSV: present - [genes/human/MVB12A/MVB12A-goa.tsv](MVB12A-goa.tsv)
- UniProt record: present - [genes/human/MVB12A/MVB12A-uniprot.txt](MVB12A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/MVB12A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/MVB12A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MVB12A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/MVB12A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: MVB12A is a metazoan ESCRT-I fourth subunit that complexes with TSG101, VPS28, and VPS37-family subunits. Its best-supported core cellular role is ESCRT-I-dependent sorting of ubiquitinated endosomal cargo into multivesicular bodies, supported by acidic phospholipid/ubiquitin binding, EGFR down-regulation context, and MVB12A-containing ESCRT-I structural evidence. Viral budding and virus maturation reflect pathogen exploitation of ESCRT machinery rather than the main endogenous MVB12A function.
- Existing/core annotation action counts: ACCEPT: 23; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 4; MODIFY: 3; UNDECIDED: 1

## PN Consistency Summary

- **Consistency:** Partial tension. GO:0000813 ESCRT I complex is fully consistent (multiply ACCEPTed). But the review MARK_AS_OVER_ANNOTATED for GO:0016236 macroautophagy, stating the ESCRT/autophagy review (PMID:20588296) and the VPS28-interface structural assay (PMID:32424346) do NOT establish MVB12A as a core phagophore-closure factor. PN's `mapped/ok_for_propagation` projection of GO:0000045 autophagosome assembly from the "Sealing" group therefore conflicts with the review's stance.
- **PN story / NEW pressure:** PN asserts MVB12A is involved in autophagophore sealing/autophagosome assembly — a role NOT in MVB12A's GOA and NOT added by the review. The review treats this as over-annotation pending MVB12A-specific phagophore-closure perturbation (the VPS37A evidence in PMID:31519728 is about a different ESCRT-I subunit). Conclusion: PN over-reaches at the gene level for GO:0000045; better left as a curator question, not a propagated annotation.
- **Evidence alignment:** Shared paper: PMID:32424346 (ESCRT-I helical assembly) is both the PN reference and the review's source for ESCRT-I/membrane-fission. PN's autophagy framing leans on PMID:20588296; review cites the same but downgrades it. Strong overlap on the structural evidence, divergence on the autophagy inference.
- **Verdict:** ESCRT-I membership consistent; PN's GO:0000045 autophagosome-assembly projection over-reaches per the review's own MARK_AS_OVER_ANNOTATED. **Recommended edits:** none to the gene YAML; flag the "Sealing" node so GO:0000045 is not auto-propagated to MVB12A without subunit-specific closure evidence.

## Full Consistency Review

- **UniProt:** Q96EY5 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|...|Sealing of autophagophore membrane|ESCRT-I complex component` and `UPS|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|idiosyncratic Ub binding` ; **PN-node mapping:** ALP leaf `mapped / GO:0000813 ESCRT I complex`; ALP "Sealing" group `mapped / ok_for_propagation / GO:0000045 autophagosome assembly`; UPS nodes all `no_mapping` (class `context_only` GO:0140036). Projected: GO:0000813 (`already_in_goa_exact`), GO:0000045 (`more_specific_than_existing_goa`).
- **Consistency:** Partial tension. GO:0000813 ESCRT I complex is fully consistent (multiply ACCEPTed). But the review MARK_AS_OVER_ANNOTATED for GO:0016236 macroautophagy, stating the ESCRT/autophagy review (PMID:20588296) and the VPS28-interface structural assay (PMID:32424346) do NOT establish MVB12A as a core phagophore-closure factor. PN's `mapped/ok_for_propagation` projection of GO:0000045 autophagosome assembly from the "Sealing" group therefore conflicts with the review's stance.
- **PN story / NEW pressure:** PN asserts MVB12A is involved in autophagophore sealing/autophagosome assembly — a role NOT in MVB12A's GOA and NOT added by the review. The review treats this as over-annotation pending MVB12A-specific phagophore-closure perturbation (the VPS37A evidence in PMID:31519728 is about a different ESCRT-I subunit). Conclusion: PN over-reaches at the gene level for GO:0000045; better left as a curator question, not a propagated annotation.
- **Mapping strategy:** This gene argues the "Sealing of autophagophore membrane" group's `ok_for_propagation` (GO:0000045) is too aggressive for MVB12A specifically — the subunit rides in via complex membership, not demonstrated phagophore-closure function (cf. broader-term rejections). Recommend the node treat per-subunit projection of GO:0000045 as candidate, not automatic.
- **Evidence alignment:** Shared paper: PMID:32424346 (ESCRT-I helical assembly) is both the PN reference and the review's source for ESCRT-I/membrane-fission. PN's autophagy framing leans on PMID:20588296; review cites the same but downgrades it. Strong overlap on the structural evidence, divergence on the autophagy inference.
- **Verdict:** ESCRT-I membership consistent; PN's GO:0000045 autophagosome-assembly projection over-reaches per the review's own MARK_AS_OVER_ANNOTATED. **Recommended edits:** none to the gene YAML; flag the "Sealing" node so GO:0000045 is not auto-propagated to MVB12A without subunit-specific closure evidence.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/MVB12A/MVB12A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-I complex component
- UniProt: Q96EY5
- In branches: ALP, UPS
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

## PN row 2: Ubiquitin Proteasome System | Ubiquitin and UBL binding | trafficking | ESCRT-I complex | idiosyncratic Ub binding / other
- UniProt: Q96EY5
- In branches: ALP, UPS
- Signature domains: PMID: 20654576
- Auxiliary domains: (none)
- PN references (titles):
    - 20654576
- PN-node mapping records (path + ancestors):
    - [subtype] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex|idiosyncratic Ub binding / other
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a family, domain, architecture, or residual subdivision. The label is useful for PN taxonomy navigation but is not itself a GO annotation target; any functional assertion should come from a curated parent role or gene-level evidence.
    - [type] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking|ESCRT-I complex
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [group] Ubiquitin Proteasome System|Ubiquitin and UBL binding|trafficking
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a UPS taxonomy container. Its descendants mix catalytic roles, complex membership, binding domains, regulators, adaptors, and substrate-context labels, so a single propagating GO assertion would overstate the shared biology.
    - [class] Ubiquitin Proteasome System|Ubiquitin and UBL binding
        status=context_only scope=too_broad_to_propagate GO=[GO:0140036 ubiquitin-modified protein reader activity]
        rationale: This class records ubiquitin/UBL-reader context, but the subtree mixes ubiquitin, SUMO, UBL-domain, domain-architecture, catalytic, signaling, trafficking, and nucleic-acid process buckets. It is useful context, not a safe direct propagation.
    - [branch] Ubiquitin Proteasome System
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level UPS branch. It is a project taxonomy umbrella rather than a direct GO assertion; UPS propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000813 ESCRT I complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-I complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
