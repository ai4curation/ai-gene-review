# CHMP4B PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9H444
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP4B/CHMP4B-ai-review.yaml](CHMP4B-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP4B/CHMP4B-ai-review.html](CHMP4B-ai-review.html)
- Gene notes: present - [genes/human/CHMP4B/CHMP4B-notes.md](CHMP4B-notes.md)
- GOA TSV: present - [genes/human/CHMP4B/CHMP4B-goa.tsv](CHMP4B-goa.tsv)
- UniProt record: present - [genes/human/CHMP4B/CHMP4B-uniprot.txt](CHMP4B-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4B.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4B.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4B.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/CHMP4B/CHMP4B-deep-research-falcon.md](CHMP4B-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: CHMP4B encodes hSnf7-2, a Snf7-family core subunit of ESCRT-III. Its best-supported function is non-enzymatic ESCRT-III polymerization on endosomal/MVB and related membranes, where CHMP4B-containing filaments bend membranes and support reverse-topology budding/fission for intraluminal vesicle formation, MVB cargo sorting, and endolysosomal degradation. CHMP4B is also an important paralog for human neuronal cargo turnover/autophagosome accumulation, cytokinetic abscission, viral budding, nuclear envelope sealing, plasma membrane repair, and lens transparency, but these contexts should be interpreted through the core ESCRT-III membrane-remodeling mechanism.
- Existing/core annotation action counts: ACCEPT: 39; KEEP_AS_NON_CORE: 57; MARK_AS_OVER_ANNOTATED: 28; MODIFY: 11; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Strong. Deep-research (falcon), review, PN, and mapping all agree CHMP4B is the dominant Snf7-family ESCRT-III core subunit with a genuine, gene-specific autophagy link: human-neuron hSnf7-2 knockdown causes autophagosome accumulation (PMID:21975012); STX13/phagophore→autophagosome maturation (PMID:24095276). No contradictions.
- **PN story / NEW pressure:** PN's "Sealing of autophagophore" projects GO:0000045 autophagosome assembly (verified real via OLS) as more specific than current GOA. The review captures the autophagy axis at a sibling altitude — GO:0097352 autophagosome maturation + GO:0016236 macroautophagy (both KEEP_AS_NON_CORE, in core_functions) — but does NOT carry GO:0000045. For CHMP4B specifically, the closure/sealing role is the best-supported of the five paralogs, so GO:0000045 is a defensible ADD as non-core. **ADD GO:0000045 autophagosome assembly (non-core).**
- **Evidence alignment:** Partial. PN cites two reviews (Cells "Key Regulators of Autophagosome Closure"; tandfonline mitophagy sealing). Review cites primary literature (PMID:18209100, 21975012, 17984323, 24095276) — same ESCRT-in-autophagy theme, different specific papers. GO:0000815 IBA original_reference is GO_REF:0000033, not the PN review.
- **Verdict:** Consistent; well-handled. **Recommended edits:** add GO:0000045 autophagosome assembly as a NEW non-core annotation (PMID:21975012, 24095276) to close the one gap vs the PN projection.

## Full Consistency Review

- **UniProt:** Q9H444 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component` AND `ALP → Microautophagy → General microautophagy machinery → ESCRT-III complex component` (2 rows)
- **PN-node mapping:** type = `mapped`/`ok_for_propagation` → GO:0000815 ESCRT III complex (already in GOA); "Sealing" group = `mapped` → GO:0000045 autophagosome assembly (`more_specific_than_existing_goa`); both classes `context_only`/`too_broad` (GO:0016236 macroautophagy, GO:0016237 microautophagy); branch `no_mapping`.
- **Consistency:** Strong. Deep-research (falcon), review, PN, and mapping all agree CHMP4B is the dominant Snf7-family ESCRT-III core subunit with a genuine, gene-specific autophagy link: human-neuron hSnf7-2 knockdown causes autophagosome accumulation (PMID:21975012); STX13/phagophore→autophagosome maturation (PMID:24095276). No contradictions.
- **PN story / NEW pressure:** PN's "Sealing of autophagophore" projects GO:0000045 autophagosome assembly (verified real via OLS) as more specific than current GOA. The review captures the autophagy axis at a sibling altitude — GO:0097352 autophagosome maturation + GO:0016236 macroautophagy (both KEEP_AS_NON_CORE, in core_functions) — but does NOT carry GO:0000045. For CHMP4B specifically, the closure/sealing role is the best-supported of the five paralogs, so GO:0000045 is a defensible ADD as non-core. **ADD GO:0000045 autophagosome assembly (non-core).**
- **Mapping strategy:** No change needed. CHMP4B membership reinforces (does not alter) the leaf→GO:0000815 / group→GO:0000045 calls; the conservative class-level `context_only` holds. PN projection is appropriately narrower than the existing macroautophagy term, unlike the rejected TOMM20/HSPA8/RAB7A broader projections.
- **Evidence alignment:** Partial. PN cites two reviews (Cells "Key Regulators of Autophagosome Closure"; tandfonline mitophagy sealing). Review cites primary literature (PMID:18209100, 21975012, 17984323, 24095276) — same ESCRT-in-autophagy theme, different specific papers. GO:0000815 IBA original_reference is GO_REF:0000033, not the PN review.
- **Verdict:** Consistent; well-handled. **Recommended edits:** add GO:0000045 autophagosome assembly as a NEW non-core annotation (PMID:21975012, 24095276) to close the one gap vs the PN projection.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP4B/CHMP4B-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q9H444
- In branches: ALP
- Notes: Component of the ESCRT-III complex, involved in autophagosome closure. Recruited to unsealed autophagosomes in macroautophagy and mitophagy.
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
    - Full article: ESCRT-mediated phagophore sealing during mitophagy (tandfonline.com)
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This PN type is a structural component class for ESCRT-III factors used in autophagophore sealing. The matching GO cellular-component term is ESCRT III complex, which is more precise than the broader late-fusion process mapping.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000045 autophagosome assembly]
        rationale: This group captures autophagophore closure/sealing, a late step in autophagosome assembly. Autophagosome assembly is the safer process target than autophagosome-lysosome fusion.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## PN row 2: Autophagy-Lysosome Pathway | Microautophagy | General microautophagy machinery | ESCRT-III complex component
- UniProt: Q9H444
- In branches: ALP
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0000815 ESCRT III complex]
        rationale: This leaf is a component bucket for ESCRT-III machinery used in microautophagy contexts. The shared GO assertion is ESCRT III complex membership.
    - [group] Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery
        status=no_mapping scope= GO=[]
        rationale: Reviewed as a broad PN taxonomy container. The descendants mix components, regulators, context labels, and mechanistic leaves, so propagation should come only from narrower curated nodes.
    - [class] Autophagy-Lysosome Pathway|Microautophagy
        status=context_only scope=too_broad_to_propagate GO=[GO:0016237 microautophagy]
        rationale: The class names a real GO process, but the subtree includes machinery components and mitochondrion-derived-vesicle contexts as well as process labels. Propagation is restricted to narrower nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (3)
- GO:0000045 autophagosome assembly | scope=ok_for_propagation_to_go | goa_status=more_specific_than_existing_goa | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Sealing of autophagophore membrane|ESCRT-III complex component
- GO:0000815 ESCRT III complex | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Microautophagy|General microautophagy machinery|ESCRT-III complex component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
