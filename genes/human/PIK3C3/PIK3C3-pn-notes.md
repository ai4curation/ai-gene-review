# PIK3C3 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q8NEB9
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: modified

## Source Files Checked

- AIGR review YAML: present - [genes/human/PIK3C3/PIK3C3-ai-review.yaml](PIK3C3-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PIK3C3/PIK3C3-ai-review.html](PIK3C3-ai-review.html)
- Gene notes: present - [genes/human/PIK3C3/PIK3C3-notes.md](PIK3C3-notes.md)
- GOA TSV: present - [genes/human/PIK3C3/PIK3C3-goa.tsv](PIK3C3-goa.tsv)
- UniProt record: present - [genes/human/PIK3C3/PIK3C3-uniprot.txt](PIK3C3-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PIK3C3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PIK3C3.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIK3C3.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIK3C3.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- [genes/human/PIK3C3/PIK3C3-deep-research-falcon.md](PIK3C3-deep-research-falcon.md)

## AIGR Review Snapshot

- Description: PIK3C3 encodes VPS34, the catalytic lipid kinase of class III phosphatidylinositol 3-kinase complexes. VPS34 generates phosphatidylinositol 3-phosphate (PI3P) on endomembranes and operates in two main Beclin 1-containing assemblies: PI3KC3-C1 with ATG14 for autophagosome initiation and PI3KC3-C2 with UVRAG for endosomal sorting and later autophagy-associated trafficking. Autophagy initiation and macroautophagy are major VPS34 roles, whereas endosomal trafficking and cytokinesis are contextual extensions of the same PI3P-generating biology.
- Existing/core annotation action counts: ACCEPT: 21; KEEP_AS_NON_CORE: 33; MARK_AS_OVER_ANNOTATED: 46; MODIFY: 14; REMOVE: 5

## PN Consistency Summary

- **Consistency:** Fully consistent. PN notes (VPS34 in PI3KC3-C1 making PI3P at nucleation; PI3KC3-C2 in endosome/autophagosome maturation + HOPS recruitment) match the review and deep research (falcon). Both projected complex terms are present: GO:0034271 ACCEPT (core, PI3KC3-C1) and GO:0034272 KEEP_AS_NON_CORE (PI3KC3-C2). The PN type-I = core / type-II = trafficking split mirrors the review's core-vs-non-core split exactly.
- **PN story / NEW pressure:** No new pressure — PN's complex memberships are already in GOA and the review. Both type-specific complex terms (GO:0034271/GO:0034272) verified real via the review's annotations; GO:0097352 autophagosome maturation (used in core_functions) verified real via OLS. The review additionally REMOVEs miscalls (GO:0004672 protein kinase, GO:0043491 PI3K/AKT) consistent with VPS34 being a class III lipid kinase. Conclusion: already captured; PN adds no over-reach.
- **Evidence alignment:** PN cites PI3KC3-C1/C2 reviews + Matsunaga (ATG14L/Rubicon) Nat Cell Biol; review anchors the same complex biology to PMID:40442316 (PI3KC3-C1 structure), PMID:33637724, PMID:7628435 (substrate specificity). Substantive overlap on complex composition and PI3P output.
- **Verdict:** Fully consistent and well-scoped; PN complex projections already captured, type-I/type-II split correctly preserved. No edits required.

## Full Consistency Review

- **UniProt:** Q8NEB9 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component` and `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` ; **PN-node mapping:** type leaves `mapped / ok_for_propagation` to GO:0034271 (C-III type I) and GO:0034272 (C-III type II); group nodes `context_only / GO:0035032`; class `context_only / GO:0016236`. Both projected terms `already_in_goa_exact`.
- **Consistency:** Fully consistent. PN notes (VPS34 in PI3KC3-C1 making PI3P at nucleation; PI3KC3-C2 in endosome/autophagosome maturation + HOPS recruitment) match the review and deep research (falcon). Both projected complex terms are present: GO:0034271 ACCEPT (core, PI3KC3-C1) and GO:0034272 KEEP_AS_NON_CORE (PI3KC3-C2). The PN type-I = core / type-II = trafficking split mirrors the review's core-vs-non-core split exactly.
- **PN story / NEW pressure:** No new pressure — PN's complex memberships are already in GOA and the review. Both type-specific complex terms (GO:0034271/GO:0034272) verified real via the review's annotations; GO:0097352 autophagosome maturation (used in core_functions) verified real via OLS. The review additionally REMOVEs miscalls (GO:0004672 protein kinase, GO:0043491 PI3K/AKT) consistent with VPS34 being a class III lipid kinase. Conclusion: already captured; PN adds no over-reach.
- **Mapping strategy:** No change. The two `mapped` component leaves are correctly the only propagating nodes; the group/class nodes are correctly `context_only` (generic GO:0035032 / GO:0016236 not propagated). This is the model case for "only explicit complex-component leaves propagate to GO complex terms."
- **Evidence alignment:** PN cites PI3KC3-C1/C2 reviews + Matsunaga (ATG14L/Rubicon) Nat Cell Biol; review anchors the same complex biology to PMID:40442316 (PI3KC3-C1 structure), PMID:33637724, PMID:7628435 (substrate specificity). Substantive overlap on complex composition and PI3P output.
- **Verdict:** Fully consistent and well-scoped; PN complex projections already captured, type-I/type-II split correctly preserved. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/PIK3C3/PIK3C3-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: Q8NEB9
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Member of class III PI3K complex 2 that is involved in endosome and autophagosome maturation and recruits the HOPS complex for lysosome fusion
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - Two Beclin 1-binding proteins, Atg14L and Rubicon, reciprocally regulate autophagy at different stages | Nature Cell Biology
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

## PN row 2: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Class 3 PI3K complex 2, direct | Class 3 PI3K complex 2 component
- UniProt: Q8NEB9
- In branches: ALP
- Notes: Member of class III PI3K complex 1 that produces PI(3)P at the site of phagophore nucleation. Member of class III PI3K complex 2 that is involved in endosome and autophagosome maturation and recruits the HOPS complex for lysosome fusion
- PN references (titles):
    - Mammalian Autophagy: How Does It Work? | Annual Review of Biochemistry (annualreviews.org)
    - Full article: Autophagy pathway: Cellular and molecular mechanisms (tandfonline.com)
    - Two Beclin 1-binding proteins, Atg14L and Rubicon, reciprocally regulate autophagy at different stages | Nature Cell Biology
- PN-node mapping records (path + ancestors):
    - [type] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component
        status=mapped scope=ok_for_propagation_to_go GO=[GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II]
        rationale: This PN type denotes component membership in the direct class III PI3K complex 2 module used during autophagosome maturation and lysosome fusion. The corresponding GO complex term is the right propagation target.
    - [group] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct
        status=context_only scope=too_broad_to_propagate GO=[GO:0035032 phosphatidylinositol 3-kinase complex, class III]
        rationale: Reviewed as a class-III PI3K complex context or regulator bucket. This node is useful for curator interpretation, but it should not project cellular-component membership; only explicit complex-component leaves propagate to GO complex terms.
    - [class] Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion
        status=context_only scope=too_broad_to_propagate GO=[GO:0016236 macroautophagy]
        rationale: This class is a late macroautophagy context, but the subtree mixes docking, fusion, localization, membrane-composition, and unknown late-stage roles. The class-level relation is useful for display while propagation is restricted to narrower mechanism nodes.
    - [branch] Autophagy-Lysosome Pathway
        status=no_mapping scope= GO=[]
        rationale: Reviewed as the top-level PN branch. It is a project taxonomy umbrella rather than a direct GO assertion; all propagation must come from manually curated child nodes.

## Projected GO annotations (2)
- GO:0034271 phosphatidylinositol 3-kinase complex, class III, type I | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component
- GO:0034272 phosphatidylinositol 3-kinase complex, class III, type II | scope=ok_for_propagation_to_go | goa_status=already_in_goa_exact | from=Autophagy-Lysosome Pathway|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component

## Note

This file is generated from the current PROTEOSTASIS phase-1 dossier and local gene-review artifacts. Edit the source review, PN mapping, or dossier rather than this generated note when correcting the underlying curation.
