# CHMP6 PN Consistency Notes

- Generated: 2026-06-18
- Project: PROTEOSTASIS
- Scope: PN consistency rereview against local AIGR review and available deep-research artifacts
- UniProt: Q96FZ7
- AIGR review status: COMPLETE
- Review batch: proteostasis-pr-1217 (PR 1217)
- Batch change status: added

## Source Files Checked

- AIGR review YAML: present - [genes/human/CHMP6/CHMP6-ai-review.yaml](CHMP6-ai-review.yaml)
- AIGR review HTML: present - [genes/human/CHMP6/CHMP6-ai-review.html](CHMP6-ai-review.html)
- Gene notes: present - [genes/human/CHMP6/CHMP6-notes.md](CHMP6-notes.md)
- GOA TSV: present - [genes/human/CHMP6/CHMP6-goa.tsv](CHMP6-goa.tsv)
- UniProt record: present - [genes/human/CHMP6/CHMP6-uniprot.txt](CHMP6-uniprot.txt)
- PN dossier: [projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/CHMP6.md)
- PN consistency section: [projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP6.md](../../../projects/PROTEOSTASIS/reports/phase1_dossiers/_sections/CHMP6.md)
- PN projection report: [projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv](../../../projects/PROTEOSTASIS/reports/pn_projection/pn_projected_gene_go_summary.tsv)
- PN mapping audit: [projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv](../../../projects/PROTEOSTASIS/reports/pn_mapping_audit/current_mapping_scrutiny.tsv)

### Deep Research Files

- No `*-deep-research*.md` file found in this gene directory.

## AIGR Review Snapshot

- Description: CHMP6 encodes the human Vps20 ortholog, a myristoylated ESCRT-III component that acts at endosomal membranes as an acceptor/nucleator for ESCRT-II and helps recruit CHMP4-family ESCRT-III subunits. Its best-supported cellular role is endolysosomal membrane-cargo quality control: MVB assembly and sorting of ubiquitinated/endocytosed cargo, delivery toward lysosomal degradation, and VPS4-mediated ESCRT-III remodeling through its internal MIM2 motif. Broader ESCRT functions in viral budding, cytokinesis, nuclear-envelope sealing, plasma-membrane repair, and autophagy are biologically plausible pathway contexts, but the CHMP6-specific literature makes endosomal MVB sorting the core function.
- Existing/core annotation action counts: ACCEPT: 22; KEEP_AS_NON_CORE: 45; MARK_AS_OVER_ANNOTATED: 14; MODIFY: 5

## PN Consistency Summary

- **Consistency:** Consistent. The review identifies CHMP6 as the human Vps20 ortholog — the myristoylated ESCRT-II→ESCRT-III **nucleator/acceptor** (bridges ESCRT-II to CHMP4 polymerization), which is mechanistically upstream of sealing rather than the sealing effector itself. PN's generic component placement and the review's nucleator framing agree; autophagy entries (GO:0097352 IEA, GO:0016236 TAS PMID:20588296) are KEEP_AS_NON_CORE. No contradiction.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). CHMP6 support is family/role-inheritance, not a CHMP6-specific closure assay; the review explicitly states "cached evidence does not make CHMP6-specific autophagosome maturation the core function" and raises a suggested_question on this. A gene-specific GO:0000045 would over-reach. **PN over-reaches for CHMP6 — already captured at non-core altitude; do not ADD.**
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary literature (PMID:15511219 CHMP6/ESCRT-II acceptor, PMID:17984323, PMID:20588296, PMID:36107470 [verified]). No shared specific citations.
- **Verdict:** Consistent; review correctly distinguishes CHMP6's nucleator role from generic sealing and resists the autophagy projection. **Recommended edits:** none.

## Full Consistency Review

- **UniProt:** Q96FZ7 · **batch:** proteostasis-pr-1217 · **review status:** COMPLETE
- **PN placement:** `ALP → Autophagosome closure maturation and lysosome fusion → Sealing of autophagophore membrane → ESCRT-III complex component` AND `ALP → Microautophagy → General microautophagy machinery → ESCRT-III complex component` (2 rows; shared CHMP template)
- **PN-node mapping:** type → GO:0000815 ESCRT III complex (`already_in_goa_exact`); "Sealing" group → GO:0000045 autophagosome assembly (`more_specific_than_existing_goa`); classes `context_only`/`too_broad`; branch `no_mapping`.
- **Consistency:** Consistent. The review identifies CHMP6 as the human Vps20 ortholog — the myristoylated ESCRT-II→ESCRT-III **nucleator/acceptor** (bridges ESCRT-II to CHMP4 polymerization), which is mechanistically upstream of sealing rather than the sealing effector itself. PN's generic component placement and the review's nucleator framing agree; autophagy entries (GO:0097352 IEA, GO:0016236 TAS PMID:20588296) are KEEP_AS_NON_CORE. No contradiction.
- **PN story / NEW pressure:** PN projects GO:0000045 autophagosome assembly (verified real). CHMP6 support is family/role-inheritance, not a CHMP6-specific closure assay; the review explicitly states "cached evidence does not make CHMP6-specific autophagosome maturation the core function" and raises a suggested_question on this. A gene-specific GO:0000045 would over-reach. **PN over-reaches for CHMP6 — already captured at non-core altitude; do not ADD.**
- **Mapping strategy:** No change. CHMP6's nucleation role fits the ESCRT-III-complex leaf (GO:0000815) well, but its upstream position makes the "Sealing" group→GO:0000045 projection a poor gene-specific fit; class-level `context_only` is the right ceiling.
- **Evidence alignment:** Divergent. PN cites only the Cells "Key Regulators of Autophagosome Closure" review. Review cites primary literature (PMID:15511219 CHMP6/ESCRT-II acceptor, PMID:17984323, PMID:20588296, PMID:36107470 [verified]). No shared specific citations.
- **Verdict:** Consistent; review correctly distinguishes CHMP6's nucleator role from generic sealing and resists the autophagy projection. **Recommended edits:** none.

## PN Dossier Context

- review_batch: proteostasis-pr-1217
- review_yaml: genes/human/CHMP6/CHMP6-ai-review.yaml
- PN workbook rows: 2

## PN row 1: Autophagy-Lysosome Pathway | Autophagosome closure maturation and lysosome fusion | Sealing of autophagophore membrane | ESCRT-III complex component
- UniProt: Q96FZ7
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
- UniProt: Q96FZ7
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
