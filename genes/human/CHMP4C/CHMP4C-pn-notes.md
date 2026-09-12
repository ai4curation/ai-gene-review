# CHMP4C PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96CF2
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP4C/CHMP4C-ai-review.yaml](CHMP4C-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP4C/CHMP4C-ai-review.html](CHMP4C-ai-review.html)
- Gene notes: present - [genes/human/CHMP4C/CHMP4C-notes.md](CHMP4C-notes.md)
- GOA TSV: present - [genes/human/CHMP4C/CHMP4C-goa.tsv](CHMP4C-goa.tsv)
- UniProt record: present - [genes/human/CHMP4C/CHMP4C-uniprot.txt](CHMP4C-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP4C.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4C.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP4C.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHMP4C encodes a Snf7-family ESCRT-III paralog with a specialized role in Aurora B/NoCut abscission checkpoint control. Unlike CHMP4B, which is the main CHMP4 paralog required for MHC-I degradation, HIV release, and cytokinesis execution in key paralog-comparison assays, CHMP4C delays abscission when chromosome segregation or checkpoint signals persist. Aurora B-phosphorylated CHMP4C localizes to the midbody/Flemming body, works with Borealin/CPC and ANCHR/ZFYVE19, and retains VPS4 at the midbody ring until checkpoint signaling is terminated. Broader ESCRT/MVB/autophagy annotations are plausible family context but should not obscure this core checkpoint-regulatory function.
- Existing/core annotation action counts: ACCEPT: 16; KEEP_AS_NON_CORE: 53; MARK_AS_OVER_ANNOTATED: 16; MODIFY: 4

## PN Consistency Summary

- **Consistency:** Consistent, with a deliberate emphasis divergence the review handles well. The review's core function is the specialized Aurora-B/NoCut **abscission-checkpoint** role (midbody, Borealin/CPC, ANCHR/ZFYVE19, VPS4 retention), NOT autophagosome sealing. The PN places CHMP4C in the generic ESCRT-III sealing bucket purely by family/component membership; the review's autophagy entries (GO:0097352, GO:0016236) are explicitly KEEP_AS_NON_CORE and flagged as inherited, "cached CHMP4C-specific papers do not directly test CHMP4C as the phagophore sealing effector." No contradiction — the review is correctly more conservative than PN.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). For CHMP4C the supporting evidence is paralog/family-level only, so this would be over-reach as a gene-specific assertion. The review already captures the family context as non-core and raises a `suggested_question` asking which assays directly implicate CHMP4C vs family inclusion. **PN over-reaches for CHMP4C — do not ADD GO:0000045; already captured at non-core altitude.**
- **Evidence alignment:** Divergent. PN cites the Cells "Key Regulators of Autophagosome Closure" review only. Review cites primary checkpoint/ESCRT papers (PMID:36107470 ESCRT-III-MIT interactome [eLife, verified — not the PN review], PMID:17984323, PMID:20588296). No shared citations.
- **Verdict:** Consistent; review correctly resists the PN autophagy projection. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q96CF2 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component` AND `ALP → Microautophagy → General microautophagy machinery → ESCRT-III complex component` (2 rows; identical template to CHMP4B/5/6/7)
- **PN-node mapping:** type → GO:0000815 ESCRT III complex (`already_in_goa_exact`); "Sealing" group → GO:0000045 autophagosome assembly (`more_specific_than_existing_goa`); classes `context_only`/`too_broad` (GO:0016236, GO:0016237); branch `no_mapping`.
- **Consistency:** Consistent, with a deliberate emphasis divergence the review handles well. The review's core function is the specialized Aurora-B/NoCut **abscission-checkpoint** role (midbody, Borealin/CPC, ANCHR/ZFYVE19, VPS4 retention), NOT autophagosome sealing. The PN places CHMP4C in the generic ESCRT-III sealing bucket purely by family/component membership; the review's autophagy entries (GO:0097352, GO:0016236) are explicitly KEEP_AS_NON_CORE and flagged as inherited, "cached CHMP4C-specific papers do not directly test CHMP4C as the phagophore sealing effector." No contradiction — the review is correctly more conservative than PN.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). For CHMP4C the supporting evidence is paralog/family-level only, so this would be over-reach as a gene-specific assertion. The review already captures the family context as non-core and raises a `suggested_question` asking which assays directly implicate CHMP4C vs family inclusion. **PN over-reaches for CHMP4C — do not ADD GO:0000045; already captured at non-core altitude.**
- **Mapping strategy:** No change. CHMP4C is a weak member for the "Sealing" group projection; the conservative class-level `context_only` is right and the gene's distinctive checkpoint role is orthogonal to the ALP-sealing node.
- **Evidence alignment:** Divergent. PN cites the Cells "Key Regulators of Autophagosome Closure" review only. Review cites primary checkpoint/ESCRT papers (PMID:36107470 ESCRT-III-MIT interactome [eLife, verified — not the PN review], PMID:17984323, PMID:20588296). No shared citations.
- **Verdict:** Consistent; review correctly resists the PN autophagy projection. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP4C/CHMP4C-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q96CF2
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
- UniProt: Q96CF2
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
