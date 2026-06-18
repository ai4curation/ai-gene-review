# PIK3R4 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q99570
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/PIK3R4/PIK3R4-ai-review.yaml](PIK3R4-ai-review.yaml)
- AIGR review HTML: present - [genes/human/PIK3R4/PIK3R4-ai-review.html](PIK3R4-ai-review.html)
- Gene notes: present - [genes/human/PIK3R4/PIK3R4-notes.md](PIK3R4-notes.md)
- GOA TSV: present - [genes/human/PIK3R4/PIK3R4-goa.tsv](PIK3R4-goa.tsv)
- UniProt record: present - [genes/human/PIK3R4/PIK3R4-uniprot.txt](PIK3R4-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/PIK3R4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/PIK3R4.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIK3R4.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/PIK3R4.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: PIK3R4/VPS15/p150 is the regulatory/scaffolding subunit of human class III PI3K complexes. In PI3KC3-C1 with PIK3C3/VPS34, BECN1, and ATG14, it organizes the autophagy-initiation complex and contributes to complex-level PI3P production required for autophagosome assembly and macroautophagy. In PI3KC3-C2/UVRAG-associated contexts it supports endosomal trafficking, receptor catabolism, and autophagosome maturation. Its central function is PI3KC3 complex regulation rather than independent catalytic signaling.
- Existing/core annotation action counts: ACCEPT: 33; KEEP_AS_NON_CORE: 16; MARK_AS_OVER_ANNOTATED: 9; MODIFY: 7; NEW: 1; REMOVE: 1

## PN Consistency Summary

- **Consistency:** Strong. Notes, review YAML, and PN all model PIK3R4/VPS15 as the regulatory/scaffolding subunit of class III PI3K complexes (PI3KC3-C1 and -C2), not the catalytic kinase. Review description and core_functions name both complexes explicitly. No contradictions.
- **PN story / NEW pressure:** Already captured. PN asserts membership in both class III complexes; review ACCEPTs GO:0034271 and GO:0034272 (both already IBA in GOA — PN goa_status `already_in_goa_exact`). No NEW GO term needed. Verdict: already captured.
- **Evidence alignment:** Partial overlap. PN cites review-style sources (Annual Review; Yang & Klionsky; PMID:19270696 Matsunaga Atg14L/Rubicon Nat Cell Biol). Review uses primary literature: PMID:8999962, 25490155, 40442316 (PI3KC3-C1 structure), 19270696, 20643123, 14617358. PMID:19270696 is shared. Review also flags VPS15 as a pseudokinase (PMID:40442316) and REMOVEs yeast nucleus-vacuole junction, MODIFYs pexophagy→autophagosome assembly — finer than PN.
- **Verdict:** Consistent; PN complex membership fully captured by existing GOA + review ACCEPT. No new GO pressure; mapping grain correct. No edits required.

## Full Consistency Review

- **UniProt:** Q99570 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP|Autophagophore initiation and elongation|Class 3 PI3K complex 1, direct|Class 3 PI3K complex 1 component` (row 1) and `ALP|Autophagosome closure maturation and lysosome fusion|Class 3 PI3K complex 2, direct|Class 3 PI3K complex 2 component` (row 2) ; **PN-node mapping:** both `type` leaves mapped, `ok_for_propagation_to_go` → GO:0034271 (C1/type I) and GO:0034272 (C2/type II); `group`/`class`/`branch` ancestors all context_only/no_mapping.
- **Consistency:** Strong. Notes, review YAML, and PN all model PIK3R4/VPS15 as the regulatory/scaffolding subunit of class III PI3K complexes (PI3KC3-C1 and -C2), not the catalytic kinase. Review description and core_functions name both complexes explicitly. No contradictions.
- **PN story / NEW pressure:** Already captured. PN asserts membership in both class III complexes; review ACCEPTs GO:0034271 and GO:0034272 (both already IBA in GOA — PN goa_status `already_in_goa_exact`). No NEW GO term needed. Verdict: already captured.
- **Mapping strategy:** Correct and unchanged by this gene. The two `type`-leaf mappings to GO:0034271/GO:0034272 are the right grain; ancestors (GO:0035032 class III PI3K complex; GO:0016236 macroautophagy) are correctly held as too_broad_to_propagate, consistent with the TRAPP-overpropagation precedent. PN-projected terms are neither broader nor narrower than the review — they coincide.
- **Evidence alignment:** Partial overlap. PN cites review-style sources (Annual Review; Yang & Klionsky; PMID:19270696 Matsunaga Atg14L/Rubicon Nat Cell Biol). Review uses primary literature: PMID:8999962, 25490155, 40442316 (PI3KC3-C1 structure), 19270696, 20643123, 14617358. PMID:19270696 is shared. Review also flags VPS15 as a pseudokinase (PMID:40442316) and REMOVEs yeast nucleus-vacuole junction, MODIFYs pexophagy→autophagosome assembly — finer than PN.
- **Verdict:** Consistent; PN complex membership fully captured by existing GOA + review ACCEPT. No new GO pressure; mapping grain correct. No edits required.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/PIK3R4/PIK3R4-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagophore initiation and elongation | Class 3 PI3K complex 1, direct | Class 3 PI3K complex 1 component
- UniProt: Q99570
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
- UniProt: Q99570
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
