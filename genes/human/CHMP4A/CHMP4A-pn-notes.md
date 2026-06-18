# CHMP4A PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q9BY43
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP4A/CHMP4A-ai-review.yaml](CHMP4A-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP4A/CHMP4A-ai-review.html](CHMP4A-ai-review.html)
- Gene notes: present - [genes/human/CHMP4A/CHMP4A-notes.md](CHMP4A-notes.md)
- GOA TSV: present - [genes/human/CHMP4A/CHMP4A-goa.tsv](CHMP4A-goa.tsv)
- UniProt record: present - [genes/human/CHMP4A/CHMP4A-uniprot.txt](CHMP4A-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4A.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4A.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4A.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHMP4A encodes a Snf7-family core subunit of ESCRT-III. Its best-supported function is non-enzymatic ESCRT-III polymerization on endosomal/MVB and related membranes, where CHMP4A-containing filaments bend membranes and support reverse-topology budding/fission for intraluminal vesicle formation, MVB cargo sorting, and downstream endolysosomal degradation. CHMP4A also participates in autophagy/autophagosome contexts, plasma membrane repair, cytokinetic abscission, nuclear envelope repair, and viral budding as topologically related ESCRT output contexts, but those should not obscure the core ESCRT-III membrane-remodeling role.
- Existing/core annotation action counts: ACCEPT: 38; KEEP_AS_NON_CORE: 48; MARK_AS_OVER_ANNOTATED: 10; MODIFY: 6; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Consistent. The review ACCEPTs GO:0000815 ESCRT III complex (IBA + NAS) and the autophagy/endolysosomal context cluster (GO:0006914, GO:0097352 autophagosome maturation, GO:0000421 autophagosome membrane, GO:1902774, GO:1904930 amphisome). The review's own caveat — CHMP4A "was [not] directly assayed as the phagophore-sealing effector" (Snf7-1 knockdown causes autophagosome accumulation, PMID:21975012/17984323) — matches PN routing "sealing" to the safe parent GO:0000045 rather than a sealing-specific term. No contradiction.
- **PN story / NEW pressure:** Already captured. Verified via OLS that **no GO term for "autophagosome closure / phagophore sealing" exists** (GO:0061908 phagophore is a CC only; GO:0000045 is the narrowest process). PN's "sealing" projection therefore correctly degrades to GO:0000045 — but the review does **not** list GO:0000045 for CHMP4A, instead carrying GO:0097352 autophagosome maturation (a sibling) + GO:0006914. Both are defensible; GO:0000045 would be the assembly-side framing of the same sealing biology.
- **Evidence alignment:** Minimal overlap. PN cites one MDPI review "Key Regulators of Autophagosome Closure"; the review uses none of PN's citations, relying on primary ESCRT-III structural/functional literature (PMID:18209100, 19234443, 17984323, 21975012). Convergent on the ESCRT-III-in-autophagosome-closure concept via independent sources.
- **Verdict:** Consistent; PN projections (GO:0000815, GO:0000045) are both ≤ existing or more-specific. Optional edit: reconcile GO:0000045 vs the review's GO:0097352 for the sealing step.

## Full Consistency Review

- **UniProt:** Q9BY43 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** 2 rows, ALP — (1) `Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component`; (2) `Microautophagy → General microautophagy machinery → ESCRT-III complex component`. **PN-node mapping:** ESCRT-III leaves=mapped→GO:0000815 (already_in_goa_exact); sealing group=mapped→GO:0000045 autophagosome assembly (more_specific_than_existing_goa); ancestors context_only (GO:0016236, GO:0016237). **Projected:** GO:0000815 (x2), GO:0000045.
- **Consistency:** Consistent. The review ACCEPTs GO:0000815 ESCRT III complex (IBA + NAS) and the autophagy/endolysosomal context cluster (GO:0006914, GO:0097352 autophagosome maturation, GO:0000421 autophagosome membrane, GO:1902774, GO:1904930 amphisome). The review's own caveat — CHMP4A "was [not] directly assayed as the phagophore-sealing effector" (Snf7-1 knockdown causes autophagosome accumulation, PMID:21975012/17984323) — matches PN routing "sealing" to the safe parent GO:0000045 rather than a sealing-specific term. No contradiction.
- **PN story / NEW pressure:** Already captured. Verified via OLS that **no GO term for "autophagosome closure / phagophore sealing" exists** (GO:0061908 phagophore is a CC only; GO:0000045 is the narrowest process). PN's "sealing" projection therefore correctly degrades to GO:0000045 — but the review does **not** list GO:0000045 for CHMP4A, instead carrying GO:0097352 autophagosome maturation (a sibling) + GO:0006914. Both are defensible; GO:0000045 would be the assembly-side framing of the same sealing biology.
  - **Recommended edits:** consider adding `GO:0000045 autophagosome assembly` (action: NEW or note in suggested_questions) to align with the PN "Sealing of autophagophore membrane → autophagosome assembly" projection, OR explicitly note GO:0097352 already covers the closure/maturation step. Low priority — the maturation term already captures the biology; flag for curator.
- **Mapping strategy:** No change needed. GO:0000815 is already_in_goa_exact (safe). GO:0000045 is more_specific_than_existing_goa (good direction, not over-reach). CHMP4A is a clean ESCRT-III member for both the autophagosome-closure and microautophagy leaves; the node mappings are appropriate.
- **Evidence alignment:** Minimal overlap. PN cites one MDPI review "Key Regulators of Autophagosome Closure"; the review uses none of PN's citations, relying on primary ESCRT-III structural/functional literature (PMID:18209100, 19234443, 17984323, 21975012). Convergent on the ESCRT-III-in-autophagosome-closure concept via independent sources.
- **Verdict:** Consistent; PN projections (GO:0000815, GO:0000045) are both ≤ existing or more-specific. Optional edit: reconcile GO:0000045 vs the review's GO:0097352 for the sealing step.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP4A/CHMP4A-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q9BY43
- In branches: ALP
- Notes: Component of the ESCRT-III complex, involved in autophagosome closure
- PN references (titles):
    - Cells | Free Full-Text | Key Regulators of Autophagosome Closure (mdpi.com)
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
- UniProt: Q9BY43
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
